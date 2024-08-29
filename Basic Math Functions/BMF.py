# START HERE

import math

# MAIN FUNCTION
def main():
    try:
        rtn_value = float(input("Enter a Decimal Number: "))

        sml_int = int(math.floor(rtn_value))  # Largest integer smaller than the number
        rnd_int = round(rtn_value)            # Nearest integer to the number
        lrg_int = int(math.ceil(rtn_value))   # Smallest integer larger than the number

        print("The floating number you entered is:             \n", rtn_value)
        # prints the floating number entered by the user.

        print("The largest integer smaller than the number is: \n", sml_int)
        # prints the integer smaller than the floating number.

        print("The nearest integer to the number is:           \n", rnd_int)
        # prints the nearest integer to the value, with halfway values rounded away from zero.

        print("The smallest integer larger than the number is: \n", lrg_int)
        # prints the integer greater than the floating number.

    except ValueError:
        # if input is not a valid floating-point number.
        print("OOPSIE!! You did not enter a valid floating number\n")

if __name__ == "__main__":
    main()
