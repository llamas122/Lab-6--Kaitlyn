def decode(password):
    # decodes the password by subtracting 3 from each digit
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
            char = 7
            new_password = new_password + str(char)
    return new_password


def encode_password(password):
    encoded_password = ""
    for num in password:
        if int(num) < 7:
            num = int(num) + 3
            encoded_password += str(num)
        elif int(num) == 7:
            num = 0
            encoded_password += str(num)
        elif int(num) == 8:
            num = 1
            encoded_password += str(num)
        elif int(num) == 9:
            num = 2
            encoded_password += str(num)
    return encoded_password


def main():
    condition = True
    while condition == True:
        print("Menu")
        print('-' * 13)


        print("1. Encode\n2. Decode\n3. Quit")
        print()

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print()
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif option == 3:
            break

if __name__ == "__main__":
    main()