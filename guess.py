import random

low, high = 1, 100
ans = random.randint(low + 1, high - 1)
while True:
    print("請輸入", low, "-", high, ":")
    guess = int(input())

    if guess < low or guess > high:
        print("invalid input")

    else:
        if guess > ans:
            print("too big")
            high = guess
        elif guess < ans:
            print("too small")
            low = guess
        else:
            print("guess right!!!")
            break
