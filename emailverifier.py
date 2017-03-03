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
                if (len(c) <= 3):
                    print(email, " is a valid email!")
                    loop4 = False
                    return True
                else:
                    print(c, "is and invalid domain extention: it must be three letters or less.")
                    loop4 = False
                    return False

        except:
                print(email, "is not a valid email")
                return False
