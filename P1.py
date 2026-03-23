# Calc Marks Program
name = input("Enter your name: ")
while len(name)<5:
    name=input("Please, give a real name: ")
total = 0
for i in range(5):
    n = i + 1
    a = int(input("Enter mark " + str(n) + ": "))
    while a>100 or a<0:
        print("Wrong data...")
        a=int(input("Please, re-enter mark " +str(n)+": "))
        break
    total = total + a
avg=total/5
print(name + "'s total marks: " + str(total))