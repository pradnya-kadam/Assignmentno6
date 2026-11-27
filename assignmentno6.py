# wap pgm to reverse a number
# num=1234
# original=num
# digit=0
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10

# print(rev)

#2 WAP to check whether a number isa palindrome 

# num=121
# original=num
# rev=0 
# digit=0
# while num>0:
#     digit=num%10 
#     rev=rev*10+digit
#     num=num//10

# if original==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#3 WAP to check whether a number is a armstrong  number 
# num=153 
# original=num
# nod=len(str(num))
# arm=0
# while num>0:
#     for i in range(0,num+1):
#         digit=num%10 
#         arm+=digit**3
#         num=num//10
        
# if arm==original:
#     print("armstrong")
# else:
#     print("not armstrong") 

#4 WAP to find factorial of a number using aloop 

# num=int(input("enter a num "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of no",fact)

# WAP to generate the fibonacci series up to N terms 
# num=int(input("enter a no"))
# a=0
# b=1
# sum=0
# for i in range(num):
#         print(sum)
#         a=b
#         b=sum
#         sum=a+b
    
#6 wap to check whether a number is prime 
# num=int(input("enter a no"))
# if num%2!=0:
#     print("prime no")
# else:
#     print("not prime no")


#7 WAP to print all prime numbers between 1 and 100 

# for i in range(0,100):
#     if i%2!=0:
#         print("prime",i)
#     else:
#         print("not prime",i)

#8 WAP to find GCD and LCM of two numbers
# gcd=0 
# num1=int(input("enter a no"))
# num2=int(input("enter a no"))
# if num2>num1:
#     mn=num1 
# else:
#     mn=num2
# for i in range(1,mn+1):
#     if num1%i==0 and num2%i==0:
#         print(i) 
# lcm=(num1*num2)/i
# print("lcm is",lcm)
# print("gcd of no is",i)

# 9 WAP to reverse a string without using slicing 

# str=input("enter ur string")
# s="" 
# for ch in str:
#     s=ch+s 
# print(s)


#10 WAP to count vowels,consonants,digits and special characters in a string

# char=input("enter ur string")
# for ch in char:
#     if ch in "AEIOUaeiou":
#         print("spoecial charcter")
#     elif ch.isalpha():
#         print("vowels")
#     elif ch.isdigit():
#         print("digits")
#     else:
#         print("special charcter")

#12 WAP to find the frequency of each character in a string 
# def countfreq(str):
#     s={}
#     for ch in str:
#         if ch in s:
#             s[ch]+=1
#         else:
#             s[ch]=1
#     return  s
# stri=input("enter a string")
# print(countfreq(stri))

#13 WAP to find out first non repeating character

# def first(s):
#     for i in s:
#         count=0
#         for j in s:
#             if i==j:
#                 count+=1
#         if count==1:
#             return i 
# s="aabcfd"
# print(first(s))

# 14 WAP to remove duplicate charcters from string 

# str=input("enter ur string")
# result=""
# for ch in str:
#     if ch not in result:
#         result+=ch
# print(result)

#15 WAP to check whether two strings are anagrams 

# char1=input("enter ur string")
# char2=input("enter ur string")

# if len(char1)==len(char2):
#     for ch in char1:
#         for  ch2 in char2:
#             if ch==ch2:
#                 print("anagram")
#             else:
#                 print("not")

#16 WAP to find longest word in a sentence 
# sentence="iam a final year student of engineering"
# sent=sentence.strip().split()
# print(max(sent,key=len))

#17WAP to find out the second largest element
# sentence="iam a final year student of engineering"
# sent=sentence.split()
# length=sorted(sent,key=len,reverse=True)

# print(length[1])

#18 remove duplicate element from a list without using set()

# list=[1,2,3,4,5,6,7,1]
# l=[]
# for i in range(1,len(list)):
#     if i not in l:
#         l.append(i)
# print(l)

#19 find the common elements between two lists 

# l1=[1,2,3,4]
# l2=[5,6,7,4]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(i)

# print(l3)

#20 move all zeros to the end of a list without chnaging the order of other elemnts 
# list=[1,2,0,3,0,4,5,6,7]
# l2=[]
# l3=[]
# for i in list:
#     if i==0:
#         l2.append(i)
#     if i!=0:
#         l3.append(i)

