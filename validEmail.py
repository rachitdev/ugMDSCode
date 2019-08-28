import re

# Make a regular expression for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = input()


def checkmail(email):
    if re.search(regex, email):
        print("valid")
    else:
        print("invalid")


checkmail(email)
