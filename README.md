Email Validator in Python
This is a simple Python script that validates an email address based on a set of predefined rules. It checks for format correctness such as length, placement of special characters, and character restrictions.

Features
Ensures the email:

Is at least 6 characters long

Starts with an alphabet

Contains exactly one '@' symbol

Ends with a domain extension like .com or .in

Does not contain whitespace

Does not contain uppercase letters

Does not contain invalid special characters

Validation Rules
The script follows these validation steps:

Minimum Length: Email must be at least 6 characters long.

Start Character: The first character must be a lowercase alphabet.

@ Symbol: Must contain exactly one '@' symbol.

Domain Check: Must end with .com or .in (i.e., the '.' must be at the 3rd or 4th position from the end).

Character Rules:

No whitespace characters

No uppercase letters

Only allowed special characters: _, ., and @

Example Output
bash
Copy
Edit
Enter your Email  : John.Doe@example.com
Wrong Email 5

Enter your Email  : john.doe@example.com
Right email
How to Use
Clone the repository or download the script.

Run the script using Python 3:

bash
Copy
Edit
python email_validator.py
Enter an email when prompted to check its validity.

File Structure
bash
Copy
Edit
.
├── email_validator.py  # Main validation script
└── README.md           # Project documentation
License
This project is licensed under the MIT License.
