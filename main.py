# Take email input from user
email = input("Enter your Email  : ")

# Initialize flags
k = 0  # flag for whitespace
j = 0  # flag for uppercase letter
d = 0  # flag for special/invalid characters

# Check if email length is at least 6 characters
if len(email) >= 6:

    # Check if the first character is an alphabet
    if email[0].isalpha():

        # Check if '@' is present and only once
        if ("@" in email) and (email.count("@") == 1):

            # Check if '.' is at 3rd or 4th position from the end (e.g. .com or .in)
            if (email[-4] == ".") or (email[-3] == "."):

                # Loop through each character in the email
                for i in email:

                    # Check if there is any whitespace
                    if i.isspace():
                        k = 1

                    # Check if character is an alphabet
                    elif i.isalpha():

                        # If it's an uppercase letter, set flag
                        if i == i.upper():
                            j = 1

                    # If character is a digit, it's okay
                    elif i.isdigit():
                        continue

                    # Allow only these special characters: _, ., @
                    elif i == "_" or i == "." or i == "@":
                        continue

                    # Any other special character is invalid
                    else:
                        d = 1

                # If any flag is raised, it's an invalid email
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Right email")

            else:
                print("Wrong Email 4")  # '.' not in the correct position
        else:
            print("Wrong Email 3")  # '@' missing or used more than once
    else:
        print("Wrong Email 2")  # Email doesn't start with an alphabet
else:
    print("Wrong Email 1")  # Email too short
