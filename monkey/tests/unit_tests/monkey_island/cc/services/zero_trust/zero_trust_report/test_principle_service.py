import pytest
from tests.unit_tests.monkey_island.cc.services.zero_trust.test_common.finding_data import (
    get_monkey_finding_dto,
)

from common.common_consts import zero_trust_consts
from monkey_island.cc.services.zero_trust.zero_trust_report.principle_service import (
    PrincipleService,
)

EXPECTED_DICT = {
    "test_pillar1": [
        {
            "principle": "Test principle description2",
            "status": zero_trust_consts.STATUS_PASSED,
            "tests": [
                {"status": zero_trust_consts.STATUS_PASSED, "test": "You ran a test2"},
            ],
        }
    ],
    "test_pillar2": [
        {
            "principle": "Test principle description",
            "status": zero_trust_consts.STATUS_PASSED,
            "tests": [{"status": zero_trust_consts.STATUS_PASSED, "test": "You ran a test1"}],
        },
        {
            "principle": "Test principle description2",
            "status": zero_trust_consts.STATUS_PASSED,
            "tests": [
                {"status": zero_trust_consts.STATUS_PASSED, "test": "You ran a test2"},
            ],
        },
    ],
}


@pytest.mark.usefixtures("uses_database")
def test_get_principles_status():
    TEST_PILLAR1 = "test_pillar1"
    TEST_PILLAR2 = "test_pillar2"
    zero_trust_consts.PILLARS = (TEST_PILLAR1, TEST_PILLAR2)

    principles_to_tests = {
        "network_policies": ["segmentation"],
        "endpoint_security": ["tunneling"],
    }
    zero_trust_consts.PRINCIPLES_TO_TESTS = principles_to_tests

    principles_to_pillars = {
        "network_policies": {"test_pillar2"},
        "endpoint_security": {"test_pillar1", "test_pillar2"},
    }
    zero_trust_consts.PRINCIPLES_TO_PILLARS = principles_to_pillars

    principles = {
        "network_policies": "Test principle description",
        "endpoint_security": "Test principle description2",
    }
    zero_trust_consts.PRINCIPLES = principles

    tests_map = {
        "segmentation": {"explanation": "You ran a test1"},
        "tunneling": {"explanation": "You ran a test2"},
    }
    zero_trust_consts.TESTS_MAP = tests_map

    monkey_finding = get_monkey_finding_dto()
    monkey_finding.test = "segmentation"
    monkey_finding.save()

    monkey_finding = get_monkey_finding_dto()
    monkey_finding.test = "tunneling"
    monkey_finding.save()

    expected = dict(EXPECTED_DICT)  # new mutable

    result = PrincipleService.get_principles_status()

    assert result == expected
