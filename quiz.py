#Quiz program

q1 = """which language you  should prefer ? 
a. C++
b. Python
c. Js
d. C# """


q2 = """Which subject you should be focus onn ?
a. English
b. Maths
c. Science
d. History """


q3 = """Is 2+2 = 4 ?
a. No
b. Yes
c. maybe
d. wrong question """

questions = {q1:"b",q2:"b", q3 :"b"}

name = input("Enter your name :")
print("Hello",name, "Welcome to the quiz world")
score=0
for i in questions:
    print()
    print(i)
    flag1 = input("Do you want to skip the question (Yes/No)")
    if flag1=="Yes":
        continue

    ans = input("Enter the answer (a/b/c/d):")
    if ans == questions[i]:
        print("Correct answer, you got 1 point")
        score = score+1
        print("current score is:",score)
    else:
        print("wrong answer, you lost 1 point")
        score=score-1
        print("current score is:",score)
    flag2 = input("Do you want to quit(Yes/No):")
    if flag2 =="Yes":
        break
print("Final score is:",score)