Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: boss-ansible-role-users, x: 42 }

License
-------

Apache

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

Influence
-------------------
https://github.com/singleplatform-eng/ansible-users/tree/master/tasks

THIS IS FOR LEARNING PURPOSES ONLY!!!!

Example:

    ---
    users:
      - username: foo
        name: Foo Barrington
        groups: ['wheel','systemd-journal']
        uid: 1001
        home: /local/home/foo
        profile: |
          alias ll='ls -lah'
        ssh_key:
          - "ssh-rsa AAAAA.... foo@machine"
          - "ssh-rsa AAAAB.... foo2@machine"
    groups_to_create:
      - name: developers
        gid: 10000
    users_deleted:
      - username: bar
        name: Bar User
        uid: 1002

## Deleting users

The `users_deleted` variable contains a list of users who should no longer be
in the system, and these will be removed on the next ansible run. The format
is the same as for users to add, but the only required field is `username`.
However, it is recommended that you also keep the `uid` field for reference so
that numeric user ids are not accidentally reused.

You can optionally choose to remove the user's home directory and mail spool with
the `remove` parameter, and force removal of files with the `force` parameter.

    users_deleted:
      - username: bar
        uid: 1002
        remove: yes
        force: yes
