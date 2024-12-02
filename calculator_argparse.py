import argparse 

ap = argparse.ArgumentParser()


ap.add_argument("-a" , "--first_operand", required=True, help="first operand")

ap.add_argument("-b" , "--second_operand",required=True,help="second operand")
## this is the method

args = vars(ap.parse_args())
## call the function
a = int(args['first_operand']) 
b = int(args['second_operand'])

print("Sum is {}".format(a+b))
print("Sub is {}".format(a-b))
print("Div is {}".format(a/b))
print("Mul is {}".format(a*b))