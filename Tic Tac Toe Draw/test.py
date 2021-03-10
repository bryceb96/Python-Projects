test = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

[print(i) for i in test]
test[0][1] = 5
test[1][0] = 6
print("\n")
[print(i) for i in test]