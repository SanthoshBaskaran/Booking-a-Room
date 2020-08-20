import random
rooms=list(map(int,input().split()))
sold=[]
count=0
for i in range(int(rooms[-1])):
    room=int(input())
    sold.append(room)
j=0
difference=rooms[0]-rooms[1]
while(j==0):
    random1=random.randint(1,rooms[0])
    count=count+1
    if random1 not in sold:
        print(random1)
        break
    if(count==rooms[0]+1 or difference==0):
        print('too late')
        break
