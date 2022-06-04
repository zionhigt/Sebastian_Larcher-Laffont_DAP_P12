from faker import Faker
from random import randint
import json

fake = Faker()

ALL = {
    "manager": [],
    "salesman": [],
    "support": [],
    "customer": [],
    "contrat": [],
    "event": [],
}

CURRENT_IDS = {
    "user": 1,
    "customer": 1,
    "contrat": 1,
    "event": 1,
}
PSQL_TABLE_NAME = {
    "manager": "authentication_user",
    "salesman": "authentication_user",
    "support": "authentication_user",
    "customer": "customer_customer",
    "contrat": "contrat_contrat",
    "event": "event_event",
}

FIELD_MAPPING = {
    "authentication_user": {
        "role": "role_id",
        "manager_id": "manager_id_id",
    },
    "customer_customer": {
        "sale_contact_id": "sale_contact_id_id",
    },
    "contrat_contrat": {
        "customer_id": "customer_id_id",
        "salesman_id": "salesman_id_id",
    },
    "event_event": {
        "support_contact_id": "support_contact_id_id",
        "contrat_id": "contrat_id_id",
    },
}

def manager_set():
    manager = get_user(role=1, manager_id=None)
    manager_id = manager.get("id")
    ALL.get("manager", []).append(manager)
    for rnd_salesman in range(0, randint(1, 5)):
        salesman_id, salesman = get_salesman_set(manager_id)
        ALL.get("salesman", []).append(salesman)
        for rnd_customer in range(0, randint(1, 5)):
            customer_id, customer = get_customer_set(salesman_id)
            ALL.get("customer", []).append(customer)
            for rnd_contrat in range(0, randint(1, 5)):
                contrat_id, contrat = get_contrat_set(customer_id, salesman_id)
                ALL.get("contrat", []).append(contrat)

                support_id, support = get_support_set(manager_id)
                ALL.get("support", []).append(support)
                event_id, event = get_event_set(support_id, contrat_id)
                ALL.get("event", []).append(event)
    print("MANAGER SET GENERATED")

def get_salesman_set(manager_id):
    salesman = get_user(role=3, manager_id=manager_id)
    salesman_id = salesman.get("id")
    return salesman_id, salesman

def get_support_set(manager_id):
    support = get_user(role=2, manager_id=manager_id)
    support_id = support.get("id")
    return support_id, support

def get_customer_set(salesman_id):
    customer = get_customer(sale_contact_id=salesman_id)
    customer_id = customer.get("id")
    return customer_id, customer

def get_contrat_set(customer_id, salesman_id):
    contrat = get_contrat(customer_id, salesman_id)
    contrat_id = contrat.get("id")
    return contrat_id, contrat

def get_event_set(support_id, contrat_id):
    event = get_event(support_contact_id=support_id, contrat_id=contrat_id)
    event_id = event.get("id")
    return event_id, event

def get_id(table):
    _id = CURRENT_IDS.get(table)
    CURRENT_IDS.update({table: _id + 1})
    return _id

def get_user(role, manager_id):
    id = get_id("user")
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = "%s %s" % (first_name, last_name)
    return {
        "id": id,
        "first_name": first_name[:25],
        "last_name": last_name[:25],
        "username": username[:25],
        "email": fake.email()[:100],
        "password": fake.sha1()[:128],
        "role": role,
        "manager_id": manager_id,
        "is_staff": True,
        "is_active": True,
        "date_joined": fake.date(),
        "is_superuser": False,
    }
def get_contrat(customer_id, salesman_id):
    id = get_id("contrat")
    return {
        "id": id,
        "customer_id": customer_id,
        "salesman_id": salesman_id,
        "date_created": fake.date(),
        "date_updated": fake.date(),
        "status": 0,
        "amount": randint(1000, 6000),
        "payment_due": fake.date(),
    }
def get_customer(sale_contact_id):
    id = get_id("customer")
    return {
        "id": id,
        "first_name": fake.first_name()[:25],
        "last_name": fake.last_name()[:25],
        "email": fake.email()[:100],
        "date_created": fake.date(),
        "date_updated": fake.date(),
        "company_name": fake.company()[:25],
        "sale_contact_id": sale_contact_id,
        "status": 0,
        "mobile": fake.phone_number()[:20],
        "phone": fake.phone_number()[:20],

    }
def get_event(support_contact_id, contrat_id):
    id = get_id("event")
    name = "%s %s" % (fake.first_name(),  fake.color_name())
    return {
        "id": id,
        "name": name[:25],
        "description": fake.text()[:200],
        "date_created": fake.date(),
        "date_updated": fake.date(),
        "support_contact_id": support_contact_id,
        "contrat_id": contrat_id,
        "status_id": 1,

    }

def get_data_set():
    for rnd_manager in range(0, randint(1, 5)):
        manager_set()

def extract_keys(dictionary):
    return dictionary.keys()

def remap(table, map):
    new_map = []
    for record in map:
        new_record = {}
        for key, value in record.items():
            new_key = FIELD_MAPPING.get(table).get(key, key)
            new_record.update({new_key: value})
        new_map.append(new_record)
    return new_map

def prepare_insert_query(table):
    psql_table_name = PSQL_TABLE_NAME.get(table)
    table_data = remap(psql_table_name, ALL.get(table))
    template_select_query = "SELECT * FROM json_populate_recordset(NULL::%s, '%s')"
    select_query = template_select_query % (
        psql_table_name,
        json.dumps(table_data)
    )
    template_insert_query = "INSERT INTO %s\n%s;\n"
    insert_query = template_insert_query % (
        psql_table_name,
        select_query
    )

    return insert_query

def prepare_query():
    get_data_set()
    for TABLE in ALL.keys():
        yield TABLE, prepare_insert_query(TABLE)

records = prepare_query()
for table, record in records:
    with open("./data/%s.sql" % table, "w") as data_file:
        data_file.writelines(record)
        data_file.close()


