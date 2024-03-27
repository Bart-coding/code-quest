import math
def power_to_persevere(input: str) -> str:
    output = ''
    for line in input.splitlines()[1:]:
        wheel_diam, revols_to_rotate, power_to_revol, rpm, power_sys_capacity, voltage, distance = map(int, line.split(' '))
        rotate_time = revols_to_rotate / rpm #min
        power_to_rotate = revols_to_rotate * power_to_revol #W
        wheel_perimeter = (math.pi * wheel_diam) / 100 #m
        num_of_rotations = distance / wheel_perimeter
        req_time = rotate_time * num_of_rotations #min
        req_power = power_to_rotate * num_of_rotations #W
        req_energy = (req_power / voltage) * (req_time / 60) #Ah
        if req_energy <= power_sys_capacity:
            output += "Success " + str(round(req_time, 4)) + '\n'
        else:
            output += "Fail" + '\n'
    return output[:-1]

#print(power_to_persevere("2\n15 6 6 10 4 12 5\n12 8 12 10 24 12 8"))