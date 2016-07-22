def test_unbound_config(Command, Sudo):
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


def test_unbound_conf_d(File, Ansible):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'OpenBSD':
        assert 'include: "/var/unbound/etc/unbound.conf.d/*.conf"' in File(
                '/var/unbound/etc/unbound.conf').content_string
        assert File('/var/unbound/etc/unbound.conf.d').is_directory
    elif ansible_os_family == 'Debian':
        assert 'include: "/etc/unbound/unbound.conf.d/*.conf"' in File(
                '/etc/unbound/unbound.conf').content_string
        assert File('/etc/unbound/unbound.conf.d').is_directory


def test_unbound_trust_anchor(Ansible, File):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'OpenBSD':
        assert File('/var/unbound/etc/root.key').exists
    elif ansible_os_family == 'Debian':
        assert File('/etc/unbound/root.key').exists


def test_unbound_user(Ansible, User, File):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'OpenBSD':
        assert User('_unbound').exists
        assert File('/etc/mail/aliases').contains('_unbound: root')
    elif ansible_os_family == 'Debian':
        assert User('unbound').exists
        assert File('/etc/aliases').contains('unbound: root')
