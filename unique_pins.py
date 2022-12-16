first_border = int(input())
second_border = int(input())
third_border = int(input())

for digit1 in range(1, first_border + 1):
    for digit2 in range(2, second_border + 1):
        for digit3 in range(1, third_border + 1):
            if digit1 % 2 == 0 and (digit2 == 2 or digit2 == 3 or digit2 == 5 or digit2 == 7) and digit3 % 2 == 0:
                print(f"{digit1} {digit2} {digit3}")