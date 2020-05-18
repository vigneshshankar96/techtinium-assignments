import json

REGION_TO_MACHINES_MAP = {
    # (machine_name, capacity, cost_per_hr)
    'New York': [
        ('Large', 10, 120),
        ('XLarge', 20, 230),
        ('2XLarge', 40, 450),
        ('4XLarge', 80, 774),
        ('8XLarge', 160, 1400),
        ('10XLarge', 320, 2820)
    ],
    'India': [
        ('Large', 10, 140),
        # ('XLarge', 20, None),
        ('2XLarge', 40, 413),
        ('4XLarge', 80, 890),
        ('8XLarge', 160, 1300),
        ('10XLarge', 320, 2970)
    ],
    'China': [
        ('Large', 10, 110),
        ('XLarge', 20, 200),
        # ('2XLarge', 40, None),
        ('4XLarge', 80, 670),
        ('8XLarge', 160, 1180),
        # ('10XLarge', 320, None)
    ]
}

class Machine():
    def __init__(self, name, capacity, cost_per_hr=None):
        self.name = name
        self.capacity = capacity
        self.cost_per_hr = cost_per_hr
        self.cost_per_unit = None

        if self.cost_per_hr is not None:
            self.cost_per_unit = self.cost_per_hr / self.capacity


def allocate_machines(machines, required_capacity):
    filtered_machines = []
    for spec_tuple in machines:
        _machine = Machine(*spec_tuple)

        # Only append machines that have cost_per_hr specified
        if _machine.cost_per_hr:
            filtered_machines.append(_machine)

    # Prioritise machines with least cost_per_unit
    machine_priorities = sorted(
        filtered_machines,
        key=lambda machine: machine.cost_per_unit
    )

    allocated_machines = []
    for machine in machine_priorities:
        reqd_no_of_machines = required_capacity // machine.capacity
        if reqd_no_of_machines <= 0:
            continue
        # Subtract maximum counts of machine capacity possible
        required_capacity %= machine.capacity
        allocated_machines.append(
            (machine.name, reqd_no_of_machines, machine.cost_per_hr)
        )
    return allocated_machines

def main(required_capacity, total_hrs):
    results = {
        'Output': []
    }

    for region, all_machines in REGION_TO_MACHINES_MAP.items():
        result = {}
        result['region'] = region
        result['machines'] = []

        total_cost = 0
        for (
            machine_name, reqd_no_of_machines, run_cost_per_hr
        ) in allocate_machines(all_machines, required_capacity):
            result['machines'].append((machine_name, reqd_no_of_machines))
            total_cost += (reqd_no_of_machines * run_cost_per_hr * total_hrs)

        result['total_cost'] = '${}'.format(total_cost)
        results['Output'].append(result)

    return results


if __name__ == '__main__':

    required_capacity, total_hrs = (1150, 1)
    print('Capacity:    {}'.format(required_capacity))
    print('Hours:       {}'.format(total_hrs))

    results = main(required_capacity, total_hrs)

    print(json.dumps(results, indent=4))
