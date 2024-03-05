def nullCipher(decryptedText: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    encryptedText = ""
    i = 1
    while i < len(decryptedText):
        if decryptedText[i-1] in vowels:
            encryptedText += decryptedText[i]
            i += 1
        i += 1
    return encryptedText