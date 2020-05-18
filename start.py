
def allocate_machines(machines, required_capacity):
    filtered_machines = []
    for machine in machines:
        machine_name, capacity, cost_per_hr = machine
        # Filter out if cost_per_hr is not available
        if cost_per_hr == None:
            continue
        cost_per_unit = cost_per_hr / capacity
        filtered_machines.append(
            (machine_name, capacity, cost_per_hr, cost_per_unit)
        )

    # Sort filtered machines based on cost_per_unit
    machine_priorities = sorted(filtered_machines, key=lambda x: x[3])

    allocated_machines = []
    for machine in machine_priorities:
        machine_name, capacity, cost_per_hr, _ = machine
        reqd_no_of_machines = required_capacity // capacity
        if reqd_no_of_machines == 0:
            continue
        required_capacity %= capacity
        allocated_machines.append(
            (machine_name, reqd_no_of_machines, cost_per_hr)
        )
    return allocated_machines

if __name__ == '__main__':

    region_to_machines_map = {
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
            ('Large', 10, 120),
            ('XLarge', 20, 230),
            ('2XLarge', 40, 450),
            ('4XLarge', 80, 774),
            ('8XLarge', 160, 1400),
            ('10XLarge', 320, 2820)
        ],
        'China': [
            ('Large', 10, 120),
            ('XLarge', 20, 230),
            ('2XLarge', 40, 450),
            ('4XLarge', 80, 774),
            ('8XLarge', 160, 1400),
            ('10XLarge', 320, 2820)
        ]
    }

    required_capacity, total_hrs = (1150, 1)
    print('Capacity:    {}'.format(required_capacity))
    print('Hours:       {}'.format(total_hrs))

    result = []

    for region, all_machines in region_to_machines_map.items():
        allocated_machines = allocate_machines(all_machines, required_capacity)
        result.append({
            'region': region,
            'machines': allocated_machines,
            'total_cost': '$'
        })

    print(result)
