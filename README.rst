Unbound
#######

Provision the Unbound DNS resolver.

Requirements
------------

See :code:`meta/main.yml` and assertions at top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.

TODO
----

- Download DNS root hints, DNSSEC anchor.
- Update DNSSEC root anchor weekly.
- Alias email to root.
- Create, use conf.d directory.
- Log to syslog.
- At the end flush handlers and wait for service to start.
- Use dhparams.
- Assertions.
- Tests.
