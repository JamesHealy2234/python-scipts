import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-display")

args = parser.parse_args()



# This will return an object containing attributes, where the attributes correspond to the names of the arguments passed to the script.
print(args.display)