# print(l3+l2)

#21 find the missing number in a list containing number from 1 to n 

# def find_missing(a,n):
#     total=n*(n+1)//2
#     arr_sum=0
#     for num in a:
#         arr_sum+=num
#     return total-arr_sum



# print(find_missing([1,2,4,5],5))

# #22. Find the maximum difference between two elements where the larger element appears after the smaller element.
# arr=[1,2,3,4,5,6]

# sum=[]
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         total=arr[j]-arr[i]
#         sum.append(total)
# print(max(sum))

#23 23. Rotate a list to the right by K positions.
# a=[1,2,3,4,5]
# k=7
# k=k%len(a)
# a=a[-k:]+a[:-k]
# print(a)

#24 24. Find all pairs in a list whose sum equals a given target.
 
# list=[1,2,3,4,5,6]
# target=10
# for i in range(0,len(list)):
#     if list[i]+list[i+1]==target:
#         print("target found",target)
#     else:
#         print("not")

#25 WAP to count the frequency of a each word in a paragraph 

# p="iam a final year student iam srudying at mit corer barshi solapur "
# word=p.strip().split()
# s={}

# for i in word:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1

# print(s)

#26 26. Write a program to merge two dictionaries. If a key exists in both, add their values.
# dict1={'a':10,'b':20,'c':30,'d':40}
# dict2={'a':15,'b':25,'c':30,'d':40,'e':90}
# result=dict1.copy()
# for key,value in dict2.items():
#     if key in result:
#         result[key]+=value
#     else:
#         result[key]=value

# print(result)

# 27. Write a program to sort a dictionary based on its values.

# dict={'a':15,'b':35,'c':30,'d':40,'e':90}
# result=sorted(dict.items(),key=lambda x:x[1])
# print(result)

#28. Given a list of student dictionaries containing name and marks, find the student with the highest marks.

# student={
#     "name":["pk","dk","rk","sk"],
#     "marks":[45,65,76,78]
# }

# result=max(student['marks'])
# print(result)

#29 29. Group words from a list based on their first character using a dictionary.

# words = ["apple", "ant", "banana", "ball", "cat", "car"]
# s={}
# for i in words:
#     key=i[0]
#     if key in s:
#         s[key].append(i)
#     else:
#        s[key]=[i]
# print(s)

#30 30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.

# keys=["name","age","city"]
# values=["pradnya",21,"akt"]
# result=dict(zip(keys,values))
# print(result)

# 31. Write a recursive function to calculate the factorial of a number.
# def factorial(num):
#     if num==0 or num==1:
#         return 1

#     return num*factorial(num-1)

# print(factorial(5))

#32 Write a recursive function to find the sum of digits of a number.

# def sum(n):
#     if n==0:
#         return 0

#     return n%10 +sum(n//10)

# print(sum(12345))


# 32. Write a recursive function to find the sum of digits of a number.
# def my_map(func,arr):
#     result=[]
#     for i in arr:
#         result.append(func(i))

#     return result 

# def sq(n):
#     return n*n

# numbers=[1,2,3,4,5]
# print(my_map(sq,numbers))

# 34. Implement a function that accepts a list and returns a new list containing only even numbers.

# def even(list):
#     result=[]
#     for i in list:
#         if i%2==0:
#             result.append(i)

#     return result 
# print(even([1,2,3,4,5,6,7,8,9,10,12]))


# 35. Write a function to flatten a nested list.

# def flatten(lst):
#     result=[]
#     for i in lst:
#         if isinstance(i, list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)
#     return result 

# print(flatten([1,[2,3],[4,[5,6]]]))

#36  36. Student Management System

# Create a console-based application with the following operations:
# - Add student
# - Display all students
# - Search student by ID
# - Update student details
# - Delete student


# class Student:
#     def init(self):
#         self.students = {}

#     def add_student(self):
#         name=input("enter ur name")
#         id=int(input("enter ur id"))
#         self.students[id] = name
#         print("student add successful")


#     def display(self):
#         for id, name in self.students.items():
#             print(id, name)


#     def search(self):
#         id=int(input("enter id for search"))
#         if id in self.students:
#             print("the stuent is found",self.students[id])
#         else:
#             print("student not found")

