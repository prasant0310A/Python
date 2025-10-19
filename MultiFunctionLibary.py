class multiFunction:  
    def subField():
        list1 = ['Machine learning', 'Neural Network', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are:")
        for name in list1:
            print(name)
        # return 
        
    def oddEven():
        num1 = int(input("Enter a number"))
        print("Enter a number:", num1)
        if (num1 % 2 == 0):
            print(f"{num1} is Even number")
        else:
            print(f"{num1} is Odd number")
        return
         
    def Elegible():
        gender = input("Enter your Gender:")
        age    = int(input("Enter your age:"))
        print("Your Gender:",gender)
        print("Your age:",age)
        if (gender == "Male" or "male" and age < 21):
            print("You are not eligible for marriage")
        elif (gender == "Female" or "female" and age < 18):
            print("You are not eligible for marriage")
        else:
            print("You are eligible for marriage")
       # return 

    def percentage():
        sub1 = int(input("Enter your Subject 1 marks:"))
        sub2 = int(input("Enter your Subject 2 marks:"))
        sub3 = int(input("Enter your Subject 3 marks:"))
        sub4 = int(input("Enter your Subject 4 marks:"))
        sub5 = int(input("Enter your Subject 5 marks:"))
        print("Subject1=",sub1)
        print("Subject2=",sub2)
        print("Subject3=",sub3)
        print("Subject4=",sub4)
        print("Subject5=",sub5)
        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total/500) * 100
        print("total :",total)
        print("Percentage :",percentage)

    def triangle_perimeter(side1,side2,side3):
        return side1 + side2 + side3

    def triangle_area(base, height):
        return (0.5 * base * height)