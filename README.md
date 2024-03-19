# ansible-role-manage-thp #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-manage-thp/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-manage-thp/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-manage-thp/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-manage-thp/actions/workflows/codeql-analysis.yml)

An Ansible role to manage Transparent HugePages (THP) on Linux systems. This
role is inspired by the [GekoCloud/ansible-role-disable-thp](https://github.com/GekoCloud/ansible-role-disable-thp)
role.

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| manage\_thp\_defrag\_path | The sysfs path to control the `defrag` setting for transparent hugepages. | `/sys/kernel/mm/transparent_hugepage/defrag` | No |
| manage\_thp\_defrag\_setting | If defined it must be a value of `always`, `defer`, `defer+madvise`, `madvise`, or `never`. Please see the [kernel documentation] for more information. | n/a | No |
| manage\_thp\_enabled\_path | The sysfs path to control the `enabled` setting for transparent hugepages. | `/sys/kernel/mm/transparent_hugepage/enabled` | No |
| manage\_thp\_enabled\_setting | A value of `always`, `madvise`, or `never`. Please see the [kernel documentation] for more information. | n/a | Yes |
| manage\_thp\_service\_name | The name of the SystemD service that is created to manage transparent hugepage settings. Please note that `.service` is appended to this value in the name of the unit file created. | `configure-transparent-hugepages` | No |

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Manage transparent hugepages
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
