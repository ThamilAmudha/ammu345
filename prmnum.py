num=int(input("enter the number"))
end=int(input("enter the number"))
for num in range(num,end+1):
    if num>1:
                for x in range(2,num):
                                if(num%x)==0:
                                                break
                else:
                                print(num)
