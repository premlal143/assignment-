# 1) What is List? How will you reverse a list?
#ANS=>
'''
        Lists are used to store multiple items in a single variable.
        Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are
            Tuple, Set, and Dictionary, all with different qualities and usage.
            
        Reversing a list using the reversed() and reverse() built-in function. Using reversed() we can reverse the list and a 
        list_reverseiterator object is created, from which we can create a list using list() type casting.Or, we can also use list.
            reverse() function to reverse list in-place
'''


# 2) How will you remove last object from a list?
#   Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
#ANS=>

        l = [2,33,222,14,25]
        l.pop(-1)
        print(l)


# 3) Differentiate between append () and extend () methods?
#ANS=>
        '''
        --> The append() method in the Python programming language adds an item to a list that already exists whereas the 
            extend() method adds each of the iterable elements which is supplied as a parameter to the end of the original  
            list.
        '''


# 4) Write a Python function to get the largest number, smallest num and sum of all from a list.
#ANS=>
        list1 = [2,22,24,26,28]
        l=max(list1)
        print("enter the largest number =",l)
        m=min(list1)
        print("enter the smallest number =",m)
        n=sum(list1)
        print("sum of list",n)


# 5) How will you compare two lists?
#ANS=>
        list1 =[1,3,5,23,43]
        list2 =[2,4,8,26,52]
        if list1==list2:
            print("this list are equle")
        else:
            print("this list are not equle")



# 6) Write a Python program to count the number of strings where the string length is 2 or more and the 
#   first and last character are same from a given list of strings.
#ANS=>
        list1 =["rushabh","karan","hardik","jaynish","akshay"]
        count=0
        for i in list1:
            if len(i)>2 and i[0]==i[-1]:
                count+=1
        print(count)        



# 7) Write a Python program to remove duplicates from a list.
#ANS=>
        l =[7,7,4,5,6,6,4,9]
        l1 = []
        for i in l:
            if l.count(i)>1:
                l1.append(i)
        for i in l1:
            l1.remove(i)
        l1.extend(set(l1))
        l1


# 8) Write a Python program to check a list is empty or not.
#ANS=>

        l =[]
        if len(l)==0 :
            print("this list is emty")
        else:
            print("this list is not emty")


# 9) Write a Python function that takes two lists and returns true if they have at least one common member.
#ANS=>

        list1 = [2,27,35,55,35]
        list2 = [2,54,32,55,62]

        for x in list1:
            for y in list2:
                if x==y:
                    print("true")



# 10) Write a Python program to generate and print a list of first and last 5 elements where the values are square
#     of numbers between 1 and 30.
#ANS=>

        l = [i for i in range(1,31)]
        print(l)
        l = list()

        for i in range(1,31):
            l.append(i**2)
            
        print(l[:5])
        print(l[-5:])


# 11) Write a Python function that takes a list and returns a new list with unique elements of the first list.
 #ANS=>

        list1 = ["R","u","s","h","a","b","h"]

        print("list1: ", list1)

        str1 = ""
        for i in list1:
            str1 += i;
            
        print("str1: ", str1)    
            


# 12) Write a Python program to convert a list of characters into a string.
#ANS=>

        a=['hardik','rushabh','khushi',552,52,85]
        print("list =",a)
        b=tuple(a)
        print("Tuple =",b)



# 14) Write a Python program to find the second smallest number in a list.
#ANS=>

        l2 = []
        n = int(input("Enter the number of elements: "))
        for i in range(1, n+1):
            e = int(input("enter the elements: "))
            l2.append(e)
        l2.sort()

        print("The sorted list:", l2)
        print("The second smallest value of this list:",l2[1])



# 15) Write a Python program to get unique values from a list.
#ANS=>

        list = [2,4,5,3,2,5,4,7,6,7]
        unique_list=[]
        for a in list:
            if a not in unique_list:
                unique_list.append(a)
        print(unique_list)        


# 16) Write a Python program to check whether a list contains a sub list.
#ANS=>

        test_list = [1,3,5,3,6,4,1,3]
        print("the original list :" + str(test_list))
        sublist = [3,2,5]
        res = False
        for i in range(len(test_list) - len(sublist) + 1):
            if test_list[i: i + len(sublist)] == sublist:
                res = True
                break
            print("sublist present list :" + str(res))    



