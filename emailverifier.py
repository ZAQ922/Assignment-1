import re

class emailVerifier():

    def verifyemail(email):

        try:
            useremail = re.search(r'(.*)@(.*)\.(.*)', email, re.I)
            useremailver1 = re.search(useremail.group(1), email, re.I)

            removespecialchar = re.compile('[\[{}()\]\\\*]')

            a = removespecialchar.sub('', useremail.group(1))

            b = removespecialchar.sub('', useremail.group(2))

            c = removespecialchar.sub('', useremail.group(3))

            if not ((re.match(('[\[{}()\]\\\*]'), email))):
                print("here55")
                if (len(c) <= 3):
                    print(email, " is a valid email!")
                    loop4 = False
                else:
                    print("Invalid domain extention: must be three letters or less")
                    loop4 = False

        except:
                print("Not a valid email")
