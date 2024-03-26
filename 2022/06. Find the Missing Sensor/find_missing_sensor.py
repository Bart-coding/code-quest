def find_missing_sensor(input: str) -> str:
    input_lines = input.splitlines()
    output = ''
    for i in range(1, len(input_lines), 2):
        num_of_sensors = int(input_lines[i])
        sensors_list = input_lines[i+1].split(' ')
        expected_sum = (1 + num_of_sensors) * (num_of_sensors / 2)
        list_sum = sum(map(int, sensors_list))
        missing_sensor = int(expected_sum - list_sum)
        output += str(missing_sensor) + '\n'
    return output[:-1]

#print(find_missing_sensor("2\n9\n5 7 3 2 8 1 4 9\n10\n7 4 1 10 8 2 9 6 3"))