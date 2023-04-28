print("where do you live?")
print("press 1 if you live in apartment")
print("press 2 if you live in a house")
print("press 3 if you live in dormitory")
residence = int(input("where do you live: "))

    
print("Enter the number of hours you are home during the average day")
print("press(1) 18 or more")
print("press(2) 10-17")
print("press(3) 8-9")
print("press(4) 6-7")
print("press(5) 0-5 ")
hours = int(input("Select an hour category from the menu: "))

if (residence == 2 and hours == 1):
    print("Recommendation: Pot-bellied pig")

elif (residence == 2 and hours == 2):
     print("Recommendation: Dog")

elif (residence == 2 and hours == 3):
    print("Recommendation: Snake")
elif (residence == 2 and hours == 4):
    print("No recommendation")
elif (residence == 2 and hours == 5):
    print("No recommendation")   


elif (residence == 1 and hours == 1):
    print("Recommendation: Cat")
elif (residence == 1 and hours == 2):
    print("Recommendation: Cat")   

elif (residence == 1 and hours ==3):
    print("Recommendation: Hamster")
elif (residence == 1 and hours ==4):
    print("No recommendation")
elif (residence == 1 and hours ==5):
    print("No recommendation")

elif (residence == 3 and hours == 1):
    print("No recommendation")
elif (residence == 3 and hours == 2):
    print("No recommendation")
elif (residence == 3 and hours == 3):
    print("No recommendation")
elif (residence == 3 and hours == 4):
    print("Recommendation: Fish")
elif (residence == 3 and hours == 5):
    print("Recommendation: Ant farm")

else:
    "Invalid"
       







