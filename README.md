# Ansible Role: postgresql

![GitHub](https://img.shields.io/github/license/jomrr/ansible-role-postgresql) ![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/ansible-role-postgresql) ![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/ansible-role-postgresql) [![dev](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-postgresql/dev-push-smoke.yml?branch=dev&event=push&label=dev)](https://github.com/jomrr/ansible-role-postgresql/actions/workflows/dev-push-smoke.yml?query=branch%3Adev) [![main](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-postgresql/main-full-gate.yml?branch=main&event=push&label=main)](https://github.com/jomrr/ansible-role-postgresql/actions/workflows/main-full-gate.yml?query=branch%3Amain)

Ansible role for installing and managing PostgreSQL.

## Purpose

This role installs, configures, and manages PostgreSQL runtime state.

## Scope

### Managed

- PostgreSQL packages through platform-specific package lists
- Distribution-native default PostgreSQL cluster initialization or detection
- PostgreSQL service enablement and runtime state
- Managed PostgreSQL conf.d snippets
- Managed pg_hba.conf and pg_ident.conf
- PostgreSQL roles, memberships, tablespaces, databases, and extensions with per-object state
- Logical replication publications and subscriptions with per-object state

### Not Managed

- Global teardown, purge, or cleanup behavior
- Dependency-aware destructive cleanup of PostgreSQL object graphs
- Cross-host replication orchestration
- DDL migration between publisher and subscriber
- Backup and restore policy
- TLS certificate issuance
- Firewall policy
- HA/failover managers such as Patroni or repmgr

## Requirements

- community.postgresql collection installed through the generated requirements.yml artifact.
- Target host must provide psycopg2 or psycopg3 through the platform package list.

## Dependencies

```yaml
collections:
  - name: ansible.posix
  - name: community.general
    version: '>=12.0.0'
  - name: community.postgresql
    version: '>=3.12.0,<5.0.0'
```

## Role Variables

The following variables are part of the public role interface.

| Name | Type | Required | Default | Description |
| ---- | ---- | -------- | ------- | ----------- |
| `postgresql_no_log` | `bool` | `false` | `True` | Suppress logging for PostgreSQL object tasks that may contain credentials. |
| `postgresql_listen_addresses` | `list` | `false` | - 127.0.0.1 | PostgreSQL listen_addresses values. |
| `postgresql_port` | `int` | `false` | `5432` | PostgreSQL TCP port. |
| `postgresql_max_connections` | `int` | `false` | `50` | Maximum concurrent PostgreSQL connections. |
| `postgresql_superuser_reserved_connections` | `int` | `false` | `3` | Connections reserved for PostgreSQL superusers. |
| `postgresql_shared_buffers` | `str` | `false` | `2GB` | Shared buffer size optimized for an 8 GB VM default profile. |
| `postgresql_effective_cache_size` | `str` | `false` | `6GB` | Planner cache estimate optimized for an 8 GB VM default profile. |
| `postgresql_work_mem` | `str` | `false` | `16MB` | Per operation work memory. |
| `postgresql_hash_mem_multiplier` | `str` | `false` | `2.0` | Hash memory multiplier. |
| `postgresql_maintenance_work_mem` | `str` | `false` | `512MB` | Maintenance work memory. |
| `postgresql_autovacuum_work_mem` | `str` | `false` | `128MB` | Autovacuum worker memory. |
| `postgresql_temp_buffers` | `str` | `false` | `16MB` | Temporary buffer size per session. |
| `postgresql_temp_file_limit` | `str` | `false` | `2GB` | Maximum temporary file size per process. |
| `postgresql_max_worker_processes` | `int` | `false` | `8` | Maximum background worker processes. |
| `postgresql_max_parallel_workers` | `int` | `false` | `4` | Maximum parallel workers. |
| `postgresql_max_parallel_workers_per_gather` | `int` | `false` | `2` | Maximum parallel workers per gather node. |
| `postgresql_max_parallel_maintenance_workers` | `int` | `false` | `2` | Maximum parallel maintenance workers. |
| `postgresql_wal_level` | `str` | `false` | `replica` | PostgreSQL WAL level. Use logical for logical replication publishers/subscribers. |
| `postgresql_max_wal_senders` | `int` | `false` | `4` | Maximum concurrent WAL sender processes. |
| `postgresql_max_replication_slots` | `int` | `false` | `4` | Maximum replication slots. |
| `postgresql_max_logical_replication_workers` | `int` | `false` | `4` | Maximum logical replication workers. |
| `postgresql_max_sync_workers_per_subscription` | `int` | `false` | `2` | Maximum sync workers per subscription. |
| `postgresql_fsync` | `str` | `false` | `on` | Whether fsync is enabled. |
| `postgresql_full_page_writes` | `str` | `false` | `on` | Whether full page writes are enabled. |
| `postgresql_synchronous_commit` | `str` | `false` | `on` | Synchronous commit setting. |
| `postgresql_wal_compression` | `str` | `false` | `on` | WAL compression setting. |
| `postgresql_checkpoint_timeout` | `str` | `false` | `15min` | Checkpoint timeout. |
| `postgresql_checkpoint_completion_target` | `str` | `false` | `0.9` | Checkpoint completion target. |
| `postgresql_max_wal_size` | `str` | `false` | `4GB` | Maximum WAL size before checkpoints. |
| `postgresql_min_wal_size` | `str` | `false` | `512MB` | Minimum WAL size. |
| `postgresql_autovacuum` | `str` | `false` | `on` | Whether autovacuum is enabled. |
| `postgresql_autovacuum_max_workers` | `int` | `false` | `2` | Maximum autovacuum workers. |
| `postgresql_autovacuum_naptime` | `str` | `false` | `1min` | Autovacuum naptime. |
| `postgresql_autovacuum_vacuum_scale_factor` | `str` | `false` | `0.05` | Autovacuum vacuum scale factor. |
| `postgresql_autovacuum_analyze_scale_factor` | `str` | `false` | `0.05` | Autovacuum analyze scale factor. |
| `postgresql_autovacuum_vacuum_cost_delay` | `str` | `false` | `10ms` | Autovacuum cost delay. |
| `postgresql_autovacuum_vacuum_cost_limit` | `int` | `false` | `1000` | Autovacuum cost limit. |
| `postgresql_random_page_cost` | `str` | `false` | `1.5` | Planner random page cost for SSD-backed VM storage. |
| `postgresql_effective_io_concurrency` | `int` | `false` | `32` | Planner effective I/O concurrency. |
| `postgresql_maintenance_io_concurrency` | `int` | `false` | `16` | Maintenance I/O concurrency. |
| `postgresql_timezone` | `str` | `false` | `UTC` | PostgreSQL timezone. |
| `postgresql_log_timezone` | `str` | `false` | `UTC` | PostgreSQL log timezone. |
| `postgresql_datestyle` | `str` | `false` | `iso, ymd` | PostgreSQL datestyle. |
| `postgresql_lc_messages` | `str` | `false` | `None` | Locale used for PostgreSQL system error messages. |
| `postgresql_lc_monetary` | `str` | `false` | `None` | Locale used for PostgreSQL monetary formatting. |
| `postgresql_lc_numeric` | `str` | `false` | `None` | Locale used for PostgreSQL number formatting. |
| `postgresql_lc_time` | `str` | `false` | `None` | Locale used for PostgreSQL date and time formatting. |
| `postgresql_default_text_search_config` | `str` | `false` | `pg_catalog.english` | Default text search configuration. |
| `postgresql_password_encryption` | `str` | `false` | `scram-sha-256` | Default password encryption method. |
| `postgresql_log_destination` | `str` | `false` | `stderr` | PostgreSQL log destination. |
| `postgresql_logging_collector` | `str` | `false` | `off` | Whether PostgreSQL logging collector is enabled. |
| `postgresql_log_statement` | `str` | `false` | `none` | PostgreSQL statement logging level. |
| `postgresql_log_min_duration_statement` | `int` | `false` | `1000` | Log statements running at least this many milliseconds. |
| `postgresql_log_temp_files` | `str` | `false` | `64MB` | Log temp files above this size. |
| `postgresql_log_checkpoints` | `str` | `false` | `on` | Whether checkpoint logging is enabled. |
| `postgresql_log_autovacuum_min_duration` | `str` | `false` | `1min` | Log autovacuum actions above this duration. |
| `postgresql_config_extra_reload` | `list` | `false` | [] | Additional PostgreSQL settings expected to become effective after a reload. |
| `postgresql_config_extra_restart` | `list` | `false` | [] | Additional PostgreSQL settings expected to require a PostgreSQL restart. |
| `postgresql_pg_ident_entries` | `list` | `false` | [] | Entries rendered into the fully managed pg_ident.conf file. |
| `postgresql_hba_entries` | `list` | `false` | - type: local<br />  database: all<br />  user: postgres<br />  method: peer<br />- type: local<br />  database: all<br />  user: all<br />  method: peer<br />- type: host<br />  database: all<br />  user: all<br />  address: 127.0.0.1/32<br />  method: scram-sha-256 | Entries rendered into the fully managed pg_hba.conf file. |
| `postgresql_roles` | `list` | `false` | [] | PostgreSQL roles and login users managed through per-object state. |
| `postgresql_memberships` | `list` | `false` | [] | PostgreSQL role memberships managed through per-object state. |
| `postgresql_tablespaces` | `list` | `false` | [] | PostgreSQL tablespaces managed through per-object state. |
| `postgresql_databases` | `list` | `false` | [] | PostgreSQL databases managed through per-object state. |
| `postgresql_extensions` | `list` | `false` | [] | PostgreSQL extensions managed through per-object state in their target database. |
| `postgresql_publications` | `list` | `false` | [] | Logical replication publications managed through per-object state in their source database. |
| `postgresql_subscriptions` | `list` | `false` | [] | Logical replication subscriptions managed through per-object state in their local database. |

## Managed Files

- `PostgreSQL configuration directory conf.d/*.conf`
- `pg_hba.conf`
- `pg_ident.conf`

## Check Mode

Package and template tasks support check mode. First-run cluster initialization and database-object changes depend on platform command/module support.

- Read-only cluster discovery commands are marked changed_when=false.
- PostgreSQL object modules from community.postgresql provide check mode where supported by the module.

## Service Behavior

The service is always enabled at boot and started after configuration. Reloads and restarts happen only through handlers.

### Handlers

- Validate postgresql configuration
- Mark postgresql restart required
- Apply postgresql configuration

## Security Notes

- postgresql_no_log defaults to true for object tasks that may contain credentials.
- pg_hba.conf and pg_ident.conf are fully managed to avoid conflicting stale rules.
- Durability settings keep fsync, full_page_writes, and synchronous_commit enabled by default.

## Operational Notes

- Defaults are tuned for a small dedicated 8 GB RAM / 4 vCPU VM on SSD-backed storage.
- Per-object state=absent is supported only where the underlying community.postgresql module supports it cleanly.
- The role does not orchestrate dependency-safe destructive cleanup across related PostgreSQL objects.
- Logical replication copies DML changes, not DDL. Schema migrations must be orchestrated outside this role.
- Debian and Ubuntu use postgresql-common cluster discovery via pg_lsclusters instead of static major-version maps.

## Supported Platforms

| OS Family | Distribution | Version | Container Image |
| --------- | ------------ | ------- | --------------- |
| RedHat | AlmaLinux | latest | [jomrr/molecule-almalinux:latest](https://hub.docker.com/r/jomrr/molecule-almalinux) |
| Debian | Debian | latest | [jomrr/molecule-debian:latest](https://hub.docker.com/r/jomrr/molecule-debian) |
| RedHat | Fedora | latest | [jomrr/molecule-fedora:latest](https://hub.docker.com/r/jomrr/molecule-fedora) |
| Suse | OpenSuse Leap | latest | [jomrr/molecule-opensuse-leap:latest](https://hub.docker.com/r/jomrr/molecule-opensuse-leap) |
| Suse | OpenSuse Tumbleweed | latest | [jomrr/molecule-opensuse-tumbleweed:latest](https://hub.docker.com/r/jomrr/molecule-opensuse-tumbleweed) |
| Debian | Ubuntu | latest | [jomrr/molecule-ubuntu:latest](https://hub.docker.com/r/jomrr/molecule-ubuntu) |

## Example Playbook

### Small local PostgreSQL instance

Apply the default small-VM PostgreSQL profile.

```yaml
---
- name: Configure PostgreSQL
  hosts: postgresql
  gather_facts: true
  roles:
    - role: jomrr.postgresql
```
### Managed database with extension

Create a login role, an application database, and an extension.

```yaml
---
postgresql_roles:
  - name: app
    role_attr_flags: LOGIN

postgresql_databases:
  - name: appdb
    owner: app
    encoding: UTF8

postgresql_extensions:
  - name: pgcrypto
    database: appdb
```
### Logical replication publisher

Publish all tables in schema app from database appdb.

```yaml
---
postgresql_wal_level: logical
postgresql_listen_addresses:
  - 127.0.0.1
  - 10.10.20.11
postgresql_roles:
  - name: replicator
    role_attr_flags: LOGIN,REPLICATION
    password: "{{ vault_postgresql_replicator_password }}"
postgresql_hba_entries:
  - type: local
    database: all
    user: postgres
    method: peer
  - type: hostssl
    database: appdb
    user: replicator
    address: 10.10.20.12/32
    method: scram-sha-256
postgresql_publications:
  - name: app_publication
    database: appdb
    tables_in_schema:
      - app
    parameters:
      publish: insert, update, delete, truncate
```

## References

- https://docs.ansible.com/ansible/latest/collections/community/postgresql/
- https://www.postgresql.org/docs/current/logical-replication.html

## Author

[Jonas Mauer](https://github.com/jomrr)

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for the full license text.

Copyright (c) 2020-2026 Jonas Mauer.
