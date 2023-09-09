
#(1) Write a Python program to check if a number is positive, negative or zero.
#=> ANS
            n = float(input("Input a number: "))
            if n >= 0:
             if n == 0:
                print("It is Zero")
             else:
                print("Number is Positive number")
            else:
                print("Number is Negative number")




#(2)  Write a Python program to get the Factorial number of given number.
#=> ANS

            num = int(input("Enter a number: "))
            factorial = 1
            if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
            elif num == 0:
            print("The factorial of 0 is 1")
            else:
            for i in range(1,num + 1):
                factorial = factorial*i
            print("The factorial of",num,"is",factorial)



#(3) Write a Python program to get the Fibonacci series of given range.
#=> ANS

            n = 10
            num1 = 0
            num2 = 1
            next_number = num2 
            count = 1
            
            while count <= n:
                print(next_number, end=" ")
                count += 1
                num1, num2 = num2, next_number
                next_number = num1 + num2
            print()




#(4) How memory is managed in Python?
#=> ANS

# According to the Python memory management documentation,
# Python has a private heap that stores our program’s objects and data structures. 
# Python memory manager takes care of the bulk of 
# the memory management work and allows us to concentrate on our code.


#(5) What is the purpose continue statement in python?
#=> ANS

# The continue keyword is used to end the current iteration in a for loop (or a while loop), 
# and continues to the next iteration.


#(6) Write python program that swap two number with temp variable and 
#    without temp variable.
#=> ANS

            x = input('Enter value of x: ')
            y = input('Enter value of y: ')

            temp = x
            x = y
            y = temp
                print('The value of x after swapping: {}'.format(x))
                print('The value of y after swapping: {}'.format(y))

#(7) Write a Python program to find whether a given number is even or odd, 
#    print out an appropriate message to the user.
#=> ANS

        num = int(input("Enter a number: "))  
        if (num % 2) == 0:  
            print("{0} is Even number".format(num))  
        else:  
            print("{0} is Odd number".format(num))   



#(8) Write a Python program to test whether a passed letter is a vowel or not.
#=> ANS

    character = input("Enter a character: ")  
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
    
    if character in vowels:  
        print(f"The character '{character}' is a vowel!")  
    else:  
        print(f"The character '{character}' is a not vowell ")  




#(9) Write a Python program to sum of three given integers. However, if 
#    two values are equal sum will be zero.
#=> ANS

        def sum_three(x, y, z):
            if x == y or y == z or x==z:
                sum = 0
            else:
                sum = x + y + z
            return sum
        print(sum_three(2, 1, 2))
        print(sum_three(3, 2, 2))
        print(sum_three(2, 2, 2))
        print(sum_three(1, 2, 3))



#(10) Write a Python program that will return true if the two given integer values are equal 
#      or their sum or difference is 5.
#=> ANS

                a = int(input("enter the number ="))
                b = int(input("enter the number ="))
                if a==b or a+b==5 or abs(a-b)==5:
                    print("true")
                else:
                    print("false")


#(11) write a python program to sum of the first n positive integers.
#=> ANS

                n = int(input("input a number: "))
                sum_num = (n *(n + 1)) / 2
                print("sum of the first", n ,"positive integers:",sum_num)



#(12) write a python program to calculate the length of a string.  
#=> ANS

                n='handle situation where reference counting alone is not sufficient, python employs a garbage collector'
                len(n)


#(13) Write a Python program to count the number of characters (character frequency) in a string.
#=> ANS

                s=input("Enter numbre = ")
                for i in s:
                    print(i,'>>>>',s.count(i))



#(14) Write a Python program to count occurrences of a substring in a string.
#=> ANS

            s = 'python also uses memory polling to improve the performance of memory allocations and deallocations.'
            for i in s.split():
                print(i,'>>>',s.count(i))



#(15) Write a Python program to count the occurrences of each word in a given sentence.
#=> ANS

            str1 = 'the quik brown fox jump over the lazy dog.'
            print(str1.count("over"))



#(16) Write a Python program to get a single string from two given strings, separated by a space and swap the
#first two characters of each string.
#=> ANS

            a = int(input("enter the number ="))
            b = int(input("enter the number ="))
            if a==b or a+b==5 or abs(a-b)==5:
                print("true")
            else:
                print("false")


#(17)  Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it unchanged.
#=> ANS

            s = input("enter the string = ")
            if len(s)>3:
                print(s + 'ing')
                if s[-3:] == 'ing':
                    a = s.replace('ing','ly')
                    print(a)
            else:
                print('unchanged')



#(18) What are negative indexes and why are they used?
#=> ANS

        # Negative Indexing is used to in Python to begin slicing from the end of the string i.e. the last. Slicing in Python gets a sub-string from a string. 
        # The slicing range is set as parameters i.e. start, stop and step



#(19) Write a Python program to find the first appearance of the substring'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace thewhole 'not'...'poor' substring with 'good'. Return the resulting string.
#=> ANS

            s = "The person is not good poor he is a middle class guys"
            s =s.replace(s[s.find('not'): s.find('poor')+4],'good')
            print(s)



#(20) Write a Python function that takes a list of words and returns the length of the longest one.
#=> ANS

            s = "python uses refernce counting as its primary memory management technique."
            l = s.split()

            temp = 0
            for i in l :
                if len(i) > temp:
                    temp = len(i)
                    word = i

            print(temp,word)



 #(21) Write a Python function to reverses a string if its length is a multiple of 4.
#=> ANS

            n = input("Enter = ")
            if len(n)%7==0:
                print(n[::-1])
            else:
                print(n)   


#(22) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the
#   string length is less than 2, return instead of the empty string.
#=> ANS

            c = input()
            t = len(c)
            temp = ""
            for i in range(0,len(c)):
                if t<3:
                    break
                else:
                    if i in (0,1,t-2,t-1):
                        temp = temp+c [i]
                    else:
                        continue
            print(temp)           



#(23) Write a Python function to insert a string in the middle of a string.
#=> ANS

            s = input('enter the string:')
            m = 'Salavi'
            print(s[:len(s)//1],m,s[len(s)//1:])