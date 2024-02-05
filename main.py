import random

#題目
ans = random.sample([0,1,2,3,4,5,6,7,8,9], k=4)
#print(ans)
a,b = (0,0)
n = 0


while a != 4:
    #玩家猜題
    guess = list(input("請輸入四位數:"))
    a,b = (0,0)
    n = 0
    for i in guess:
        if int(guess[n]) == ans[n]:
            a += 1
        else:
            if int(i) in ans:
                b += 1
        n += 1
    print(a,"A",b,"B")
    
print("賓果!!!")