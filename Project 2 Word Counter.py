# Code to display the welcome message
def display_welcome():
    print("Welcome to Project 2")
    print("Greetings from Ashmit")

# Code to get the user's name
def get_user_name():
    name = input("Enter the name of the user: ")
    print(f"Welcome, {name}!")
    return name

# Code to enter and analyze text input
def analyze_text(input_text):
    word_count = len(input_text.split())
    char_count = len(input_text)
    print(f"The total number of words in the above text is: {word_count}")
    print(f"The total length of the above text is: {char_count}")

# Code to demonstrate error handling
def demonstrate_error_handling():
    try:
        print("undefined_variable")  # This will trigger a NameError
    except NameError:
        print("An error occurred: A variable is not defined.")

# Code to run the program
def main():
    display_welcome()
    get_user_name()
    input_text = input("Enter the text: ")
    analyze_text(input_text)
    demonstrate_error_handling()

# Run the program
main()

