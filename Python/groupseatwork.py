medical = 650
dental = 500
long =  1000

print("press 1 if your skill level is 1")
print("press 2 if your skill level is 2")
print("press 3 if your skill level is 3")
skilllevel = int(input("Enter skill level: "))

if skilllevel == 2:
    hours = int(input("Hours worked: "))
    print("press option 1 for medical insurance the rate is: 650")
    print("press option 2 for dental insurance the rate is 500")
    print("press option 3 for long-term disability insurance the rate is 1000")
    insurance = int(input("What is your appropriate insurance and retirement plan:"))

elif skilllevel == 3:
    hours = int(input("Hours worked: "))
    print("press option 1 for medical insurance the rate is 650")
    print("press option 2 for dental insurance the rate is 500")
    print("press option 3 for long-term disability insurance the rate is 1000")    
    insurance = int(input("What is your appropriate insurance and retirement plan:"))
elif skilllevel == 1:
    hours = int(input("Hours worked: "))
    print("Hours worked: ", hours)

if (skilllevel == 1 and hours < 40):
    regular = (350 * hours)
    print("Hourly pay rate: 350")
    print("Regular pay: ", regular)
    print("Net pay: ", regular)
elif (skilllevel == 1 and hours < 40) :
    regular = (350 * hours)
    print("Hourly pay rate: 350")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Dental insurance -- 500")
    print("Net pay: ", regular)
elif (skilllevel == 1 and hours < 40) :
    regular = (350 * hours)
    print("Hourly pay rate: 350")
    print("Regular pay: ", regular)
    print("Net pay: ", regular)
elif (skilllevel == 2 and hours < 40 and  insurance == 1):
    regular = (400 * hours)
    print("Hourly pay rate: 400")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Medical insurance -- 650")
    print("Net pay: ", regular - medical)
elif (skilllevel == 2 and hours < 40 and insurance == 2):
    regular = (400 * hours)
    print("Hourly pay rate: 400")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Dental insurance -- 500")
    print("Net pay: ", regular - dental)
elif (skilllevel == 2 and hours < 40 and insurance == 3):
    regular = (400 * hours)
    print("Hourly pay rate: 400")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Long-term disability insurance -- 1000")
    print("Net pay: ", regular - long)
elif (skilllevel == 3 and hours < 40 and insurance == 1):
    regular = (460 * hours)
    retirement = regular *0.03
    total1 = retirement + medical
    print("Hourly pay rate: 460")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Medical insurance -- 650")
    print("retirement plan at 3% of their gross pay: ", retirement )
    print("Total:", total1)
    print("Net pay: ", regular - total1 )
elif (skilllevel == 3 and hours < 40 and insurance == 2):
    regular = (460 * hours)
    retirement = regular *0.03
    total1 = retirement + dental
    print("Hourly pay rate: 460")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Dental insurance -- 500")
    print("retirement plan at 3% of their gross pay: ", retirement )
    print("Total:", total1)
    print("Net pay: ", regular - total1 )
elif (skilllevel == 3 and hours < 40 and insurance == 3):
    regular = (460 * hours)
    retirement = regular *0.03
    total1 = retirement + long
    print("Hourly pay rate: 460")
    print("Regular pay: ", regular)
    print("Itemized deduction:")
    print("Long-term disability insurance -- 1000")
    print("retirement plan at 3% of their gross pay: ", retirement )
    print("Total:", total1)
    print("Net pay: ", regular - total1 ) 

elif (skilllevel == 1 and hours >= 40):
    overtotal = (350 * 0.5) * hours
    regular = (350 * hours)
    overtime = overtotal - regular
    retirement = regular *0.003
    print("Hourly pay rate: 350")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtime)
    print("Total of regular and overtime pay:", regular + overtime )
    

elif (skilllevel == 2 and hours >= 40 and insurance == 1):
    overtotal = (600)*(hours - 40)
    regular = (400 * hours)
    retirement = regular *0.03
    total1 = retirement + medical
    print("Hourly pay rate: 400")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Medical insurance -- 650")

    print("Total:", medical)
    print("Net pay: ", (regular + overtotal) - medical)


elif (skilllevel == 2 and hours >= 40 and insurance == 2):
    overtotal = (600)*(hours - 40)
    regular = (400 * hours)
    retirement = regular *0.03
    total1 = retirement + dental
    print("Hourly pay rate: 400")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Dental insurance -- 500")
    print("Total:", dental)
    print("Net pay: ", (regular + overtotal) - dental)
elif (skilllevel == 2 and hours >= 40 and insurance == 3):
    overtotal = (600)*(hours - 40)
    regular = (400 * hours)
    overtime = overtotal - regular
    retirement = regular *0.03
    total1 = retirement + long
    print("Hourly pay rate: 400")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Long-term disability insurance -- 1000")
    print("Total:", long)
    print("Net pay: ", (regular + overtotal) - long)
elif (skilllevel == 3 and hours >= 40 and insurance == 1):
    overtotal = (690)*(hours - 40)
    regular = (460 * hours)
    retirement = regular *0.03
    total1 = retirement + medical
    print("Hourly pay rate: 460")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Medical insurance -- 650")
    print("retirement plan at 3% of their gross pay:", retirement)
    print("Total:", total1)
    print("Net pay: ", (regular + overtotal) - total1)
elif (skilllevel == 3 and hours >= 40 and insurance == 2):
    overtotal = (690)*(hours - 40)
    regular = (460 * hours)
    
    retirement = regular *0.03
    total1 = retirement + dental
    print("Hourly pay rate: 460")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Dental insurance -- 650")
    print("retirement plan at 3% of their gross pay:", retirement)
    print("Total:", total1)
    print("Net pay: ", (regular + overtotal) - total1)
elif (skilllevel == 3 and hours >= 40 and insurance == 3):
    overtotal = (690)*(hours - 40)
    regular = (460 * hours)
    retirement = regular *0.03
    total1 = retirement + long
    print("Hourly pay rate: 460")
    print("Regular pay for 40 hours:", 460* 40)
    print("Overtime pay: ", overtotal)
    print("Total of regular and overtime pay:", regular + overtotal )
    print("Itemized deduction:")
    print("Long-term disability insurance -- 1000")
    print("retirement plan at 3% of their gross pay:", retirement)
    print("Total:", total1)
    print("Net pay: ", (regular + overtotal) - total1)


else:
    print("error")