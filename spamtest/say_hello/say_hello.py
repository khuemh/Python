def greeting(time):
    if time == "morning":
        print("Good morning..!")
    elif time == 'afternoon':
        print('Good afternoon..!')
    elif time == 'evening':
        print('Good evening..!')


time = input('Time input? ')
greeting(time)
