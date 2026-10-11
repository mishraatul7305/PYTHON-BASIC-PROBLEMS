## problem 1-------------------------------
#break=====================
for i in range (10) :
    if i ==5:
        break
    print(i)  
##problem 2== continue========================
for i in range (5):
    if i == 3:
        continue
    print(i) 
    # problem 3========================
    # find the  check whether a number is even or odd
    num= int(input("enter a number :"))
    if num % 2== 0:
        print ("even")
    else:
        print ("odd") 
        #problem 4========================
        ##largest of three numbers
        a,b,c=5,12,9
        largest=a
        if b>largest:
            largest=b
            if c>largest:
                largest=c
                print("largest:",largest) 
                #problem 5========================
## print number from 1 to 10
for i in range (1,11):
    print(i) 
    #problem 6======================== 
    #print output in Python-------
    print("hello word!") 
    print("name:", name ,sep=" ", end="\n")
    #problem 7==========================
    #casting ======================================
    x ="28"
    y =int(x) 
    z =float(y)
    print (z)
#problem 8 ===============================
#dictionary==========================================
    person = {"name": "Atul", "age": 24} 
    print (person) 
#problem 9 ==========================
# break 
for i in range(10):
        if i == 5 :
            break 
        print (i)    
# problem 10 =======
#loop
for i in range (1,6) :

    print(i)