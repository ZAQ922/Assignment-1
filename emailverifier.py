import re

class emailVerifier():

    def verifyemail(email):

        useremail     = re.search(r'(.*)@(.*)\.(.*)', email, re.I)
        useremailver1 = re.search(useremail.group(1), email, re.I)
        removespecialchar = re.compile('[\[{}()\]\\\*]')
        a = removespecialchar.sub('', useremail.group(1))
        b = removespecialchar.sub('', useremail.group(2))
        c = removespecialchar.sub('', useremail.group(3))

        if useremail.group:
            if (len(c) <= 3):
                print (a, b, c)
            else:
                print ("Invalid domain extention: must be three letters or less")
        else:
            print ("Not a valid email")
