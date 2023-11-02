#input a 10~20 odd
n=int(input('請輸入一個正整數:'))
while not(n>=10 and n<=20 and n%2!=0):
    n=int(input('請重新輸入一個正整數:'))
mid=n//2+1
#x坐標軸
print(' '*4,end='')

for i in range(1,n+1):
    print('%4d'%i,end='')
print()
for col in range(1,n+1):
    print('%4d'%col,end='')#劃y座標
    for row in range(1,n+1):
        if (row//2+1==col) or ((n-row)//2+1==col and row!=mid):
            print(' '*4,end='')
        else:
            print('%4d'%1,end='')
    print()