#! /bin/bash

set -e
psql -d epic_event_migration_test < ./data/manager.sql
psql -d epic_event_migration_test < ./data/salesman.sql
psql -d epic_event_migration_test < ./data/support.sql
psql -d epic_event_migration_test < ./data/customer.sql
psql -d epic_event_migration_test < ./data/contrat.sql
psql -d epic_event_migration_test < ./data/event.sql