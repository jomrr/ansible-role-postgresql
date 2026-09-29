# Ansible Role: postgresql

![GitHub](https://img.shields.io/github/license/jomrr/ansible-role-postgresql)
![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/ansible-role-postgresql)
![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/ansible-role-postgresql)
[![dev](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-postgresql/dev.yml?branch=dev&label=dev)](https://github.com/jomrr/ansible-role-postgresql/actions/workflows/dev.yml?query=branch%3Adev)
[![main](https://img.shields.io/github/actions/workflow/status/jomrr/ansible-role-postgresql/main.yml?branch=main&label=main)](https://github.com/jomrr/ansible-role-postgresql/actions/workflows/main.yml?query=branch%3Amain)

Ansible role for installing and managing PostgreSQL.

## Purpose

This role installs, configures, and manages PostgreSQL runtime state.

## Scope

### Managed

- PostgreSQL packages through platform-specific package lists
- Distribution-native default PostgreSQL cluster initialization
- PostgreSQL service enablement and runtime state
- Managed PostgreSQL conf.d snippets
- Managed pg_hba.conf and pg_ident.conf
- PostgreSQL roles, memberships, tablespaces, databases, and extensions with
  per-object state
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

- PostgreSQL 15 or newer and the community.postgresql collection from
  collections.yml.
- Target host must provide psycopg2 or psycopg3 through the platform package
  list.
- Local Unix-socket access as the PostgreSQL superuser postgres must use peer
  authentication.
- The first HBA entry must be local all postgres peer without authentication
  options.

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

### `postgresql_no_log`

Type: `bool`. Required: `false`.

Suppress logs and diffs when processing credentials, free-form settings, or
stored connection data.

Default:

```yaml
postgresql_no_log: true
```

### `postgresql_listen_addresses`

Type: `list`. Required: `false`.

PostgreSQL listen_addresses values.

Default:

```yaml
postgresql_listen_addresses:
  - 127.0.0.1
```

### `postgresql_port`

Type: `int`. Required: `false`.

PostgreSQL TCP port.

Default:

```yaml
postgresql_port: 5432
```

### `postgresql_max_connections`

Type: `int`. Required: `false`.

Maximum concurrent PostgreSQL connections.

Default:

```yaml
postgresql_max_connections: 50
```

### `postgresql_superuser_reserved_connections`

Type: `int`. Required: `false`.

Connections reserved for PostgreSQL superusers.

Default:

```yaml
postgresql_superuser_reserved_connections: 3
```

### `postgresql_shared_buffers`

Type: `str`. Required: `false`.

Shared buffer size optimized for an 8 GB VM default profile.

Default:

```yaml
postgresql_shared_buffers: 2GB
```

### `postgresql_effective_cache_size`

Type: `str`. Required: `false`.

Planner cache estimate optimized for an 8 GB VM default profile.

Default:

```yaml
postgresql_effective_cache_size: 6GB
```

### `postgresql_work_mem`

Type: `str`. Required: `false`.

Per operation work memory.

Default:

```yaml
postgresql_work_mem: 16MB
```

### `postgresql_hash_mem_multiplier`

Type: `str`. Required: `false`.

Hash memory multiplier.

Default:

```yaml
postgresql_hash_mem_multiplier: '2.0'
```

### `postgresql_maintenance_work_mem`

Type: `str`. Required: `false`.

Maintenance work memory.

Default:

```yaml
postgresql_maintenance_work_mem: 512MB
```

### `postgresql_autovacuum_work_mem`

Type: `str`. Required: `false`.

Autovacuum worker memory.

Default:

```yaml
postgresql_autovacuum_work_mem: 128MB
```

### `postgresql_temp_buffers`

Type: `str`. Required: `false`.

Temporary buffer size per session.

Default:

```yaml
postgresql_temp_buffers: 16MB
```

### `postgresql_temp_file_limit`

Type: `str`. Required: `false`.

Maximum temporary file size per process.

Default:

```yaml
postgresql_temp_file_limit: 2GB
```

### `postgresql_max_worker_processes`

Type: `int`. Required: `false`.

Maximum background worker processes.

Default:

```yaml
postgresql_max_worker_processes: 8
```

### `postgresql_max_parallel_workers`

Type: `int`. Required: `false`.

Maximum parallel workers.

Default:

```yaml
postgresql_max_parallel_workers: 4
```

### `postgresql_max_parallel_workers_per_gather`

Type: `int`. Required: `false`.

Maximum parallel workers per gather node.

Default:

```yaml
postgresql_max_parallel_workers_per_gather: 2
```

### `postgresql_max_parallel_maintenance_workers`

Type: `int`. Required: `false`.

Maximum parallel maintenance workers.

Default:

```yaml
postgresql_max_parallel_maintenance_workers: 2
```

### `postgresql_wal_level`

Type: `str`. Required: `false`.

PostgreSQL WAL level. Use logical for logical replication
publishers/subscribers.

Default:

```yaml
postgresql_wal_level: replica
```

### `postgresql_max_wal_senders`

Type: `int`. Required: `false`.

Maximum concurrent WAL sender processes.

Default:

```yaml
postgresql_max_wal_senders: 4
```

### `postgresql_max_replication_slots`

Type: `int`. Required: `false`.

Maximum replication slots.

Default:

```yaml
postgresql_max_replication_slots: 4
```

### `postgresql_max_logical_replication_workers`

Type: `int`. Required: `false`.

Maximum logical replication workers.

Default:

```yaml
postgresql_max_logical_replication_workers: 4
```

### `postgresql_max_sync_workers_per_subscription`

Type: `int`. Required: `false`.

Maximum sync workers per subscription.

Default:

```yaml
postgresql_max_sync_workers_per_subscription: 2
```

### `postgresql_fsync`

Type: `str`. Required: `false`.

Whether fsync is enabled.

Default:

```yaml
postgresql_fsync: 'on'
```

### `postgresql_full_page_writes`

Type: `str`. Required: `false`.

Whether full page writes are enabled.

Default:

```yaml
postgresql_full_page_writes: 'on'
```

### `postgresql_synchronous_commit`

Type: `str`. Required: `false`.

Synchronous commit setting.

Default:

```yaml
postgresql_synchronous_commit: 'on'
```

### `postgresql_wal_compression`

Type: `str`. Required: `false`.

WAL compression setting.

Default:

```yaml
postgresql_wal_compression: 'on'
```

### `postgresql_checkpoint_timeout`

Type: `str`. Required: `false`.

Checkpoint timeout.

Default:

```yaml
postgresql_checkpoint_timeout: 15min
```

### `postgresql_checkpoint_completion_target`

Type: `str`. Required: `false`.

Checkpoint completion target.

Default:

```yaml
postgresql_checkpoint_completion_target: '0.9'
```

### `postgresql_max_wal_size`

Type: `str`. Required: `false`.

Maximum WAL size before checkpoints.

Default:

```yaml
postgresql_max_wal_size: 4GB
```

### `postgresql_min_wal_size`

Type: `str`. Required: `false`.

Minimum WAL size.

Default:

```yaml
postgresql_min_wal_size: 512MB
```

### `postgresql_autovacuum`

Type: `str`. Required: `false`.

Whether autovacuum is enabled.

Default:

```yaml
postgresql_autovacuum: 'on'
```

### `postgresql_autovacuum_max_workers`

Type: `int`. Required: `false`.

Maximum autovacuum workers.

Default:

```yaml
postgresql_autovacuum_max_workers: 2
```

### `postgresql_autovacuum_naptime`

Type: `str`. Required: `false`.

Autovacuum naptime.

Default:

```yaml
postgresql_autovacuum_naptime: 1min
```

### `postgresql_autovacuum_vacuum_scale_factor`

Type: `str`. Required: `false`.

Autovacuum vacuum scale factor.

Default:

```yaml
postgresql_autovacuum_vacuum_scale_factor: '0.05'
```

### `postgresql_autovacuum_analyze_scale_factor`

Type: `str`. Required: `false`.

Autovacuum analyze scale factor.

Default:

```yaml
postgresql_autovacuum_analyze_scale_factor: '0.05'
```

### `postgresql_autovacuum_vacuum_cost_delay`

Type: `str`. Required: `false`.

Autovacuum cost delay.

Default:

```yaml
postgresql_autovacuum_vacuum_cost_delay: 10ms
```

### `postgresql_autovacuum_vacuum_cost_limit`

Type: `int`. Required: `false`.

Autovacuum cost limit.

Default:

```yaml
postgresql_autovacuum_vacuum_cost_limit: 1000
```

### `postgresql_random_page_cost`

Type: `str`. Required: `false`.

Planner random page cost for SSD-backed VM storage.

Default:

```yaml
postgresql_random_page_cost: '1.5'
```

### `postgresql_effective_io_concurrency`

Type: `int`. Required: `false`.

Planner effective I/O concurrency.

Default:

```yaml
postgresql_effective_io_concurrency: 32
```

### `postgresql_maintenance_io_concurrency`

Type: `int`. Required: `false`.

Maintenance I/O concurrency.

Default:

```yaml
postgresql_maintenance_io_concurrency: 16
```

### `postgresql_timezone`

Type: `str`. Required: `false`.

PostgreSQL timezone.

Default:

```yaml
postgresql_timezone: UTC
```

### `postgresql_log_timezone`

Type: `str`. Required: `false`.

PostgreSQL log timezone.

Default:

```yaml
postgresql_log_timezone: UTC
```

### `postgresql_datestyle`

Type: `str`. Required: `false`.

PostgreSQL datestyle.

Default:

```yaml
postgresql_datestyle: iso, ymd
```

### `postgresql_lc_messages`

Type: `str`. Required: `false`.

Locale used for PostgreSQL system error messages.

Default:

```yaml
postgresql_lc_messages: null
```

### `postgresql_lc_monetary`

Type: `str`. Required: `false`.

Locale used for PostgreSQL monetary formatting.

Default:

```yaml
postgresql_lc_monetary: null
```

### `postgresql_lc_numeric`

Type: `str`. Required: `false`.

Locale used for PostgreSQL number formatting.

Default:

```yaml
postgresql_lc_numeric: null
```

### `postgresql_lc_time`

Type: `str`. Required: `false`.

Locale used for PostgreSQL date and time formatting.

Default:

```yaml
postgresql_lc_time: null
```

### `postgresql_default_text_search_config`

Type: `str`. Required: `false`.

Default text search configuration.

Default:

```yaml
postgresql_default_text_search_config: pg_catalog.english
```

### `postgresql_password_encryption`

Type: `str`. Required: `false`.

Default password encryption method.

Default:

```yaml
postgresql_password_encryption: scram-sha-256
```

### `postgresql_ssl`

Type: `str`. Required: `false`.

Enable TLS for PostgreSQL client connections.

Default:

```yaml
postgresql_ssl: 'off'
```

### `postgresql_ssl_cert_file`

Type: `str`. Required: `false`.

Server certificate file used by PostgreSQL TLS.

Default:

```yaml
postgresql_ssl_cert_file: null
```

### `postgresql_ssl_key_file`

Type: `str`. Required: `false`.

Server private key file used by PostgreSQL TLS.

Default:

```yaml
postgresql_ssl_key_file: null
```

### `postgresql_ssl_ca_file`

Type: `str`. Required: `false`.

Trusted CA file used for PostgreSQL client certificate validation.

Default:

```yaml
postgresql_ssl_ca_file: null
```

### `postgresql_ssl_crl_file`

Type: `str`. Required: `false`.

Certificate revocation list file used by PostgreSQL TLS.

Default:

```yaml
postgresql_ssl_crl_file: null
```

### `postgresql_ssl_crl_dir`

Type: `str`. Required: `false`.

Certificate revocation list directory used by PostgreSQL TLS.

Default:

```yaml
postgresql_ssl_crl_dir: null
```

### `postgresql_ssl_ciphers`

Type: `str`. Required: `false`.

TLS cipher list for TLS 1.2 and older.

Default:

```yaml
postgresql_ssl_ciphers: null
```

### `postgresql_ssl_tls13_ciphers`

Type: `str`. Required: `false`.

TLS 1.3 cipher suites.

Default:

```yaml
postgresql_ssl_tls13_ciphers: null
```

### `postgresql_ssl_prefer_server_ciphers`

Type: `str`. Required: `false`.

Whether PostgreSQL should prefer the server cipher order.

Default:

```yaml
postgresql_ssl_prefer_server_ciphers: 'on'
```

### `postgresql_ssl_min_protocol_version`

Type: `str`. Required: `false`.

Minimum TLS protocol version.

Default:

```yaml
postgresql_ssl_min_protocol_version: null
```

### `postgresql_ssl_max_protocol_version`

Type: `str`. Required: `false`.

Maximum TLS protocol version.

Default:

```yaml
postgresql_ssl_max_protocol_version: null
```

### `postgresql_ssl_dh_params_file`

Type: `str`. Required: `false`.

Diffie-Hellman parameters file used by PostgreSQL TLS.

Default:

```yaml
postgresql_ssl_dh_params_file: null
```

### `postgresql_ssl_passphrase_command`

Type: `str`. Required: `false`.

Command used to unlock passphrase-protected private keys.

Default:

```yaml
postgresql_ssl_passphrase_command: null
```

### `postgresql_ssl_passphrase_command_supports_reload`

Type: `str`. Required: `false`.

Whether the TLS passphrase command may be used during reload.

Default:

```yaml
postgresql_ssl_passphrase_command_supports_reload: 'off'
```

### `postgresql_log_destination`

Type: `str`. Required: `false`.

PostgreSQL log destination.

Default:

```yaml
postgresql_log_destination: stderr
```

### `postgresql_logging_collector`

Type: `str`. Required: `false`.

Whether PostgreSQL logging collector is enabled.

Default:

```yaml
postgresql_logging_collector: 'off'
```

### `postgresql_log_statement`

Type: `str`. Required: `false`.

PostgreSQL statement logging level.

Default:

```yaml
postgresql_log_statement: none
```

### `postgresql_log_min_duration_statement`

Type: `int`. Required: `false`.

Log statements running at least this many milliseconds.

Default:

```yaml
postgresql_log_min_duration_statement: 1000
```

### `postgresql_log_temp_files`

Type: `str`. Required: `false`.

Log temp files above this size.

Default:

```yaml
postgresql_log_temp_files: 64MB
```

### `postgresql_log_checkpoints`

Type: `str`. Required: `false`.

Whether checkpoint logging is enabled.

Default:

```yaml
postgresql_log_checkpoints: 'on'
```

### `postgresql_log_autovacuum_min_duration`

Type: `str`. Required: `false`.

Log autovacuum actions above this duration.

Default:

```yaml
postgresql_log_autovacuum_min_duration: 1min
```

### `postgresql_config_extra_reload`

Type: `list`. Required: `false`.

Additional PostgreSQL settings expected to become effective after a reload.
Entries require name and value. The optional quote flag defaults to true.

Default:

```yaml
postgresql_config_extra_reload: []
```

### `postgresql_config_extra_restart`

Type: `list`. Required: `false`.

Additional PostgreSQL settings expected to require a PostgreSQL restart.
Entries require name and value. The optional quote flag defaults to true.

Default:

```yaml
postgresql_config_extra_restart: []
```

### `postgresql_pg_ident_entries`

Type: `list`. Required: `false`.

Entries rendered into the fully managed pg_ident.conf file.

Default:

```yaml
postgresql_pg_ident_entries: []
```

### `postgresql_hba_entries`

Type: `list`. Required: `false`.

Entries rendered into the fully managed pg_hba.conf file.
The first entry must be local all postgres peer without authentication options.

Default:

```yaml
postgresql_hba_entries:
  - type: local
    database: all
    user: postgres
    method: peer
  - type: host
    database: all
    user: all
    address: 127.0.0.1/32
    method: scram-sha-256
```

### `postgresql_roles`

Type: `list`. Required: `false`.

PostgreSQL roles and login users managed through per-object state.

Default:

```yaml
postgresql_roles: []
```

### `postgresql_memberships`

Type: `list`. Required: `false`.

PostgreSQL role memberships managed through per-object state.

Default:

```yaml
postgresql_memberships: []
```

### `postgresql_tablespaces`

Type: `list`. Required: `false`.

PostgreSQL tablespaces managed through per-object state.

Default:

```yaml
postgresql_tablespaces: []
```

### `postgresql_databases`

Type: `list`. Required: `false`.

PostgreSQL databases managed through per-object state.

Default:

```yaml
postgresql_databases: []
```

### `postgresql_extensions`

Type: `list`. Required: `false`.

PostgreSQL extensions managed through per-object state in their target database.

Default:

```yaml
postgresql_extensions: []
```

### `postgresql_publications`

Type: `list`. Required: `false`.

Logical replication publications managed through per-object state in their
source database.

Default:

```yaml
postgresql_publications: []
```

### `postgresql_subscriptions`

Type: `list`. Required: `false`.

Logical replication subscriptions managed through per-object state in their
local database.

Default:

```yaml
postgresql_subscriptions: []
```

## Managed Files

- `PostgreSQL configuration directory conf.d/*.conf`
- `pg_hba.conf`
- `pg_ident.conf`

## Check Mode

Package and template tasks support check mode. First-run cluster initialization
and database-object changes depend on platform command/module support.

- Read-only cluster discovery commands are marked changed_when=false.
- PostgreSQL object modules from community.postgresql provide check mode where
  supported by the module.

## Service Behavior

The service is always enabled at boot and started after configuration. Reloads
and restarts happen only through handlers.

### Handlers

- apply configuration

## Security Notes

- postgresql_no_log defaults to true and protects role tasks that manage
  passwords and role-specific settings.
- Other object entries without management passwords show their names and change
  status. Tablespace directory tasks receive only file metadata.
- Subscription results remain protected because the module returns stored
  connection credentials, even when no password is supplied.
- HBA files, free-form configuration and TLS passphrase settings remain
  protected; ordinary settings and identity mappings are visible.
- pg_hba.conf and pg_ident.conf are fully managed to avoid conflicting stale
  rules.
- Durability settings keep fsync, full_page_writes, and synchronous_commit
  enabled by default.

## Operational Notes

- Repeated runs with unchanged inputs are idempotent and do not reload or
  restart PostgreSQL.
- Configuration changes reload the server; pending_restart or changed restart
  extras trigger a restart when required.
- Configuration snippets and the main include directive use native module
  validation before writing. Module backups remain available.
- HBA and Ident files have no separate preflight validation; PostgreSQL reads
  them during service start or reload.
- Certificate issuance and deployment remain external responsibilities.
- Defaults are tuned for a small dedicated 8 GB RAM / 4 vCPU VM on SSD-backed
  storage.
- Per-object state=absent is supported only where the underlying
  community.postgresql module supports it cleanly.
- The role does not orchestrate dependency-safe destructive cleanup across
  related PostgreSQL objects.
- Logical replication copies DML changes, not DDL. Schema migrations must be
  orchestrated outside this role.
- Debian and Ubuntu use the package-provided main cluster and resolve its
  standard paths from pg_config --bindir.
- TLS configuration settings are managed as PostgreSQL config values;
  certificate issuance and file deployment stay outside this role.

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
postgresql_ssl: "on"
postgresql_ssl_cert_file: /etc/postgresql/tls/server.crt
postgresql_ssl_key_file: /etc/postgresql/tls/server.key
postgresql_ssl_ca_file: /etc/postgresql/tls/root-ca.crt
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

- [Ansible community.postgresql collection](https://docs.ansible.com/ansible/latest/collections/community/postgresql/)
- [PostgreSQL logical replication](https://www.postgresql.org/docs/current/logical-replication.html)
- [PostgreSQL SSL support](https://www.postgresql.org/docs/current/ssl-tcp.html)

## Author

[Jonas Mauer](https://github.com/jomrr)

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for the full license text.

Copyright (c) 2020-2026 Jonas Mauer.
