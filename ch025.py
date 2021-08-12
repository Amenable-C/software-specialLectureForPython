firstName = input("Enter your first name : ")

if(len(firstName) < 5):
    surName = input("Enter your surname : ")
    fullName = firstName + surName
    print(fullName.upper())
else:
    print(firstName.lower())