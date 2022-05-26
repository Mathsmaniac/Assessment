# Check int function
def check_int(to_check):
    # Uses isinstance to determine variable type
    if isinstance(to_check, int):
        return False
    # returns true if it hasn't returned false
    return True


# while true input for testing purposes
while True:
    print(check_int(input("test: ")))
