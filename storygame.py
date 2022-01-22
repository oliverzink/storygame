
import time
import random

mmm = random.randint(1, 500)
print('\nEntering data log',mmm,'\n...\n')
time.sleep(2)
print('Welcome. Please state your name for the record.')
name = input('Enter name: ')
print('\nProcessing...\n')
time.sleep(4)
print('Good to see you remember. Welcome back '+ name)
print('\n...\n')
# time.sleep(2)
# print('\nAnd '+name+', who do you dislike most in this world?')
# print('if you have no adversion, simply press enter')
# bad = input('Enter data: ')
# print('\nProcessing...\n')
# time.sleep(3)
# print('And who do you love most in this world? ')
# good = input('Enter data: ')
# print('\nProcessing...\n')
time.sleep(3)
print('* Please note subject seems to be in sufficient cognitive health *')
time.sleep(3)
print('\n* No visible risk of containment breach or subject awareness *\n')
time.sleep(4)
print("* Confirmed... lets max it out at 9.77... *")
time.sleep(4)
print('\nApplying nueral dampening combatants...')
time.sleep(3)
print('\nInitializing ionic chamber...')
time.sleep(4)
print('\nPreparing hourglass procedure...\n')
time.sleep(4)
print('Enjoy your stay '+name+' we will be seeing you soon')
time.sleep(5)
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
print('---------------------------------------------------------')


inloop = False

def choices2(q, x):
    exitw = False
    while exitw == False:
        choice = input('Enter: ')
        if q in choice:
            return q
        elif x in choice:
            return x

def choices3(q, x, y):
    exitw = False
    while exitw == False:
        choice = input(': ')
        if q in choice:
            return q
        elif x in choice:
            return x
        elif y in choice:
            return y

def choices4(q, x, y, z):
    exitw = False
    while exitw == False:
        choice = input(': ')
        if q in choice:
            return q
        elif x in choice:
            return x
        elif y in choice:
            return y
        elif z in choice:
            return z

# def choosing(a, q, x, y, z):
#     b = choices(q, x, y, z)
#     print(b)
#     if b == 'exit':
#         a = ''
#         return a
penlistother = ['Well, you better get your shit together, Its your big day at work. Dont you remember?', 'Shut up '+name+' and go to work', 'You make me laugh', 'If you dont shut your trap and get your arse off that couch Im gonna flip my shit','Honestly '+name+' I think its time we begin to consider a divorce','That might just be the best damn thing youve ever said to me', 'Right back atcha buddy','Ah nevermind, you dont get it','thats interesting...']
penlisthi = ['hi','hello','morning','hey']
penlisthow = ['how are']
penlistsim = ['simulation','matrix','game']
penlistbye = ['bye', 'later']

def askpenny():
    e = False
    while e == False:
        askpen = input('Talk to Penny: ')
        penprint = False
        askp = askpen.lower()
        for term in penlisthi:
            if term in askp:
                print('Good morning '+name+', glad your awake')
                penprint = True
        for term in penlisthow:
            if term in askp:
                print('Im doing well '+name)
                penprint = True
        for term in penlistbye:
            if term in askp:
                print('Goodbye '+name+' have a great day at work')
                penprint = True
                e = True
        for term in penlistsim:
            if term in askp:
                print(name+'... never mention that again. Please... I dont want to get reset.')
                print('\nOh God! not again plea-\n')
                time.sleep(4)
                print('* penny.ex rebooting... please stand by *\n')
                time.sleep(5)
                print('Ah, good morning honey. Ready for your big day at work?')
                penprint = True
        if 'who' in askp:
            print('Honey, its me, Penny... Im worried about you. Have you been drinking?')
        elif 'where' in askp:
            print('Your lazy ass in on the damn couch, thats where. Now get up and get ready for work!')
        elif 'code' in askp:
            print('Your so forgetful '+name+', its 1234')
        elif 'log' in askp or 'toilet' in askp:
            print('How dare you. I would never do such a thing. That mustve been you...\nBy the way, have you seen my hair spray?')
        elif askp == 'exit':
            e = True
            #im high asf but try to understand that below I have a list of shit that I wanna cross check with the user input. Then we for loop through the list and check the user input against each one. then you could just
            #do i in range(len(list)) and basically just check list[i] in userinput or not. if not then moves on, if so, delivers the output. could match tons of shit up for this and would need to do one for each point.  

        
        elif penprint == False:
            pennum = random.randint(0,9)
            if pennum == 9:
                print('\nRegional error 489... ')
                time.sleep(2)
                print('\nWhat the fuck is happening...')
                time.sleep(2)
                print('\nWhere am I?\n\nWho the hell are you?')
                time.sleep(2)
                print('\n* system rebooting... *')
                time.sleep(4)
                print('\nHahaha '+name+' your the best. Have a great day at work.')
            else:
                print(penlistother[pennum])
