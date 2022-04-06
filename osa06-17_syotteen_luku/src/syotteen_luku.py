# tee ratkaisu tänne
def lue(lause: str, mista: int, mihin: int):
    while True:
        try:
            syote = int(input(f"{lause}"))
            if syote >=mista and syote <= mihin:
                return syote
        except ValueError:
            pass
        print(f"Syötteen on oltava kokonaisluku väliltä {mista}...{mihin}")
if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)