import argparse,textwrap,logging
from src.passwordValidator import PasswordValidator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PasswordValidator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
            PasswordValidator
            Required Field: Password
            ''')
    )
    requiredNamed = parser.add_argument_group('Required Named Argument.')
    requiredNamed.add_argument("-p", help="Please enter the password", dest="password", required=True)
    args = parser.parse_args()

    password_validator = PasswordValidator(args.password)

    len_check = password_validator.length_check()
    digit_check = password_validator.isDigitAvaialble()
    space_check = password_validator.isSpaceAvailable()
    special_char_check = password_validator.isSpecialCharacterAvaialble()
    cap_character_check=password_validator.captialCharcterCheck()
    lower_character_check=password_validator.lowerCharcterCheck()
    if len_check==True and digit_check==True and space_check==True and special_char_check==True and cap_character_check==True\
            and lower_character_check==True:
        print("password provided is accepted")
    else:
        print("Length check passed" if len_check==True else len_check,
              "Digit check passed" if digit_check==True else digit_check,
              "space check passed" if space_check==True else space_check,
              "Special Character check passed" if special_char_check==True else special_char_check,
              "Capital Character check passed" if cap_character_check==True else cap_character_check,
              "Lower Character check passed" if lower_character_check==True else lower_character_check,sep='\n')
