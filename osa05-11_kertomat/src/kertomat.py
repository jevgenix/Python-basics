def kertomat(n: int):
    kertomat = {}; 
    s = 1
    for i in range(1,n + 1):
        s *= i
        kertomat[i] = s
    return kertomat

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])