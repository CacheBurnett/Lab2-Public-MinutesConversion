#In this lab I will create a code that will convert minutes into hours and minutes.

#Start
#Ask use for INPUT to enter the number of minutes
#Variable total_minutes will store the users input
#Calculate minutes into hours by dividing total_minutes by 60 #Processing
#Variable hours will store the WHOLE number of hours
#Calculate remaining minutes by dividing total_minutes by 60
#Variable remaining_minutes will store leftover minutes
#Message will display to user telling how many hours and minutes the entered number respresents
#END



def main():
    print("=== Minutes to Hours Converter===")

#Will get input from the user

    total_minutes = int(input("Enter the number of minutes: "))

#Will Perform mathematical calculations

    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

#Will Display the result

    print(f"{total_minutes} minutes is equal to {hours} hour(s) and {remaining_minutes} minute(s).")

#This will run the program
main()

