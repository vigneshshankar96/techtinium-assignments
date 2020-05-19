from main import allocate_machines

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
