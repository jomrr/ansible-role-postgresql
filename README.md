# ansible-role-postgresql

Ansible role for setting up postgresql.

## Supported Platforms

* Alpine Linux 3.10, 3.11
* Amazonlinux 2
* Archlinux
* CentOS 7, 8
* Debian 10
* Fedora 31
* Ubuntu 18.04

## Requirements

Ansible 2.9 or higher is recommended.

## Variables

Variables and defaults for this role:

| variable | default value in defaults/main.yml | description |
| -------- | ---------------------------------- | ----------- |
| postgresql_enabled | False | determine whether role is enabled (True) or not (False) |

## Dependencies

None.

## Example Playbook

```yaml
---
# role: ansible-role-postgresql
# file: site.yml

- hosts: postgresql_systems
  become: True
  vars:
    postgresql_enabled: True
  roles:
    - role: ansible-role-postgresql
```

## License and Author

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.

## References

[ArchWiki](https://wiki.archlinux.org/)
