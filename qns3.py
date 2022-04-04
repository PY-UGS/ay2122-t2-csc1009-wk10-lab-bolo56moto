modCode = input("Enter module code: ")

def module(i):
    case = {
        0:'Mathematics 2',
        1:'Operating Systems',
        2:'Data Structures and Algorithms',
        3:'Object Oriented Programming',
        4:'Computer Networks'
    }
    return print(case.get(i))

if modCode == "CSC1006":
    module(0)
elif modCode == "CSC1007":
    module(1)
elif modCode == "CSC1008":
    module(2)
elif modCode == "CSC1009":
    module(3)
elif modCode == "CSC1010":
    module(4)
else:
    print("Invalid module code.")


print("Odd numbers in descending order from 102 to 66: ")
for i in range(102,64,-1):
    if(i%2!=0):
        print(i)