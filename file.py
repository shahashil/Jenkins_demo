print("Calculator")
try:
    n = int(input())
    print(n * 10)
    print("Addition is ",n)
except EOFError as e:
    print(e)


