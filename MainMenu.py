

def main():
    """while loop for continual menu options?"""
    print('1  :   BMI Calculator')
    print('2  :   Retirement Calculator')
    print('3  :   Distance Formula')
    print('4  :   Email Verifier')
    choice = input("Select an application number: ")

    if isinstance(choice, int) and (1 <= choice <= 4):
        if choice is 1:
            print(choice, ": BMI Calculator chosen")
        if choice is 2:
            print(choice, ": Retirement chosen")
        if choice is 3:
            print(choice, ": Distance chosen")
        if choice is 4:
            print(choice, ": Email chosen")
    else:
        print('Please choose a number from 1 to 4.')


if __name__ == 'main__':
    main()
