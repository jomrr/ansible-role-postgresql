# ansible-role-postgresql

Ansible role for setting up postgresql.

By default this role sets up a PostgreSQL database with the following settings

* default tablespace
* listen_addresses = localhost
* socket auth for postgresql user and all local users
* md5 auth for localhost only
* NO replication

## Supported Platforms

* CentOS 7, 8
* Debian 10
* Fedora 31
* Ubuntu 18.04, 20.04

## Requirements

Ansible 2.9 or higher is recommended.

## Variables

Variables and defaults for this role:

| variable | default value in defaults/main.yml | description |
| -------- | ---------------------------------- | ----------- |
| postgresql_enabled | False | determine whether role is enabled (True) or not (False) |
| postgresql_listen_addresses | ['localhost'] | Listen addressess for daemon |
| postgresql_locales | ['en_US.UTF-8', 'de_DE.UTF-8'] | Supported locales (on Debian-based OSes) |
| postgresql_user | 'postgres' | The postgres user |
| postgresql_group | 'postgres' | The postgres group |
| postgresql_global_config_options | [{option:..., value: ...}, ...] | postgresql.conf: see [defaults/main.yml](https://github.com/jam82/ansible-role-postgresql/blob/master/defaults/main.yml) |
| postgresql_hba_entries | [{type: ...,...},...] | pg_hba.conf: see [defaults/main.yml](https://github.com/jam82/ansible-role-postgresql/blob/master/defaults/main.yml)
| postgresql_databases | [{name: exampledb,...}...] | Configured databases: see [defaults/main.yml](https://github.com/jam82/ansible-role-postgresql/blob/master/defaults/main.yml)
| postgresql_users | [{name: example,...}...] | Configured users: see [defaults/main.yml](https://github.com/jam82/ansible-role-postgresql/blob/master/defaults/main.yml)
| postgresql_no_log | True | Boolean for controlling the no_log option when creating users |


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

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.

## References

[PostgreSQL](https://www.postgresql.org/docs/manuals/)
