# (batch_name, units_per_batch, cost_per_hr_per_batch)
all_machines = [
    ('Large', 10, 120),
    ('XLarge', 20, 230),
    ('2XLarge', 40, 450),
    ('4XLarge', 80, 774),
    ('8XLarge', 160, 1400),
    ('10XLarge', 320, 2820)
]

capacity, total_hrs = (1150, 1)

print('Capacity:    {}'.format(capacity))
print('Hours:       {}'.format(total_hrs))

# (batch_name, units_per_batch, cost_per_hr_per_batch, cost_per_hr_per_unit)
filtered_machines = []
for machine in all_machines:
    _, units_per_batch, cost_per_hr_per_batch = machine
    if cost_per_hr_per_batch == None:
        continue
    cost_per_hr_per_unit = cost_per_hr_per_batch / units_per_batch
    filtered_machines.append(
        (*machine, cost_per_hr_per_unit)
    )

# (batch_name, units_per_batch, cost_per_hr_per_batch, cost_per_hr_per_unit)
machine_priorities = []
# Sort filtered machines on cost_per_hr_per_unit
machine_priorities = sorted(filtered_machines, key=lambda x: x[3])
print(machine_priorities)

# (batch_name, units_per_batch, cost_per_hr_per_batch, cost_per_hr_per_unit, no_of_machines_required)
used_machines = []
_capacity = capacity
for machine in machine_priorities:
    no_of_machines_required = _capacity // machine[1]
    if no_of_machines_required == 0:
        continue
    _capacity %= machine[1]
    used_machines.append(
        (*machine, no_of_machines_required)
    )
print(used_machines)
