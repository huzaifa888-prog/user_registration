print('''
         AUTHENTICATION SYSTEM USING PYTHON

         1 Press User rigestration.
         
         2 Press Login.
         
         3 Press Show All the use.
         
         4 Press quite.
''')
user_registration = []

for i in range(100):
    choice = int(input('Enter the choice: '))
    if choice == 1:
        name = input('Enter Your Full name: ').lower().strip()
        if name:
            email = input('Enter Your email: ').strip().lower()
            if email.endswith('@gmail.com'):
                gender = input('Enter Your gender: ').lower().strip()
                if gender == "male" or gender == "female":
                    password = input('Enter Your Password: ')
                    confirm_password = input('Re-again password: ')
                    if password == confirm_password:
                        user_registration.append({
                            "Name": name,
                            "Email": email,
                            "Gender": gender,
                            "Password": password
                        })
                        print(f'\n\n\tMr/Mrs Your registration is Successfully\n {user_registration}')
                    else:
                        print('Invalid Password. Try Again..!')
                else:
                    print('please Confirm Your Gender..!')
            else:
                print('Invalid Email.. Try again...!')
        else:
            print('Require Full name..!')
    if choice == 2:
        email = input('Enter Your Email: ').lower()
        password = input('Enter Password: ')
        for user in user_registration:
            if user[email] == user_registration["email"] and user["password"] == user_registration[password]:
                print('\n\tLogin Successful..!')
            else:
                print('Invalid Password..! Try Agian')
    if choice == 4:
        print('Thanks For using This Portal..!')
        break