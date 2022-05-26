def check_int(to_check):
    try:
        # Returns false if the code works, if it doesn't the try kicks in
        int(to_check)
        return False
    except ValueError:
        return True


while True:
    print(check_int(input("test: ")))
