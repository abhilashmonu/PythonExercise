 # find the second largest number in a list
list1 = []
try:
    num1 = int(input("Enter the number of elements in a list: "))
    if num1 == 1:
        print("Minimum length of list should be 2 \n")
        quit()
    else:
        for i in range(num1):
            try:
                data = int(input("Enter element:"))
                list1.append(data)
                list1.sort()
            except ValueError:
                print("The entered value is not of type int \n ")
                quit()
        print("Second largest element is:", list1[-2])
except ValueError:
    print("The entered value is not of type int \n ")

# swap the first and last value of a list
list2 = []
try:
    num2 = int(input("Enter the number of elements in a list: "))
    for i in range(num2):
        try:
            data = int(input("Enter element:"))
            list2.append(data)
        except ValueError:
            print("The entered value is not of type int \n")
            quit()
    print("First number is:",list2[0])
    print("Last number is:", list2[-1])
    temp = list2[0]
    list2[0] = list2[-1]
    list2[-1] = temp
    print("After swap, First number is:",list2[0])
    print("After swap, Last number is:", list2[-1])
except ValueError:
    print("The entered value is not of type int \n")

# remove the duplicate items from the list
list3 = []
try:
    num3 = int(input("Enter the number of elements in a list: "))
    for i in range(num3):
        try:
            data = int(input("Enter element:"))
            list3.append(data)
        except ValueError:
            print("The entered value is not of type int \n")
            quit()
    print(list3)
    list3 = set(list3)
    print("After removing duplicates:",list(list3))
except ValueError:
    print("The entered value is not of type int \n")

# read a list of words and return the length of the longest one
list4=[]
try:
    num4= int(input("Enter the length of the list:"))
    for i in range(num4):
        try:
            data = str(input("Enter element:"))
            list4.append(data)
            length=len(list4[0])
            temp=list4[0]
        except ValueError:
            print("The entered value is not of type string \n")
            quit()
    print("The list is:", list4)
    for j in list4:
        if(len(j)>length):
            length=len(j)
            temp=j
    print("The word with the longest length is:", temp)
except ValueError:
    print("The entered value is not of type int \n ")
