def checkered_board():
    C = int(input("Please enter the number of columns: "))
    R = int(input("Please enter the number of rows: "))
    check1 = "⬜⬛"
    check2 = "⬛⬜"
    if R % 2 == 0:
        for i in range(R//2):
            if C % 2 == 0:
                print((C//2) * check1)
                print((C//2) * check2)
            elif C % 2 != 0:
                print((C//2) * check1 + "⬜")
                print((C//2) * check2 + "⬛")

    if R % 2 != 0 and C % 2 == 0:
        x = 0
        while x != R:
            if x % 2 == 0:
                print((C//2) * check1)
            elif x % 2 != 0:
                print((C//2) * check2)
            x += 1
    
    if R % 2 != 0 and C % 2 != 0:
        x = 0
        while x != R:
            if x % 2 == 0:
                print((C//2) * check1 + "⬜")
            elif x % 2 != 0:
                print((C//2) * check2 + "⬛")
            x += 1

checkered_board()