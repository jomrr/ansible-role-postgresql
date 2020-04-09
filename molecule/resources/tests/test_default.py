import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# the pytest way
@pytest.mark.parametrize("name", [
    ("postgresql"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_service(host):
    # just for demonstration
    if host.system_info.distribution == 'redhat':
        daemon = 'postgresql'
    else:
        daemon = 'postgresql'
    assert host.service(daemon).is_enabled
    assert host.service(daemon).is_running
