"""
Week 1 Homework - Python Hello World Program

Bryan Phillips
03/09/24
SDEV 325 / 73780
"""

# Import statements
import datetime


def main():
    """

    :return:
    """

    # Display welcome message
    print("Hello, World!")

    # Prompt user for their name
    user_name = ''
    while not user_name.strip():
        user_name = input("What is your name? ").title()
    print("\nNice to meet you, " + user_name + "!")

    # Ask user they want to know the current date and time
    user_input = ''
    while user_input not in ["y", "n"]:
        user_input = input("Would you like to know the current date and time? (Y/N): ").lower()

    # Display the current date and time
    if user_input == "y":
        current_time = datetime.datetime.now().strftime("%I:%M%p")
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        print(f"The current time is {current_time} and the date is {current_date}.")

        # Ask the user if they want to divide two numbers
        user_divide_input = ''
        while user_divide_input not in ["y", "n"]:
            user_divide_input = input("\nWould you like to divide two numbers? (Y/N): ").lower()

        # Get user and input and check for non-zero division and if exists alert user and prompt
        # again for proper input
        if user_divide_input == "y":
            while True:
                try:
                    user_num1 = float(input("Enter the first number: "))
                    break
                except ValueError:
                    print("\nInvalid input! Please enter a number only.")
            while True:
                try:
                    user_num2 = float(input("Enter the second number: "))
                    if user_num2 != 0:
                        break
                    print("\nInvalid input! The divisor cannot be zero. Please try again.")
                except ValueError:
                    print("\nInvalid input! Please enter a number only.")

            # Display the result
            quotient = user_num1 / user_num2
            print(f"The result of dividing {user_num1} by {user_num2} is {quotient}.")

    # Display the goodbye message
    print("\nNice to meet you " + user_name + "!" + " Goodbye!")


if __name__ == "__main__":
    main()
