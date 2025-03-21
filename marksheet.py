  
  # Marksheet 
  # Function 
def marksheet(Name,Englis,Math,Science,Sindhi,Computer):
    total= Englis + Math + Science + Sindhi + Computer
    percentage = total / 500 * 100
    print(f"Name :{Name}\nTotal Marks : {total}\nPercentage:{percentage} %")

# Conditions
    if percentage >=90:
        print("Grade A")
        print("Excellent")
        print("You are a 1st marks holder")
        print(" Result :Pass")

    elif percentage >=80:
        print("Grade B")
        print("Very Good")
        print("Result : Pass")

    elif percentage >=70:
        print("Grade C")
        print("Good")
        print("Result : Pass")

    elif percentage >=60:
        print("Grade D")
        print("Average")
        print("Result : Pass")

    elif percentage >=50:   
        print("Grade E")
        print("Just Pass")
        print("Result : Pass")

    else:
        print("Grade E")
        print("Fail")
        print("Result : Fail")
marksheet("Ahmed",90,80,70,60,50)
marksheet("Ali",80,70,60,50,40)
#marksheet("Usman",70,60,50,40,30)
#marksheet("Waleed",60,50,40,30,20)
#marksheet("Farooque",50,40,30,20,10)




        
        
        
        
        
        





