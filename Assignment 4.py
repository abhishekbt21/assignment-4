#Q1
marks=int(input("Enter marks"))
if marks>=80:
    print("grade= A")
elif marks>=60:
    print("grade= B") 
elif marks>=50:
    print("grade= C")
elif marks>=45:
    print("grade= D")
elif marks>=25:
    print("grade= E")
elif (marks<=25):
    print("grade= F")
#Q2
year=int(input("year"))
if (year%400==0) and (year%100==0):
    print(year,"is a leap year") 
elif(year%4==0) and (year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
#Q3
import random
turns = 0
n = 1
print()
ques = int(input("How many questions needed to be there in test :\n"))
while turns < ques:
    n_1 = random.randint(1,10)
    n_2 = random.randint(1,10)

    print()
    print("Q -",n)
    print("What is", n_1,"x",n_2 ,"?")

    answer = int(input("Enter your answer :\n"))

    if (n_1)*(n_2) == answer:
        print("Your given answer is Correct")
    else :
        print("Your given answer is Wrong")
    
    print("\n")

    turns = turns + 1
    n = n + 1    
#Q4
for candies in range(0,200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(str(candies) + " is the correct answer")    
 

     
    

    

