def rot13(input: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    for letter in input:
        index = (alphabet.find(letter) + 13) % 26
        output = output + alphabet[index]
    
    return output

if __name__ == "__main__":
    print(rot13("SIMSALABIM"))
