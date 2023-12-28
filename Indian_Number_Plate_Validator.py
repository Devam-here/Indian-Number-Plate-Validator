import json
#THIS IS THE LIST OF STATE CODES.
STATE_CODES = ("AN", "AP", "AR", "AS", "BR", "CH", "DN", "DD", "DL", "GA", "GJ", "HR", "HP", "JK", "KA", "KL", "LD", "MP", "MH", "MN", "ML", "MZ", "NL", "OR", "PY", "PN", "RJ", "SK", "TN", "TR", "UP", "WB")


def main():
    #THIS TAKES THE NUMBER PLATE INPUT FROM THE USER.
    number_plate = input("Enter the vehicle number plate: ").upper().strip()

    if is_valid(number_plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(number_plate):
    return starts_with(number_plate) and dc_check(number_plate) and rv_check(number_plate) and np_check(number_plate)

#THIS FUNCTION CHECKS THE STATE CODE OF THE NUMBER PLATE.
def starts_with(number_plate):
    state_code = number_plate[0:2]
    if not state_code.isalpha() or state_code not in STATE_CODES:
        print("ERROR MESSAGE: ENTER CORRECT STATE CODE!")
        return False
    return True

#THIS FUNCTION CHECKS THE DISTRICT CODE OF THE NUMBER PLATE.
def dc_check(number_plate):
    with open('district_code_list.json', 'r') as file:
        district_codes = json.load(file)
        state_code = number_plate[0:2]
        district_code = number_plate[2:4]
        if not district_code.isnumeric() or district_code not in district_codes.get(state_code, []):
            print("ERROR MESSAGE: ENTER CORRECT DISTRICT CODE!")
            return False
        return True

#THIS FUNCTION CHECKS THE CORRECT FORMAT OF VARIABLES IN NUMBER PLATE.
def rv_check(number_plate):
    variable = number_plate[4:6]
    if not variable.isalpha() or not 1 <= len(variable) <= 2:
        print("ERROR MESSAGE: ENTER CORRECT VARIABLES!")
        return False
    return True

#THIS FUNCTIONI CHECKS THE CORRECT FORMAT OF NUMBER PLATE.
def np_check(number_plate):
    number_part = number_plate[6:10]
    if not number_part.isnumeric() or not len(number_part) == 4:
        print("ERROR MESSAGE: Enter CORRECT NUMBER PLATE!")
        return False
    return True

    

if __name__ == "__main__":
    main()
