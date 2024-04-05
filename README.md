# ansible-role-postgresql

![GitHub](https://img.shields.io/github/license/jomrr/ansible-role-postgresql) ![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/ansible-role-postgresql) ![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/ansible-role-postgresql) ![Travis (.com) branch](https://img.shields.io/travis/com/jomrr/ansible-role-postgresql/main?label=ansible-lint%20latest)

**Ansible role for setting up postgresql.**

## General Information

> This role does not setup locales on the target systems.

Please read section Variables to adjust the configuration.

## Supported Versions and Platforms

| OS Family | Distribution  | Latest | Supported Version(s) | Comment |
|-----------|---------------|--------|----------------------|---------|
| Alpine    | Alpine        | :heavy_check_mark: | 3.12, 3.13 | |
| Archlinux | Archlinux     | :heavy_check_mark: | - | |
|           | Manjaro       | :heavy_check_mark: | - | |
| Debian    | Debian        | :heavy_check_mark: | 10, 11 | |
|           | Ubuntu        | :heavy_check_mark: | 18.04, 20.04 | |
| RedHat    | Almalinux     | :heavy_check_mark: | 8 | |
|           | Amazonlinux   | :x: | - | not tested, image not working |
|           | Centos        | :heavy_check_mark: | 8 | |
|           | Fedora        | :heavy_check_mark: | 33, 34, Rawhide | |
|           | Oraclelinux   | :heavy_check_mark: | 7, 8 | |
| Suse      | OpenSuse Leap | :heavy_check_mark: | 15.1, 15.2, 15.3 | |
|           | Tumbleweed    | :heavy_check_mark: | - | |

## Requirements

Ansible 2.9 or higher is recommended.

## Variables

Variables and defaults for this role.

### defaults/main.yml

```yaml
# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which includes tasks/tasks.yml if enabled.
postgresql_role_enabled: false

# Prevent logging of sensitive information in postgres modules.
# Turn to false for debugging purposes.
postgresql_no_log: true

# The addresses to bind to.
postgresql_listen_addresses:
  - 127.0.0.1

# The listening port.
postgresql_port: 5432

# Change here to use a non-default location for the data dir.
postgresql_data_dir: "{{ postgresql_default_data_dir }}"

# Usually the default one.
postgresql_unix_socket_directories:
  - "{{ postgres_default_unix_socket_directory }}"

# This allows local users to authenticate via socket.
# Set to something more restrictive if you do not need that.
# Owner and group are postgres.
postgresql_unix_socket_directories_mode: 02775

# Global configuration options that will be set in postgresql.conf.
# Alter the distribution configuration file via lineinfile.
# You can also set state: present|absent.
# ATTENTION:
# Change password_encryption to e.g. to scram-sha-256 with versions >= 10.
# The value 'on' is for Amazon Linux compatibility only and defaults to md5
# also in the current versions of postgresql.
postgresql_conf:
  - key: listen_addresses
    value: "{{ postgresql_listen_addresses | join(',') }}"
  - key: port
    value: "{{ postgresql_port }}"
    state: present
  - key: unix_socket_directories
    value: "{{ postgresql_unix_socket_directories | join(',') }}"
  - key: password_encryption
    value: 'on'
  - key: timezone
    value: 'UTC'
  - key: log_timezone
    value: 'UTC'
  - key: datestyle
    value: 'iso, ymd'
  - key: default_text_search_config
    value: 'pg_catalog.english'

# Entries for pg_hba.conf (host based authentication).
# These are compatibility settings for Amazon Linuxs' version 9.2 of postgres.
# Change on versions >=10 and e.g. use scram-sha-256 instead of ident:
#  - { type: local, database: all, user: postgres, auth_method: peer }
#  - { type: local, database: all, user: all, auth_method: scram-sha-256 }
#  - { type: host, database: all, user: all, address: '127.0.0.1/32', auth_method: scram-sha256 }
# POSSIBLE KEYS:
# type, database, user, address, ip_address, ip_mask, auth_method, auth_options
postgresql_hba:
  - { type: local, database: all, user: all, auth_method: peer }
  - { type: host, database: all, user: all, address: '127.0.0.1/32', auth_method: ident }

# Databases.
# see: https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_db_module.html
postgresql_databases: []
#  - name: awesomedb    # required; the rest is optional
#    state:             # default('present')
#    ca_cert:           # default(omit)
#    conn_limit:        # default(omit)
#    dump_extra_args:   # default(omit)
#    encoding:          # default(omit)
#    lc_collate:        # default(omit)
#    lc_ctype:          # default(omit)
#    login_host:        # default(omit)
#    login_password:    # default(omit)
#    login_unix_socket: # default(omit)
#    login_user:        # default(omit)
#    maintenance_db:    # default(omit)
#    owner:             # default(omit)
#    port:              # default(omit)
#    session_role:      # default(omit)
#    ssl_mode:          # default(omit)
#    tablespace:        # default(omit)
#    target:            # default(omit)
#    target_opts:       # default(omit)
#    template:          # default(omit)
#    trust_input:       # default(omit)

# Users.
# see: https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_user_module.html
postgresql_users: []
#  - name: looseruser     # required; the rest is optional
#    state:               # default('present')
#    ca_cert:             # default(omit)
#    conn_limit:          # default(omit)
#    db:                  # default(omit)
#    encrypted:           # default(omit)
#    expires:             # default(omit)
#    fail_on_user:        # default(omit)
#    groups:              # default(omit)
#    login_host:          # default(omit)
#    login_password:      # default(omit)
#    login_unix_socket:   # default(omit)
#    login_user:          # default(omit)
#    no_password_changes: # default(omit)
#    password:            # default(omit)
#    port:                # default(omit)
#    priv:                # default(omit)
#    role_attr_flags:     # default(omit)
#    session_role:        # default(omit)
#    ssl_mode:            # default(omit)
#    trust_input:         # default(omit)
```

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-postgresql
# play: postgresql
# file: postgresql.yml

- hosts: all
  become: true
  gather_facts: true
  vars:
    postgresql_role_enabled: true
  roles:
    - role: ansible-role-postgresql
```

## Acknowledgements

This role is highly inspired by [Jeff Geerlings postgresql role](https://github.com/geerlingguy/ansible-role-postgresql).

## License and Author

- Author:: [jomrr](https://github.com/jomrr/)
- Copyright:: 2021, [jomrr](https://github.com/jomrr/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jomrr/ansible-role-postgresql/blob/master/LICENSE) file in repository.

## References

- [ArchWiki](https://wiki.archlinux.org/)
