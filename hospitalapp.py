patient_name = input('enter patient name')
patient_age = int(input ('enter patient_age'))
datetime=input('enter datetime')
dischargeDatetime= input('enter dischargeDatetime')

listPatient= patient_name + datetime + dischargeDatetime
print(listPatient)
if patient_age >= 40:
    print('you old buddy')
elif patient_age <= 35:
    print('you are almost there')

else: print('you underage')



