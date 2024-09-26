def starPrin2(x):
    # print("Enter the function")
    # for i in range(1,x,1):
    #     print(" ",end="")
    #     for j in  range(x-1,i,-1):
    #         # print(j)
    #         print(" ",end="")
    #     for k in range(1,i+1,1):
    #         print("*",end="")
    #     print("")

    for i in range(1,x+1,1):
        # print("-",end="")
        for j in range(x,i,-1):
            print("-",end="")
        for k in range (1, i+1, 1):
            print("*",end="")

        print("")
        
        
starPrin2(5)




    
