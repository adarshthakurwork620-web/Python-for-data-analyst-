'''Take login attempts and print warning after 3 attempts.'''
correct_passward="adarsh1234"
for attempts in range(3):
    passward=input("Enter passward:")
    if passward==correct_passward:
        print("Login successful")
        break
    else:
        print("wrong passward")

    if attempts == 3:
            print(" Warning: Too many failed login attempts!") 
