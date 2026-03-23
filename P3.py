# Calc Marks Program
print("""Hello, my name is Ella and I'm going to help you 
calculate your Total marks, Average marks and Grade""")

# name-val section
name = input("What's your name?: ")
while len(name) < 3:
    name = input("Please, give a real name: ")

# Sub-val section
n = int(input("How many subjects do you take? "))
if n >= 15:
    print("""Taking more than 14 subjects must be overwhelming, isn't it?
    Anyways, let's continue ;(""")
    
total = 0

for i in range(n):
    subject_no = i + 1   # ✅ don't mess with n
    
    while True:
        a = input("Enter mark " + str(subject_no) + ": ")
        
        try:
            a = int(a)
            
            if a > 100 or a < 0:
                print("Wrong data...")
            else:
                break   # valid mark
                
        except:
            print("Please enter a valid number!")

    total = total + a

avg = total / n   # ✅ now n is still correct

print("Results obtained, calculating.......")
print("__________________________________________________")
print(name + ", here are your results.")
print("Total marks: " + str(total))
print("Average marks: " + str(avg))