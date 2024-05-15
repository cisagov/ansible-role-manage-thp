# ansible-role-manage-thp #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-manage-thp/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-manage-thp/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-manage-thp/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-manage-thp/actions/workflows/codeql-analysis.yml)

An Ansible role that creates a SystemD unit to manage Transparent HugePage (THP)
settings on Linux systems. This role is inspired by the
[GekoCloud/ansible-role-disable-thp](https://github.com/GekoCloud/ansible-role-disable-thp)
role.

## Requirements ##

None.

## Role Variables ##

> [!NOTE]
> Although none of the variables that control settings are individually required,
> at least one of them must be defined.

<!--
Note:
The order of any setting's valid values is intentionally _not_ enforced in alphabetical
order. They instead match the output of a `cat /path/to/setting` command on a live
system so that it is easier to cross-reference the setting values with what one would
see when configuring Transparent HugePage settings manually.
-->

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| manage\_thp\_defrag\_path | The sysfs path to control the Transparent HugePage `defrag` setting. | `/sys/kernel/mm/transparent_hugepage/defrag` | No |
| manage\_thp\_defrag\_setting | If defined this variable must be given a value of `always`, `defer`, `defer+madvise`, `madvise`, or `never`. Please see the [kernel documentation] for more information. | n/a | No |
| manage\_thp\_enabled\_path | The sysfs path to control the Transparent HugePage `enabled` setting. | `/sys/kernel/mm/transparent_hugepage/enabled` | No |
| manage\_thp\_enabled\_setting | If defined this variable must be given a value of `always`, `madvise`, or `never`. Please see the [kernel documentation] for more information. | n/a | No |
| manage\_thp\_service\_name | The name of the SystemD service that is created to manage Transparent HugePage settings. Please note that `.service` is appended to this value in the name of the unit file created. | `configure-transparent-hugepage-settings` | No |
| manage\_thp\_shmem\_enabled\_path | The sysfs path to control the Transparent HugePage `shmem_enabled` setting. | `/sys/kernel/mm/transparent_hugepage/shmem_enabled` | No |
| manage\_thp\_shmem\_enabled\_setting | If defined this variable must be given a value of `always`, `within_size`, `advise`, `never`, `deny`, or `force`. Please see the [kernel documentation] for more information. | n/a | No |
| manage\_thp\_start\_before\_service | The name of the service that the SystemD unit file should be configured to start before. Please note that `.service` is appended to this value in the definition of the `Before` directive. | n/a | No |
| manage\_thp\_use\_zero\_page\_path | The sysfs path to control the Transparent HugePage `use_zero_page` setting. | `/sys/kernel/mm/transparent_hugepage/use_zero_page` | No |
| manage\_thp\_use\_zero\_page\_setting | If defined this variable must be given a value of `0` or `1`. Please see the [kernel documentation] for more information. | n/a | No |

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: manage_thp
  src: https://github.com/cisagov/ansible-role-manage-thp
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Manage Transparent HugePage settings
      ansible.builtin.include_role:
        name: manage_thp
      vars:
        manage_thp_enabled_setting: never
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Nicholas McDonnell - <nicholas.mcdonnell@gwe.cisa.dhs.gov>

[kernel documentation]: https://www.kernel.org/doc/html/next/admin-guide/mm/transhuge.html#global-thp-controls
