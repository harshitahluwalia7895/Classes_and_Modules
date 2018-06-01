class Temperature:

    def convertFahrenheit(self, celcius):
        return (((9 / 5) * (celcius)) + 32)

    def convertCelsius(self, fahrenheit):
        return ((fahrenheit - 32) * (5 / 9))


t = Temperature()
ch = 'y'
while ch == 'y':
    c1 = input("Enter 1 to Convert Celcius to Fahrenheit\nEnter 2 to convert Fahrenheit to Celcius\n")
    if c1 == '1':
        c = float(input("Enter temperatur in Celcius"))
        f = t.convertFahrenheit(c)
        print("Temperature in Fahrenheit=", f)
    elif c1 == '2':
        f = float(input("Enter temperatur in Fahrenheit"))
        c = t.convertCelsius(f)
        print("Temperature in Celcius=", c)
    else:
        print("Wrong Input")

    ch = input("Do you want to do more conversions?? y//n: ")
print('Thankyou !!!')