#     def update(self):
#         id =int(input("enter id to chnge the details"))
#         if id in self.students:
#             name=input("enter name too update")
#             self.students.update({id: name})
#             print("update sussesfully")
#         else:
#             print("student not found")

#     def delete(self):
#         id=int(input("enter id for delete"))
#         if id in self.students:
#             self.students.pop(id)
#             print("data removed successfully ")


# obj = Student()

# while True:
#     print("1.add studet")
#     print("2. Display Student")
#     print("3. search student ")
#     print("4. Update studet")
#     print("5. delete student")
#     print("6. exit") 
#     ch=int(input("enter ur choice"))
#     if ch==1:
#         obj.add_student()
#     elif ch==2:
#         obj.display()
#     elif ch==3:
#         obj.search()
#     elif ch==4:
#         obj.update()
#     elif ch==5:
#         obj.delete()
#     elif ch==6:
#         break
#     else:
#         print("invalid choice")


# 37. Bank Account Management

# Create a bank account program with:
# - Create account
# - Deposit money
# - Withdraw money
# - Check balance
# - Display account details

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self):
#         name = input("Enter your name: ")
#         acc_no = input("Enter account number: ")

#         if acc_no in self.accounts:
#             print("Account already exists!")
#         else:
#             self.accounts[acc_no] = {
#                 "name": name,
#                 "balance": 0
#             }
#             print("Account created successfully!")

#     def deposit(self):
#         acc_no = input("Enter account number: ")

#         if acc_no in self.accounts:
#             amount = float(input("Enter deposit amount: "))

#             if amount > 0:
#                 self.accounts[acc_no]["balance"] += amount
#                 print("Amount deposited successfully!")
#             else:
#                 print("Enter a valid amount.")
#         else:
#             print("Account not found!")

#     def withdraw(self):
#         acc_no = input("Enter account number: ")

#         if acc_no in self.accounts:
#             amount = float(input("Enter withdrawal amount: "))

#             if 0 < amount <= self.accounts[acc_no]["balance"]:
#                 self.accounts[acc_no]["balance"] -= amount
#                 print("Withdrawal successful!")
#             else:
#                 print("Insufficient balance or invalid amount.")
#         else:
#             print("Account not found!")

#     def check_balance(self):
#         acc_no = input("Enter account number: ")

#         if acc_no in self.accounts:
#             print("Balance:", self.accounts[acc_no]["balance"])
#         else:
#             print("Account not found!")

#     def display_accounts(self):
#         for acc_no, details in self.accounts.items():
#             print("Account Number:", acc_no)
#             print("Name:", details["name"])
#             print("Balance:", details["balance"])
#             print("-------------------")

# bank = Bank()

# while True:
#     print("\n1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check Balance")
#     print("5. Display Accounts")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         bank.create_account()
#     elif choice == "2":
#         bank.deposit()
#     elif choice == "3":
#         bank.withdraw()
#     elif choice == "4":
#         bank.check_balance()
#     elif choice == "5":
#         bank.display_accounts()
#     elif choice == "6":
#         print("Thank you!")
#         break
#     else:
#         print("Invalid choice!")

#create  a pgm -add employee details - calculate gross salary - calculate deduction -calculate net salary - display employee salary details 


# class Employee:
#     def __init__(self):
#         self.name = ""
#         self.salary = 0
#         self.gross = 0
#         self.deduction = 0
#         self.net = 0

#     def add_employee(self):
#         self.name = input("Enter employee name: ")

#     def gross_salary(self):
#         self.salary = int(input("Enter basic salary: "))
#         hra = int(input("Enter HRA: "))
#         da = int(input("Enter DA: "))
#         other = int(input("Enter other allowances: "))

#         self.gross = self.salary + hra + da + other
#         print("Gross Salary:", self.gross)

#     def calculate_deduction(self):
#         self.deduction = int(input("Enter deduction amount: "))
#         print("Deduction:", self.deduction)

#     def net_salary(self):
#         self.net = self.gross - self.deduction
#         print("Net Salary:", self.net)

#     def employee_details(self):
#         print("\n--- Employee Salary Details ---")
#         print("Name:", self.name)
#         print("Gross Salary:", self.gross)
#         print("Deduction:", self.deduction)
#         print("Net Salary:", self.net)


# emp = Employee()

