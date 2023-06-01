array_3rd=[[['*' for _  in range (6)] for _ in range(4) ] for _ in range(3)]

for i in range(3):
    for j in range(4):
        for k in range(6):
            print(array_3rd[i][j][k], end=' ')
        print()
    print()

