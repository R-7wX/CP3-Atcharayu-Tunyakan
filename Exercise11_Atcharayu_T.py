Number = int(input())
for i in range(Number):
    Spaces = " " * (Number - i - 1)
    Texts = "*" * (2*i + 1)
    print(Spaces + Texts + Spaces)
