def palindromi(mjono) -> str:
    return mjono[:: -1] == mjono

while True: 
    sana = input("Anna palindromi: ")
    if palindromi(sana): 
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")