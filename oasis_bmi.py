while True:
    try:
        
        Height = float(input("Please enter your height in inches: "))
        Weight = float(input("Please enter your weight in pound: "))
    except ValueError:

        print("Please provide valid input.")
        continue  
    else:
        if Height <= 0 or Weight <= 0:
            print("Your input must not be zero or less.")
            continue
        else:
            
            BMIIndex = round(Weight / (Height * Height) * 703, 2)

            print("Your Body Mass Index is: ", BMIIndex)

            if BMIIndex < 18.5:
                print(" You are Underweight.")
            elif BMIIndex <= 24.9:
                print("You are Normal.")
            elif BMIIndex <= 29.9:
                print("You are Overweight.")
            else:
                print("You are Obese.")
        break