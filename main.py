import random

strengthPrompt = '''
How strong should you're password be: Type <1> for 'Weak'
                                      Type <2> for 'Moderate'
                                      Type <3> for 'Strong'\n>>>'''
numCharPrompt = "What length do you want you're password to be:\n>>>"

# a function to ask and validate strength
def askStrength():
    while True:
        strength = input(strengthPrompt)
        try:
            strength = int(strength)
            if not (strength == 1 or strength == 2 or strength == 3):
                print(f"Please enter a number that is either 1,2 or 3")
            else:
                return strength
                break
        except:
            print(f"Please enter a number you entered {strength}")


def askCharNum():
    while True:
        charnum = input(numCharPrompt)
        try:
            charnum = int(charnum)
            if not (charnum > 0):
                print(f"please enter a valid positive count")
            else:
                return charnum
                break
        except:
            print(f"Please enter a count you entered {charnum}")


weakValues = []
j = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
for every in j:
    weakValues.append(every)

moderateValues = []
k = '1234567890'
for every in j:
    moderateValues.append(every)
for every in k:
    moderateValues.append(every)

strongValues = []
l = '!@#$%&<>?'
for every in l:
    strongValues.append(every)
for every in j:
    strongValues.append(every)
for every in k:
    strongValues.append(every)


strength = askStrength()
numchar = askCharNum()

while True:
    if strength == 1 and numchar >= 5:
        passwordRaw = random.choices(weakValues, k=numchar)
        password = ''
        for every in passwordRaw:
            password = password + every
        break
    elif strength ==1 and numchar < 5:
        print(f'Weak passwords must have a maximum of 5 characters you gave{numchar}')
        numchar = askCharNum()

    elif strength == 2 and numchar >= 7:
        passwordRaw = random.choices(moderateValues, k=numchar)
        password = ''
        for every in passwordRaw:
            password = password + every
        break
    elif strength == 2 and numchar < 7:
        print(f'Weak passwords must have a maximum of 5 characters you gave{numchar}')
        numchar = askCharNum()

    elif strength == 3 and numchar >= 10:
        passwordRaw = random.choices(strongValues, k=numchar)
        password = ''
        for every in passwordRaw:
            password = password + every
        break
    elif strength == 3 and numchar < 10:
        print(f'Weak passwords must have a maximum of 5 characters you gave{numchar}')
        numchar = askCharNum()
    else:
        print('Oh Shit!!!you should not be here\nRESTART AND TRY AGAIN')


try:
    print('This Is Your Password: ' + password + '\nDo not forget it and\nDont show it to anyone')
except:
    print("i dont even know why you're reding this")