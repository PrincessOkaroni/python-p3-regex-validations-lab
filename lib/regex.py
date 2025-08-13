import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!
# Name: Capitalized words, may include hyphen or apostrophe
name = r"^[A-Z][a-z]+(?:[-'][A-Z][a-z]+)*$"
name_regex = re.compile(r"^[A-Z][a-z]*(?:'[A-Z][a-z]*)?(?:[ -][A-Z][a-z]*)*$")


# Phone: 3 formats - 10 digits, dash format, parentheses format
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# Email: lowercase letters, optional dot/number, then @, domain, .tld
email_address = r"^[a-z]+(?:\.[a-z0-9]+)*@[a-z]+\.[a-z]+$"
email_regex = re.compile(email_address)
