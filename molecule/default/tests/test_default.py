"""Module containing the tests for the default scenario."""

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
        "configure-transparent-hugepages",
    ],
)
def test_configure_thp_service(host, service):
    """Test that any services created are enabled."""
    svc = host.service(service)
    assert svc.is_enabled, f"The {service} service is not enabled"
