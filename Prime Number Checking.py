value = int( input("Please enter value : ") )
if value < 1:
    print( value," not a prime number" )
else:
    for digit in range( 2 , value ):
        if value % digit == 0:
            print( "not a prime number" )
            break
        else:
            print("it is prime number")

lower_Number = 100
upper_Number = 200
for number in range( lower_Number , upper_Number + 1 ):
    if number > 1:
        for i in range( 2 , number ):
            if number % i == 0:
                break
        else:
            print(number)