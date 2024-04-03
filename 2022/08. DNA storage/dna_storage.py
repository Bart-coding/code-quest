def dna_storage(input: str) -> str:
    input_lines = input.splitlines()
    num_of_test_cases = int(input_lines[0])
    output = []
    for line in input_lines[1 : num_of_test_cases + 1]:
        i = 0
        while i < len(line):
            encrypted_letter = []
            for j in range(i, i + 7):
                if line[j] == "A" or line[j] == "T":
                    encrypted_letter.append("0")
                else:
                    encrypted_letter.append("1")
            encrypted_letter = "".join(encrypted_letter)
            decrypted_letter = chr(int(encrypted_letter, 2))
            output.append(decrypted_letter)
            i = i + 7
        output.append('\n')
    return "".join(output)[:-1]

#print(dna_storage("3\nGACGTTCGGAGCCCGGCTGACACTAGCGGGCAAGAGGATCACACTTTAAGGCATCTCCAGTACCGAAGGGCCTGATTCCCACAT\nCTAGTATCCTTGTGGGTGGATCGTCGTACCTGGCGAGTATTAGCGTCGCGCAGGCCCCCATGAGGTGCTTGCTAGAA\nCTTTAACGCAGGTCGGTTTACGGGGTCTCCACTAGGGTGCCTGCTACGCTGTTTTC"))