
class main():
    def mainMenu(self):
        print('1  :   BMI Calculator')
        print('2  :   Retirement Calculator')
        print('3  :   Distance Formula')
        print('4  :   Email Verifier')
        """while loop for continual menu options?"""
        try:
            choice = int(input("Select an application number: "))
        except ValueError:
            print('What you input was not an integer!')
            return 0
        if (isinstance(choice, int)):
            if (1 <= choice <= 4):
                if choice == 1:
                    print(choice, ": BMI Calculator chosen")
                if choice == 2:
                    print(choice, ": Retirement chosen")

                if choice == 3:
                    print(choice, ": Distance chosen")

                if choice == 4:
                    print(choice, ": Email chosen")
            else:
                print('That number is not an option: 1, 2, 3, or 4')
        else:
            print('Something went wrong.')
        return 0


main().mainMenu()
