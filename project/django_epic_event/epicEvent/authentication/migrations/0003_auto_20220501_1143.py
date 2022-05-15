# Generated by Django 4.0.4 on 2022-05-01 11:43

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal

def get_basis_permissions(apps, permission_object, model_name):
    permision_do = [
        "add",
        "change",
        "delete",
        "view",
    ]
    permission_codenames = [f"{do}_{model_name}" for do in permision_do]
    return [permission_object.objects.get(codename=codename) for codename in permission_codenames]

def create_roles(apps, schema_migration):
    Role = apps.get_model('authentication', "Role")
    default_role = [
        "MANAGER",
        "SUPPORT",
        "SALESMAN"
    ]
    for i in default_role:
        try:
            Role.objects.get(name=i)
        except Role.DoesNotExist: 
            role = Role(name=i)
            role.save()
    return

def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    emit_post_migrate_signal(2, False, 'default')
    [
        add_user,
        change_user,
        delete_user,
        view_user,
    ] = get_basis_permissions(apps, Permission, "user")

    [
        add_contrat,
        change_contrat,
        delete_contrat,
        view_contrat,
    ] = get_basis_permissions(apps, Permission, "contrat")
    
    [
        add_event,
        change_event,
        delete_event,
        view_event,
    ] = get_basis_permissions(apps, Permission, "event")

    [
        add_customer,
        change_customer,
        delete_customer,
        view_customer,
    ] = get_basis_permissions(apps, Permission, "customer")

    
    manager_permissions = [
        add_user,
        change_user,
        delete_user,
        view_user,
        add_contrat,
        change_contrat,
        delete_contrat,
        view_contrat,
        add_event,
        change_event,
        delete_event,
        view_event,
        add_customer,
        change_customer,
        delete_customer,
        view_customer,
    ]
    
    managers = Group(name='managers')
    managers.save()
    managers.permissions.add(*manager_permissions)

    support_permissions = [
        add_event,
        change_event,
        delete_event,
        view_event,
        view_user,
        view_contrat,
        view_customer,
    ]
    supports = Group(name='supports')
    supports.save()
    supports.permissions.set(support_permissions)

    salesman_permissions = [
        add_contrat,
        change_contrat,
        delete_contrat,
        view_contrat,
        add_customer,
        change_customer,
        delete_customer,
        view_user,
        view_customer,
        view_event,
    ]
    salesmans = Group(name='salesmans')
    salesmans.save()
    salesmans.permissions.set(salesman_permissions)
    
    for user in User.objects.all():
        if user.role is not None:
            if user.role.name == 'MANAGER':
                managers.user_set.add(user)
            if user.role.name == 'SUPPORT':
                supports.user_set.add(user)
            if user.role.name == 'SALESMAN':
                salesmans.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '__latest__'),
        ('contenttypes', '__latest__'),
        ('authentication', '0002_role_alter_user_options_user_manager_id_and_more'),
        ('event', '__latest__'),
        ('contrat', '__latest__'),
        ('customer', '__latest__'),
    ]

    operations = [
        migrations.RunPython(create_roles, atomic=True),
        migrations.RunPython(create_groups, atomic=True),
    ]
