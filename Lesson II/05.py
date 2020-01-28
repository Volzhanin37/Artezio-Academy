password ='qwerty'
username = input('enter username: ')
while True:
    user_password = input('enter password: ')
    if user_password == password:
        print(f'Password for user: {username} is correct')
        break
    else:
        print(f'Password for user: {username} is incorrect')
        print("Please try again...")