# while True:
#     print("\n1. Add employee details")
#     print("2. Calculate gross salary")
#     print("3. Calculate deduction")
#     print("4. Calculate net salary")
#     print("5. Display employee details")
#     print("6. Exit")

#     ch = input("Enter your choice: ")

#     if ch == "1":
#         emp.add_employee()

#     elif ch == "2":
#         emp.gross_salary()

#     elif ch == "3":
#         emp.calculate_deduction()

#     elif ch == "4":
#         emp.net_salary()

#     elif ch == "5":
#         emp.employee_details()

#     elif ch == "6":
#         break

#     else:
#         print("Invalid choice")

# 39. Library Management System

# Create a program to:
# - Add books
# - Display available books
# - Issue a book
# - Return a book
# - Search books by title

# class Library:
#     def __init__(self):
#         self.books={
#             "python":True,
#             "java":True,
#             "R":True
#         }

#     def add_books(self):
#         name=input("enter ur book name")
#         self.books[name]=True
#         print("Books added successfully")


#     def available_books(self):
#         for name,status  in self.books.items():
#             if status==True:
#                 print(name)



#     def issue_book(self):
#         name=input("enter ur book name for issue")
      
#         if name in self.books:
#             if self.books[name]==True:
#                 self.books[name]==False
#                 print("book issued successfully")
#             else:
#                 print("book already issued")

#         else:
#             print("book not found")


#     def return_book(self):
#        name=input("enter ur book name")

#        if name in self.books:
#            if self.books[name]==False:
#                print("book rerurned successfully")
#            else:
#                print("book is already available")
#        else:
#            print("book not found")    

#     def search_book(self):
#         name=input("enter book name to search")

#         if name in self.books:
        
#             print("book found",self.books[name])
#         else:
#             print("not found")

        
# Lib=Library()
# while True:
#     print("- Add books")
#     print("Display available books ")
#     print("issue a book")
#     print("Return a book")
#     print("Search books by title")

#     ch=input("enter ur choice")
#     if ch=='1':
#         Lib.add_books()

#     elif ch=="2":
#         Lib.available_books()

#     elif ch=="3":
#         Lib.issue_book()

#     elif ch=="4":
#         Lib.return_book()

#     elif ch=="5":
#         Lib.search_book()

#     else:
#         break
    
# 40. Task Management Application

# Create a console-based task manager with:
# - Add task
# - View all tasks
# - Update task
# - Delete task
# - Mark task as completed
# - Filter completed and pending tasks


class Task_Management:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Enter task name: ")

        self.tasks.append({
            "name": name,
            "status": "Pending"
        })

        print("Task added successfully")

    def view_task(self):
        if not self.tasks:
            print("No tasks available")
        else:
            for task in self.tasks:
                print(task["name"], "-", task["status"])

    def update_task(self):
        name = input("Enter task name to update: ")

        for task in self.tasks:
            if task["name"] == name:
                new_name = input("Enter new task name: ")
                task["name"] = new_name
                print("Task updated successfully")
                return

        print("Task not found")

    def delete_task(self):
        name = input("Enter task name to delete: ")

        for task in self.tasks:
            if task["name"] == name:
                self.tasks.remove(task)
                print("Task deleted successfully")
                return

        print("Task not found")

    def mark_task(self):
        name = input("Enter task name to mark completed: ")

        for task in self.tasks:
            if task["name"] == name:
                task["status"] = "Completed"
                print("Task completed successfully")
                return

        print("Task not found")

    def filter_completedtask(self):
        for task in self.tasks:
            if task["status"] == "Completed":
                print(task["name"])

    def filter_pendingtask(self):
        for task in self.tasks:
            if task["status"] == "Pending":
                print(task["name"])


obj = Task_Management()

while True:

    print("\n1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task completed")
    print("6. View completed tasks")
    print("7. View pending tasks")
    print("8. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        obj.add_task()

    elif ch == "2":
        obj.view_task()

    elif ch == "3":
        obj.update_task()

    elif ch == "4":
        obj.delete_task()

    elif ch == "5":
        obj.mark_task()

    elif ch == "6":
        obj.filter_completedtask()

    elif ch == "7":
        obj.filter_pendingtask()

    elif ch == "8":
        break

    else:
        print("Invalid choice")
