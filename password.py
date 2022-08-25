password = 'a123456'
number = 3
while number > 0:
    code = input('Please input your password:')
    if code == password:
        print('access suessfully')
        break
    else:
        number = number - 1
        print('The password you input is wrong, you have', number,'times for try!!')

        




    