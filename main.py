# This is a short script to allow a user to convert m/s to knots
# And vice versa.
#
# User should enter the value they want to convert followed
# kt if it's in knots or ms if it's meters per second.
#
# User can enter 'quit', to exit out


print('\n\n Hello, this is a script to convert knots to meters per second.')
print('If you would like to quit the script, please enter in "quit"')

while True:

    units = input("Enter the units to convert from (knots or m/s): ")

# Exit statement to quit the program
    if units == 'quit':
        break

# Checks for correct input by user
    if units not in ['knots', 'm/s']:
        print('Sorry please enter the correct units \n \n')
        continue

# Computes knots to meter per second
    if units == 'knots':
        try:
            input_value = float(input("Please enter your windspeed in knots: "))
        except ValueError:
            print("Sorry, please enter in an integer or a float \n \n")
            continue
        output = input_value * 0.514444444

# Computes meters per second to knots
    if units == 'm/s':
        try:
            input_value = float(input("Please enter your windspeed in m/s: "))
        except ValueError:
            print("Sorry, please enter in an integer or a float \n \n")
            continue
        output = input_value * 1.94384

# Set the units coverted to for the output message.
# Picks the opposite of whatever the user inputted.
    converted_units = ['knots', 'm/s']
    converted_units.remove(units)

    print('%f %s is %f %s \n \n' % (input_value, units,
                                    output, converted_units[0]))
