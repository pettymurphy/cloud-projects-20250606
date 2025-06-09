def greeting(time_of_day, name):
    print("Good" , time_of_day + ",", name + "!")
time = input("Enter the time of day(morning, afternoon, evening):") # Ask the user for time of day (e.g., morning, afternoon, evening)
person = input("Enter your name:")

    
greeting(time, person)# Call the function using their input