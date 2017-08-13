import random

a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
end=False
c=[1]
elbut=0
k=1
bal=0
ad=[]
while end!=True:
    zeros=0
    for i in a:
        zeros+=i.count(0)
    k=1
    b=[]
    if zeros!=0:
        k=0
        if elbut==0:
            for i in range(4):
                for j in range(4):
                    if a[i][j]==0:
                        b.append([i,j])
            d=random.randrange(len(b))
            if random.random()>0.0909090909:
                a[b[d][0]][b[d][1]]=2
            else:
                a[b[d][0]][b[d][1]]=4
    ad=[]
    for i in a:
        ad.append(i)
    zeros=0
    for i in a:
        zeros+=i.count(0)
        k=1
    if zeros==0:
        k=0
        for i in range(4):
            for j in range(4):
                if i==0 and j==0:
                    if a[i][j]==a[i+1][j] or a[i][j]==a[i][j+1]:
                        k+=1
                elif i==0 and j==3:
                    if a[i][j]==a[i+1][j] or a[i][j]==a[i][j-1]:
                        k+=1
                elif i==3 and j==0:
                    if a[i][j]==a[i-1][j] or a[i][j]==a[i][j+1]:
                        k+=1
                elif i==3 and j==3:
                    if a[i][j]==a[i-1][j] or a[i][j]==a[i][j-1]:
                        k+=1
                elif i==0:
                    if a[i][j]==a[i+1][j] or a[i][j]==a[i][j-1] or a[i][j]==a[i][j+1]:
                        k+=1
                elif j==0:
                    if a[i][j]==a[i+1][j] or a[i][j]==a[i-1][j] or a[i][j]==a[i][j+1]:
                        k+=1
                elif i==3:
                    if a[i][j]==a[i-1][j] or a[i][j]==a[i][j-1] or a[i][j]==a[i][j+1]:
                        k+=1
                elif j==3:
                    if a[i][j]==a[i-1][j] or a[i][j]==a[i][j-1] or a[i][j]==a[i+1][j]:
                        k+=1
                else:
                    if a[i][j]==a[i-1][j] or a[i][j]==a[i][j-1] or a[i][j]==a[i+1][j] or a[i][j]==a[i+1][j+1]:
                        k+=1
    if k==0:
        print('Кол-во очков:',bal)
        for i in range(4):
            for j in range(4):
                print(a[i][j],end='   ')
            print('')
        print('Конец игры')
        break
    elbut=0
    print('Кол-во очков:',bal)
    for i in range(4):
        for j in range(4):
            print(a[i][j],end='   ')
        print('')
    button=input()
    dva=[]
    flag=0
    if button=='w':
        for l in range(3):
            for i in range(3):
                for j in range(4):
                    if(a[i][j]==0):
                        if a[i+1][j]!=0:
                            flag+=1
                        a[i][j]+=a[i+1][j]
                        a[i+1][j]=0
        for i in range(3):
            for j in range(4):
                if(a[i][j]==a[i+1][j]!=0)and(dva.count([i,j])==0):
                    a[i][j]+=a[i+1][j]
                    bal+=a[i][j]
                    a[i+1][j]=0
                    dva.append([i,j])
                    flag+=1
        for i in range(3):
            for j in range(4):
                if(a[i][j]==0):
                    if a[i+1][j]!=0:
                            flag+=1
                    a[i][j]+=a[i+1][j]
                    a[i+1][j]=0
    elif button=='s':
        a.reverse()
        for i in a:
            i.reverse()
        for l in range(3):
            for i in range(3):
                for j in range(4):
                    if(a[i][j]==0):
                        if a[i+1][j]!=0:
                            flag+=1
                        a[i][j]+=a[i+1][j]
                        a[i+1][j]=0
        for i in range(3):
            for j in range(4):
                if(a[i][j]==a[i+1][j]!=0)and(dva.count([i,j])==0):
                    a[i][j]+=a[i+1][j]
                    bal+=a[i][j]
                    a[i+1][j]=0
                    dva.append([i,j])
                    flag+=1
        for i in range(3):
            for j in range(4):
                if(a[i][j]==0):
                    if a[i+1][j]!=0:
                            flag+=1
                    a[i][j]+=a[i+1][j]
                    a[i+1][j]=0
        a.reverse()
        for i in a:
            i.reverse()
    elif button=='d':
        a.reverse()
        for i in a:
            i.reverse()
        for l in range(3):
            for j in range(3):
                for i in range(4):
                    if(a[i][j]==0):
                        if a[i][j+1]!=0:
                            flag+=1
                        a[i][j]+=a[i][j+1]
                        a[i][j+1]=0
        for j in range(3):
            for i in range(4):
                if(a[i][j]==a[i][j+1]!=0)and(dva.count([i,j])==0):
                    a[i][j]+=a[i][j+1]
                    bal+=a[i][j]
                    a[i][j+1]=0
                    dva.append([i,j])
                    flag+=1
        for j in range(3):
                for i in range(4):
                    if(a[i][j]==0):
                        if a[i][j+1]!=0:
                            flag+=1
                        a[i][j]+=a[i][j+1]
                        a[i][j+1]=0
        a.reverse()
        for i in a:
            i.reverse()
    elif button=='a':
        for l in range(3):
            for j in range(3):
                for i in range(4):
                    if(a[i][j]==0):
                        if a[i][j+1]!=0:
                            flag+=1
                        a[i][j]+=a[i][j+1]
                        a[i][j+1]=0
        for j in range(3):
            for i in range(4):
                if(a[i][j]==a[i][j+1]!=0)and(dva.count([i,j])==0):
                    a[i][j]+=a[i][j+1]
                    bal+=a[i][j]
                    a[i][j+1]=0
                    dva.append([i,j])
                    flag+=1
        for j in range(3):
                for i in range(4):
                    if(a[i][j]==0):
                        if a[i][j+1]!=0:
                            flag+=1
                        a[i][j]+=a[i][j+1]
                        a[i][j+1]=0
    else:
        elbut=1
    if flag==0:
        elbut=1
