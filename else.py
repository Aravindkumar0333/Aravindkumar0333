i=1
while(i<=10):
    print(i)
    i+=1
else:
    print("loop completed")
    print("_____________________________")
    for j in range(1,15):
        if(j==4):
            continue
        print(j)
    else:
        print("For loop completed")