import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_vagrant_user(host):
    h = host.user('vagrant')

    assert h.uid == 1000
    assert h.gid == 1000
    assert h.group == 'vagrant'
    assert 'sudo' in h.groups
    assert 'adm' in h.groups
    assert 'vagrant' in h.groups
    assert h.home == '/home/vagrant'
    assert h.shell == '/bin/bash'
