answer1 = str.lower(input("Is it raining?"))
if (answer1 == "yes"):
    answer2 = str.lower(input("Is it windy?"))
    if(answer2 == "yes"):
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")