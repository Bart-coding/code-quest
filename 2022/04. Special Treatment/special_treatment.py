def special_treatment(input: str) -> str:
    output_lines = ''
    for line in input.splitlines()[1:]:
        output_lines += ''.join(char for char in line if char.isalnum() or char.isspace()) + '\n'
    return output_lines[:-1]

#print(special_treatment("3\nThis “is” amazing!\nCan’t you - yes, you - remove all the special characters?\nAnything /not/ a letter, numb3r, or _space_ should go."))