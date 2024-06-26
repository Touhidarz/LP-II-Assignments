#import bodyStats
#import symptomQuestions

print('Welcome to COVID-19 Expert system')
covidSuspicionCounter=0


severity=0
asym=0 
oxygen_level=0
temperature_flag=0

bodyStats=['What is your body temperature','What is your oxygen level','How many vaccines have you taken','What is your age']
symptomQuestions=['Do you have cough and cold','Are you able to recognize smell and taste','Are you suffering from sore throat','Are you suffering from headache','Are you suffering from BP/ diabetes','Have you come in a contact of a Covid suspicious person']



for i in range(6):

    print(symptomQuestions[i])
    print()
    ans=input()

    if(i!=1 and ans=='yes'):

        covidSuspicionCounter+=1

    elif(i==1 and ans=='no'):

        covidSuspicionCounter+=1

for i in range(4):

    print(bodyStats[i])
    print()

    if(i==0):
        ans=float(input())

        if(ans>=101.0):
            severity+=2
            covidSuspicionCounter+=1
            temperature_flag=1

        elif(ans<101.0 and ans>=99.6):
            severity+=1

        else:
            severity+=0
    if(i==1):
        ans=int(input())

        if(ans>=94):
            severity+=0

        elif(ans<94 and ans>87):
            severity+=1

        else:
            severity+=2
            covidSuspicionCounter+=1
            oxygen_level=1

    if(i==2):
        ans=int(input())

        if(ans==0):
            severity+=2

        elif(ans==1):
            severity+=1

        else:
            severity+=0

    if(i==3):
        ans=int(input())

        if(ans>12 and ans<31):
            severity+=0

        elif(ans>31 and ans<51):
            severity+=1

        else:
            severity+=2

if(covidSuspicionCounter>3):
    print('The patient is probably covid positive')
    print()

    if(severity<3):
        print('It looks like the symptoms are mild\nhome quarantine')

    elif(severity>=3 and severity<6):
        print('The patient can get an admission in the general ward')

    else:
        print('The patient looks critical')

else:
    print('It looks like patient is not Covid positive')

print()

if(oxygen_level==1):
    print("Keep monitoring patient's oxygen level")
    
if(temperature_flag==1):
    print("Keep monitoring patient's body temperature")
    
    
    
    
    
#_____________________
    # 2
