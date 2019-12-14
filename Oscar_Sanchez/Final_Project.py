'''
Programmer Name:Oscar Sanchez
Date:12/7/19
Description:You are going to write a program called BankApp to simulate a banking application.
he information needed for this project are stored in a text file. Those are:
usernames, passwords, and balances.
Your program should read username, passwords, and balances for each customer, and
store them into three lists.
userName (string), passWord(string), balances(float)
The txt file with information is provided as UserInformtion.txt
'''
readfile=open("UserInformation.txt",'r')
userName=[]
passWord=[]
balance=[]
for row in readfile:
    column=row.split()
    userName.append(column[0])
    passWord.append(column[1])
    balance.append(float(column[2]))

def ValUser(user):
    while user not in userName:
        print("!!!Wrong User!!!")
        user=input("Please enter correct username:")
    return user
    
def ValPass(password):
    while password!=passWord[ind]:
        print("!!!Wrong Password!!")
        password=input("Please enter correct password:")
    return password
    
def Deposit(depositM):
    while depositM<0:
        depositM=float(input("Please enter correct amount: $"))
    balance[ind]+=depositM
    ShowBalance()
    
def Withdraw(withdrawM):
    while (withdrawM>balance[ind] or withdrawM<0):
        withdrawM=float(input("Please enter correct amount to withdraw: $"))
    balance[ind]-=withdrawM
    ShowBalance()
    
def ShowBalance():
    print("User: "+user+' Current Balance: $'+str(format(balance[ind],'.2f')))
    
def ChangeUser(user,password,ind):
    user=input("Please enter the user you want to switch to: ")
    user=ValUser(user)
    ind= userName.index(user)
    password=input("Please enter the password:")
    password=ValPass(password)
    return ind

print(userName)
print(passWord)
print(balance)
print("----- Welocome to the Bank App ----- \nPlease provide the following information")
user=input("Please enter the username:")
user=ValUser(user)
ind= userName.index(user)
password=input("Please enter the password:")
password=ValPass(password)

while True:
    print("----Menu----")
    option=input("Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit\nEnter option:").upper()
    if option=="D":
        depositM=float(input("Enter amount of money you want to deposit: $"))
        Deposit(depositM)
    elif option =="W":
        ShowBalance()
        withdrawM=float(input("Enter amount of money you want to withdraw: $"))
        Withdraw(withdrawM)
    elif option =="B":
        ShowBalance()
    elif option =="C":
        ind=ChangeUser(user,password,ind)
        print("Hello: "+userName[ind])
    elif option =="E":
        readfile.close()
        writefile=open("UserInformation.txt",'w')
        for i in range(len(userName)):
            writefile.write(userName[i]+"\t"+passWord[i]+"\t"+str(balance[i])+"\n")
        exit()
    else:
        print("Enter the Correct Option")
        False
    print('\n')

