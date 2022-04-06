# Tee ratkaisu tänne
def anagrammi(mjono1 : str, mjono2 : str):
    mjono1 = sorted(mjono1) 
    mjono2 = sorted(mjono2)
    return mjono1 == mjono2

if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False