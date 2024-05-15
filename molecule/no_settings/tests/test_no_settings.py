"""Module containing the tests for the no_settings scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "service",
    [
        "configure-transparent-hugepage-settings",
    ],
)
def test_no_configure_thp_service(host, service):
    """Test that no services were created."""
    svc = host.service(service)
    # TODO: We cannot use this test because of pytest-dev/pytest-testinfra#757,
    # which would be resolved with the merge of pytest-dev/pytest-testinfra#754.
    # Once that pull request has been merged and a new release is cut we can use
    # the following test instead of the workaround being used below. Please see
    # #5 for details and tracking.
    # assert svc.exists is False, f"The {service} service exists"
    load_state = svc.systemd_properties["LoadState"]
    assert load_state == "not-found", f"The {service} service exists"
