from main import parse_input, allocate_machines, allocate_machines_regionally, REGION_TO_MACHINES_MAP
import pytest

@pytest.mark.parametrize("input_string,expected_output", [
    ('Capacity of 1150 units for 1 Hour', (1150, 1)),
    ('230 units for 5 Hours', (230, 5)),
    ('100 units for 24 Hours', (100, 24)),
    ('1100 units for 12 Hours', (1100, 12))
])
def test_parse_input(input_string, expected_output):
    assert parse_input(input_string) == expected_output

@pytest.mark.parametrize("country,allocated_machines", [
    ('New York', [('8XLarge', 7, 1400), ('XLarge', 1, 230), ('Large', 1, 120)]),
    ('India', [('8XLarge', 7, 1300), ('Large', 3, 140)]),
    ('China', [('8XLarge', 7, 1180), ('XLarge', 1, 200), ('Large', 1, 110)])
])
def test_allocate_machines_regionally(country, allocated_machines):
    assert allocate_machines_regionally(
        REGION_TO_MACHINES_MAP[country], 1150
    ) == allocated_machines


def test_allocate_machines():
    assert allocate_machines(1150, 1) == {
        "Output": [
            {
                "region": "New York",
                "machines": [
                    ("8XLarge", 7),
                    ("XLarge", 1),
                    ("Large", 1)
                ],
                "total_cost": "$10150"
            },
            {
                "region": "India",
                "machines": [
                    ("8XLarge", 7),
                    ("Large", 3)
                ],
                "total_cost": "$9520"
            },
            {
                "region": "China",
                "machines": [
                    ("8XLarge", 7),
                    ("XLarge", 1),
                    ("Large", 1)
                ],
                "total_cost": "$8570"
            }
        ]
    }
