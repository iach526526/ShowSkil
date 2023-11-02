n=int(input('請輸入一個正整數:'))
while not(n>=10 and n<=20 and n%2!=0):
    n=int(input('請重新輸入一個正整數:'))
#輸出第一個橫排(好看的)
print('    ',end='')
for i  in range(1,n+1):
    print('%4d'%i,end='')
print()
mid=n//2+1
for col in range(1,n+1):#一橫排
    print('%4d'%col,end='')
    for row in range(1,n+1):#橫的每個元素
        if row+col<=mid or (col+row<=n and col>mid) or (row>mid and row-col>mid-1) or (row>mid and col>mid and row-col>0):#(左上) or (左下) or (右上) or 左下
            print(' '*4,end='')
        else:
            print('%4d'%(row*col),end='')
    print()