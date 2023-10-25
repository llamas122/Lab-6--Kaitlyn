def decode(password):
    new_password = ''
    for char in password:
        if int(char) > 2:
            char = int(char) - 3
            new_password = new_password + str(char)
        elif int(char) == 2:
            char = 9
            new_password = new_password + str(char)
        elif int(char) == 1:
            char = 8
            new_password = new_password + str(char)
        else:
            char = 9
            new_password = new_password + str(char)
    return new_password

