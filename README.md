# ansible-role-postgresql

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-postgresql) [![Build Status](https://travis-ci.org/jam82/ansible-role-postgresql.svg?branch=master)](https://travis-ci.org/jam82/ansible-role-postgresql)

**Ansible role for setting up postgresql.**

By default this role sets up a PostgreSQL database with the following settings

- default tablespace
- listen_addresses = localhost
- socket auth for postgresql user and all local users
- md5 auth for localhost only
- NO replication

## Supported Platforms

- CentOS 7, 8
- Debian 10
- Fedora 31
- Ubuntu 18.04, 20.04

## Requirements

Ansible 2.9 or higher is recommended.

## Variables

Variables and defaults for this role:

```yaml
---
# role: ansible-role-postgresql
# file: defaults/main.yml

# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which includes tasks.yml if enabled.
postgresql_enabled: False

postgresql_listen_addresses:
  - localhost

postgresql_locales:
  - 'de_DE.UTF-8'
  - 'en_US.UTF-8'

postgresql_user: postgres
postgresql_group: postgres

# Global configuration options that will be set in postgresql.conf.
postgresql_global_config_options:
  - option: unix_socket_directories
    value: "{{ postgresql_unix_socket_directories | join(',') }}"
  - option: listen_addresses
    value: "{{ postgresql_listen_addresses | join(',') }}"

# Entries for pg_hba.conf (host based authentication).
# possible keys: type, database, user, address, ip_address, ip_mask, auth_method, auth_options
postgresql_hba_entries:
  - { type: local, database: all, user: postgres, auth_method: peer }
  - { type: local, database: all, user: all, auth_method: peer }
  - { type: host, database: all, user: all, address: '127.0.0.1/32', auth_method: md5 }

# Databases to configure.
postgresql_databases: []
# - name: foremandb # required; the rest are optional
#   lc_collate: # defaults to 'en_US.UTF-8'
#   lc_ctype: # defaults to 'en_US.UTF-8'
#   encoding: # defaults to 'UTF-8'
#   template: # defaults to 'template0'
#   login_host: # defaults to 'localhost'
#   login_password: # defaults to not set
#   login_user: # defaults to '{{ postgresql_user }}'
#   login_unix_socket: # defaults to 1st of postgresql_unix_socket_directories
#   port: # defaults to not set
#   owner: # defaults to postgresql_user
#   state: # defaults to 'present'

# Users to configure.
postgresql_users: []
# - name: foreman #required; the rest are optional
#   password: # defaults to not set
#   encrypted: # defaults to not set
#   priv: # defaults to not set
#   role_attr_flags: # defaults to not set
#   db: # defaults to not set
#   login_host: # defaults to 'localhost'
#   login_password: # defaults to not set
#   login_user: # defaults to '{{ postgresql_user }}'
#   login_unix_socket: # defaults to 1st of postgresql_unix_socket_directories
#   port: # defaults to not set
#   state: # defaults to 'present'

# Do not output ansible log data, i.e. when managing users.
postgresql_no_log: True
```

## Dependencies

None.

## Example Playbook

```yaml
---
# playbook: myawesomesite
# file: site.yml

- hosts: postgresql_systems
  become: True
  vars:
    postgresql_enabled: True
  roles:
    - role: ansible-role-postgresql
```

## Acknowledgements

This role is highly inspired by [Jeff Geerlings postgresql role](https://github.com/geerlingguy/ansible-role-postgresql). It is adopted to my ansible-role-skeleton and comes with slightly different default settings and listening_addresses set to localhost.

## License and Author

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2020, [jam82](https://github.com/jam82/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jam82/ansible-role-updates/blob/master/LICENSE) file in repository.

## References

[PostgreSQL](https://www.postgresql.org/docs/manuals/)
