systolic= int(input("Enter your systolic reading: "))
diastolic= int(input("Enter your diastolic reading: "))

if systolic < 90 or diastolic < 60:
    print ("Your blood pressure is LOW.")
elif (systolic >= 90 and systolic <= 120) and (diastolic >= 60 and diastolic <= 80):
    print ("Your blood pressure is NORMAL.")
elif systolic >= 120 or diastolic >= 80:
    print ("Your blood pressure is HIGH.")
else:
    print ("see a doctor")

