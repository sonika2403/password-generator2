import random
import string

#The elements that include the below choices: uppercase, lowercase, ascii letters, name and DOB
def generate_password(length=12, include_name=False, include_dob=False):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    #include the letters from your name if needed in the password
    if include_name:
        name = input("Enter your name: ")
        password += ''.join(random.choice(name) for _ in range(min(4, len(name))))

    #including the numbers from your dob if needed in the password
    if include_dob:
        dob = input("Enter your date of birth (YYYYMMDD): ")
        password += ''.join(random.choice(dob) for _ in range(min(6, len(dob))))

    return password

#generating it
def main():
    print("Password Generator")
    print("Generate secure and feasible random passwords over here!")

    #to input all the necessary elements needed to generate the password
    length = int(input("Enter the desired length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    include_name = input("Include your name in the password? (y/n): ").lower() == 'y'
    include_dob = input("Include your date of birth in the password? (y/n): ").lower() == 'y'

    #printing the generated passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(length, include_name, include_dob)
        print(password)

#main module for the code to get executed
if __name__ == "__main__":
    main()