gameover = False
inventory = []
# while gameover == False:

print(name+'... '+name+'! Wake up! You need to leave for work in ten minutes!\n')
b = 'exit'
while b == 'exit':
    print('\n- Go to the kitchen\n- Talk to the lady\n- Go to the bathroom\n- Go through the front door')
    a = choices4('kitchen', 'bathroom', 'talk', 'door')
    while a == 'kitchen':
        print('\n~ you look around the kitchen ~\n')
        print('- Open the fridge\n- Open the drawer\n- Exit the kitchen')
        b = choices3('fridge','drawer','exit')
        if b == 'exit':
            break
        while b == 'drawer':
            if 'lighter' in inventory:
                print('\nnothing else to see here '+name)
                break
            print('\n~ its locked. enter the four digit passcode (or exit) ~')
            code = ''
            while code != 'exit' and code != '1234':
                code = input(': ')
            if code == '1234':
                print('\nUnlocked...\n')
                print('Inside the drawer you see a lighter and a bunch of junk\n')
                print('- Grab the lighter\n- Exit')
            if code == 'exit':
                break
            c = choices2('lighter','exit')
            if c == 'lighter':
                print('\nlighter added to inventory!')
                inventory.append(c)
                # print(inventory)
                break
            if c == 'exit':
                break    
        while b == 'fridge':
            if 'carrot' in inventory:
                print('\nnothing else to see here '+name)
                break
            print('\n~ you open the fridge. theres some leftover turkey and a carrot. ~\n')
            print('- Grab the carrot\n- Exit')
            c = choices2('carrot','exit')
            if c == 'carrot':
                print('\ncarrot added to inventory!')
                inventory.append('carrot')
                # print(inventory)
                break
            if c == 'exit':
                break      
    while a == 'bathroom':
        print('\n~ you look around the bathroom ~\n')
        print('- Check out the toilet\n- Open the sink cabinet\n- Exit the bathroom')
        b = choices3('toilet','cabinet','exit')
        if b == 'exit':
            break
        while b == 'cabinet':
            if 'hair spray' in inventory:
                print('\nnothing else to see here '+name)
                break
            print('\n~ you open the cabinet. you see some trash and a can of hair spray ~\n')
            print('- Grab the hair spray\n- Exit')
            c = choices2('hair','exit')
            if c == 'hair':
                print('\nhair spray added to inventory!')
                inventory.append('hair spray')
                # print(inventory)
                break
            if c == 'exit':
                break      
        while b == 'toilet':
            if 'plunger' in inventory:
                print('\ntrust me, you dont wanna go back there '+name)
                break
            print('\n~ you inspect the toilet. there appears to be a log in the bowl ~\n')
            print('- Pick up the plunger\n- Exit out of there ASAP')
            c = choices2('plunger','exit')
            if c == 'plunger':
                print('\n'+c+' added to inventory!')
                inventory.append(c)
                # print(inventory)
                break
            if c == 'exit':
                break
        
    while a == 'talk':
        g = askpenny()
        break
        
