from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_unbound_config(Command, Sudo):
    with Sudo():
        assert Command('unbound-checkconf').rc == 0


def test_unbound_service(Service):
    service = Service('unbound')
    assert service.is_running
    try:
        assert service.is_enabled
    except NotImplementedError:
        pass


def test_unbound_socket(Socket):
    assert Socket('udp://127.0.0.1:53').is_listening


def test_unbound_conf_d(File, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert 'include: "/var/unbound/etc/unbound.conf.d/*.conf"' in File(
                '/var/unbound/etc/unbound.conf').content_string
        assert File('/var/unbound/etc/unbound.conf.d').is_directory
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert 'include: "/etc/unbound/unbound.conf.d/*.conf"' in File(
                '/etc/unbound/unbound.conf').content_string
        assert File('/etc/unbound/unbound.conf.d').is_directory


def test_unbound_trust_anchor(SystemInfo, File):
    if SystemInfo.type == 'openbsd':
        assert File('/var/unbound/etc/root.key').exists
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert File('/etc/unbound/root.key').exists


def test_unbound_user(SystemInfo, User, File):
    if SystemInfo.type == 'openbsd':
        assert User('_unbound').exists
        assert File('/etc/mail/aliases').contains('_unbound: root')
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert User('unbound').exists
        assert File('/etc/aliases').contains('unbound: root')
