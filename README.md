# Email Validation Script in Python

This repository contains a simple Python script that validates an email address based on custom rules. It uses basic string and character checks without relying on external libraries.

## 🔍 Features

- Ensures the email:
  - Is at least 6 characters long
  - Starts with an alphabet
  - Contains exactly one `@` symbol
  - Ends with a domain like `.com` or `.in` (i.e., a `.` at the 3rd or 4th position from the end)
  - Does not contain:
    - Whitespaces
    - Uppercase letters
    - Invalid special characters

## ✅ Allowed Special Characters

- Underscore (`_`)
- Dot (`.`)
- At symbol (`@`)

## ❌ Invalid Email Examples

- `Example@domain.com` – contains uppercase letters
- `example domain@com` – contains whitespace
- `example@domain!.com` – contains invalid special characters
- `ex@co` – less than 6 characters
- `1example@domain.com` – does not start with an alphabet
- `example@domain@com` – more than one `@` symbol

## 💡 Usage

Run the script using any Python 3 interpreter:

```bash
python email_validator.py
