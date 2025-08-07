
print('Welcome to the User Registration System!')
username = input('Enter your username: ')
password = input('Enter your password: ')

print('Your account has been created successfully!')
print(f'Welcome, {username}! You can now log in with your credentials.')
print('Login Now.')

username2 = input('Enter your username : ')
password2 = input('Enter your password : ')

if username == username2 and password == password2:
    print('Login successful!')
else:
    print('Login failed! Please check your username and password.')