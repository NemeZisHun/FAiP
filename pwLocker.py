#! python 3 
# Insecure pw vault

import pyperclip

pw={"email":'hdéfuhh377zt8ghw9uUHIUH97G(Zg(Zg(/v(',"bank":"uhf47rg832hfhhid28ozgt38qdiwh29h","porn":'it wasnt me mom, I swear'}
while True:
    print('Please type in the keyword for which you want to copy the password:')
    keyword = input()
    if keyword in pw.keys():
        pyperclip.copy(pw[keyword])
        print('Your password is on the clipboard, proceed')
    else:
        print('''There is no password for this keyword, do you want to add it?
        (Type in password to save, or leave it blank to exit)''')
        newPw = input()
        if newPw == '':
            print('Thank you for choosing, Matt Enterprises')
            break
        else:
            pw[keyword]=newPw