# 17) Write a Python program to split a list into different variables.
#ANS=>

        name = ['Rushabh','khushi','jaynish','hardik']
        print("name :",name)

        a,b,c,d = name
        print("var a:",a)
        print("var b:",b)
        print("var c:",c)
        print("var d:",d)


# 18) What is tuple? Difference between list and tuple.
#ANS=>

        '''
            The primary difference between tuples and lists is that tuples are immutable as opposed to lists which 
            are mutable. Therefore, it is possible to change a list but not a tuple. The contents of a tuple cannot 
            change once they have been created in Python due to the immutability of tuples.
        '''


# 19) Write a Python program to create a tuple with different data types.
#ANS=>

        t = ("tuple",False,5.3,7)
        print(t)


# 20) Write a Python program to create a tuple with numbers. 
 #ANS=>

        t = 6,12,18,24,30
        print(t)

        d = 12
        print(d)


# 21) Write a Python program to convert a tuple to a string.
#ANS=>

        a = ('R','u','s','h','a','b','h')
        str = "".join(a)
        print(str)


# 22) Write a Python program to check whether an element exists within a tuple.
#ANS=>

        a = ("Rushabh",75,"Salavi")
        if "Rushabh" in a:
            print("yes")
        else:
            print("No")


# 23) Write a Python program to find the length of a tuple. 
#ANS=>

        a = ("jaynish", 10,17,"patel",59)
        print(a)
        print(len(a))


# 24) Write a Python program to convert a list to a tuple.
#ANS=>

        a = ["hitesh","patel",58,54,53]
        print("List = ",a)
        b = tuple(a)
        print("tuple = ",b)



# 25) Write a Python program to reverse a tuple.
#ANS=>

        a = (43,65,32,87,34,12)
        reversed_tuple = a[::-1]
        print(reversed_tuple)



# 26) Write a Python program to replace last value of tuples in a list. 
#ANS=>

        l = [(70,80,90),(10,20,30,),(60,50,40)]
        print([t[:-1] + (150,) for t in l])



# 27) Write a Python program to find the repeated items of a tuple.
#ANS=>

        t = 11,14,14,16,14,13,11,16
        print(t)
        count =t.count(14)
        print(count)



# 28) Write a Python program to remove an empty tuple(s) from a list of tuples. 
#ANS=>

        l =[(),(),('I','J'),("K","L")]
        l =[t for t in l if t]
        print(l)


# 29)  Write a Python program to unzip a list of tuples into individual lists.
#ANS=>

        a,b,c = [1,2,3]
        print("a > ",a)
        print("b > ",b)
        print("c > ",c)


# 30) Write a Python program to convert a list of tuples into a dictionary.
#ANS=>

        tuples = [('21',21), ('22',22), ('23',23), ('24',24), ('25',25)]
        result = dict(tuples)
        print(result)


# 31)  How will you create a dictionary using tuples in python?
#ANS=>

        '''
        --> In Python, use the dict() function to convert a tuple to a dictionary. A dictionary object can be created
            with the dict() function. The dictionary is returned by the dict() method, which takes a tuple of tuples as 
            an argument. A key-value pair is contained in each tuple. 
        '''


# 32) Write a Python script to sort (ascending and descending) a dictionary by value.
#ANS=>

        d = {'guj':45,"eng":42,"account":49,"state":38}
        d1 ={}
        temp ={}
        for key,value in d.items():
            temp[value] =key
        print(temp)
        for key in sorted(temp.keys()):
            d1[key] =temp[key]
            
        print(d1)  


# 33) Write a Python script to concatenate following dictionaries to create a new one.
#ANS=>

        d1 = {1:100, 2:200}
        d2 = {3:300, 4:400}
        d3 = {5:500, 6:600}
        d4 = {}
        for d in (d1,d2,d3): d4.update(d)
        print(d4)    


# 34) Write a Python script to check if a given key already exists in a dictionary.
#ANS=>

        d = {'x':5, 'y':10}
        key = 'x'
        if key in d:
            print("This key is exists")
        else:
            print("This key not exists")


