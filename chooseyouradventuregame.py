name=input('Type yor name: ')
print('welcome',name,'to this escape adventure!!! ')
print('you entered a room ')

answer = input('There are 2 doors : red or blue? ').lower()
if answer == 'red':
    print('you entered the red room ')
    choice=input('you saw window and key: window or key? ').lower()
    if choice=='window':
        print('the window was locked ')
        jump=input('you have to break the window: yes or no? ').lower()
        if jump=='yes':
            print('you have jumped from window and escaped You Win!!! ')
        else:
            print('You stayed inside forever Game Over!!! ')
    else:
        print('you used the key and its a trap')
    
elif answer=='blue':
    print('you entered the blue room ')
    choice=input('you saw stairs and secret room : stairs or secret room? ').lower()
    if choice =='stairs':
        print('you ran upstairs and there is no escape!!! You Lose ')
    elif choice=='secret room': 
        output=input('there is tunnel and monster: tunnel or monster? ').lower()
        if output=='tunnel':
            print('In tunnel there are snakes you are bitten by snake ')
        elif output=='monster':
            fight=input('you have to fight or run? ').lower()
            if fight=='run':
                print('you ran and won the game ')
            else:
                print('monster defeated you and you lose')
        else:
            print('wrong choice...Game over!!!!')

    else:
        print('wrong choice...Game over!!!!')
else:
    print('wrong choice...Game over!!!!')

