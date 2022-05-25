"""
In this version, I simply made the function and made sure it worked
"""


def check_not_blank(input_):
    if input_.isspace() or input_ == "":
        return "blank"
    else:
        return "not blank"


# Get test input
while True:
    print(check_not_blank(input("Test: ")))