# 35) How Do You Traverse Through A Dictionary Object In Python? 
#ANS=>

        statesAndCapitals = {
            'Bihar': 'Patna',
            'maharashtra': 'Mumbai',
            'Gujarat': 'gandhinager',
            'Rajasthan': 'jaipur'
        }
        
        keys = statesAndCapitals.keys()
        print(keys)


# 36) How Do You Check The Presence Of A Key In A Dictionary?
#ANS=>

        my_dict = {'key1':10, 'key2':20, 'key3':30}
        if 'key1' in my_dict:
            print("key 'key1' this key is exists")
        else:
            print("this key not exists")



# 39) Write a Python script to merge two Python dictionaries.
#ANS=>

        r1 = {'a':4,'b':6,'c':8}
        r2 = {'d':10,'e':12}
        r3 = {**r1,**r2}
        print(r3)



# 40) Write a Python program to map two lists into a dictionary.
#ANS=>

        keys = {'RUSHABH','JAYNISH','KHUSHI'}
        values = {'75','58','60'}
        name_dictionary = dict(zip(keys,values))
        print(name_dictionary)


# 41) Write a Python program to combine two dictionary adding values for common keys. 
#     d1 = {'a': 100, 'b': 200, 'c':300}  d2 = {'a': 300, 'b': 200,'d':400}
#ANS=>

        d1 = {'a': 100, 'b': 200, 'c':300}
        d2 = {'a': 300, 'b': 200, 'd':400}
        for key in d2:
            if key in d1:
                d2[key] = d2[key] + d1[key]
            else:
                pass
        print(d2)    


# 42) Write a Python program to print all unique values in a dictionary.
#ANS=>

        d = [{'rus':1, 'is':2}, {'habh':1, 'for':3}, {'Salavi':2}]
        print("original list : " + str(d))
        r = list(set(val for dic in d for val in dic.values()))
        print("unique values in list :" + str(r))



# 43) Why Do You Use the Zip () Method in Python.
#ANS=>

        '''
            Zip is an in-built function in Python used to iterate over multiple iterables. It takes corresponding elements
            from all the iterable passed to it and merges them in a tuple. 
        '''


# 44) write a python program to create  and display all combinations of letters,selecting each letter frome
#     a different key in a dictionary.
# sample data: {1:['a,b'], 2:['c','d']}
#ANS=>

        d ={'1':['a','b'], '2':['c','d']}
        for i in d['1']:
            for j in d['2']:
                print(i+j)


# 45)   Write a Python program to find the highest 3 values in a dictionary
#ANS=>

        my_dict = {'A':90,'B':87,'C':85,'D':39,'E':66,'F':52}

        print("Initial Dictionary:")
        print(my_dict, "\n")

        print("Dictionary with 3  highest values:")
        print("keys: values")

        x =list(my_dict.values())
        d =dict()
        x.sort(reverse=True)
        x=x[:3]
        for i in x:
            for j in my_dict.keys():
                if(my_dict[j]==i):
                    print(str(j)+" : "+str(my_dict[j]))
                    
        Initial  Dictionary:
        {'A': 90, 'B': 87, 'C': 85,  'D': 39, 'E': 66, 'F': 52} 



# 46) Write a Python program to combine values in python list of dictionaries. 
#    Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
#    300}, o {'item': 'item1', 'amount': 750}]
#ANS=>

        from collections import Counter
        item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]
        result = Counter()
        for d in item_list:
            result[d['item']] += d['amount']
            print(result)


# 47)  Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the
#      string. 
#      Sample string: 'w3resource' 
#ANS=>

        str1 = 'W3resource'
        my_dict = {}
        for i in str1:
            my_dict[i] = my_dict.get(i,0) + 1
        print(my_dict)


# 48) Write a Python function to calculate the factorial of a number (a nonnegative integer)
#ANS=>

        num = int(input("Enter a number: "))
        factorial = 1
        if num < 0:
            print("")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
            print("The factorial of",num,"is",factorial)    


