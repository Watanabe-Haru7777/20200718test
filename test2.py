print("整数を入力してください")

vx=int(input("整数:"))

i=0

if (vx%2==0):
    while i<=100:
        print(i)
        i+=2

print("偶数だけを出しました")

print("奇数も出しましょう")
i=1

if (vx%2==0):
    while i<=100:
        print(i)
        i+=2