# 49) Write a Python function to check whether a number is in a given range.
#ANS=>

        start = int (input("Enter starting Range: "))
        end = int (input("Enter Ending Range: "))
        number =  int (input("Enter a number: "))
        if start <= number <= end:
            print("Number is in the Range")
        else:
            print("Number is not with in the range")



# 50) Write a Python function to check whether a number is perfect or not. 
#ANS=>

        num=int(input("Enter the number: "))
        sum_v = 0
        for i in range(1,num):
            if (num%i==0):
                sum_v=sum_v+i
        if(sum_v==num):
            print("The entered number is a perfect number")
        else:
            print("The entered number is not a perfect number")
    


# 51) Write a Python function that checks whether a passed string is palindrome or not.
#ANS=>

        a=input("Enter the string:")
        b=a[-1::-1]
        if (a==b) :
            print("palindrome")
        else:
            print("Not palindrome")



# 52) How Many Basic Types Of Functions Are Available In Python? 
#ANS=>

    '''
        There are two types of functions in python: User-Defined Functions - these types of functions are defined
        by the user to perform any specific task. Built-in Functions - These are pre-defined functions in python.
    '''


# 53) How can you pick a random item from a list or tuple?
#ANS=>

        import random
        list = [4,6,5,5,8,4]
        n = 4
        for i in range(n):
            print(random.choice(list), end = " ")



# 54) How can you pick a random item from a range?
#ANS=>

        import random
        test_list = [2, 5, 3, 6, 4, 8]
        print(" origanal list is :" + str(test_list))
        random_num = random.choice(test_list)
        print("random selected number is : " + str(test_list))


# 55) How can you get a random number in python?
#ANS=>

        import random
        print("A random number from list is : ", end="")
        print(random.choice([2, 4, 6, 8, 10]))
        print("A random number from range is : ",end="")
        print(random.randrange(10,30,5))



# 56) How will you set the starting value in generating random numbers?
#ANS=>

        import random
        for i in range(4):
            random.seed(0)
            print(random.randint(1, 1000))



# 57) How will you randomizes the items of a list in place?
#ANS=>

import random

        print("The origanal list is :" + str(test_list))
        test_list = [2, 4, 7, 5, 9]


        for i in range(len(test_list)-1,0, -1):
            j = random.randint(0, i + 1)
            test_list[i], test_list[j] = test_list[j], test_list[i]
        print("The shuffled list is : " + str(test_list))   


# 58) Write a Python program to read a random line from a file.
#ANS=>

        import random

        list = [4,8,10,15];
        random.shuffle(list)
        print("Reshuffled list : ", list)

        random.shuffle(list)
        print("Reshuffled list : ", list)


# 59) Write a Python program to convert degree to radian 
#ANS=>

        i = 22/7
        degree = float(input("input degrees: "))
        radian = degree *(i/190)
        print(radian)



# 60) Write a Python program to calculate the area of a trapezoid.
#ANS=>

        r1 = 8
        r2 = 10
        height = float(input("Height of trspezoid: "))
        r1 = float(input('base one value: '))
        r2 = float(input('base two value: '))
        area = ((r1 + r2) / 2) * height
        print("Area is:",area)


# 61)Write a Python program to calculate the area of a parallelogram.
#ANS=>

        base = float(input('length of base: '))
        height = float(input('Measurement of height: '))
        area = base * height
        print("Area is:",area)


# 62) Write a Python program to calculate surface volume and area of a cylinder.
#ANS=>

        x = 3.0
        y = 6.0
        surfacearea = (1*11*(x + y))/7
        print("surface Area of cylinder : ");
        print(surfacearea);


# 63) Write a Python program to returns sum of all divisors of a number.
#ANS=>

        def sum_div (number):
            divisors = [1]
            for i in range(2,number):
                if (number % i)==0:
                    divisors.append(i)
            return sum(divisors)
        print(sum_div(4))
        print(sum_div(6))


# 64)  Write a Python program to find the maximum and minimum numbers  from the specified decimal numbers. 
#ANS=>

        def max_min(data):
            l = data[0]
            s = data[0]
            for num in data:
                if num> l:
                    l = num
                elif num< 5:
                    s = num
            return l,s   
        print(max_min([0,10,15,40,-5,42,17,28,75]))
