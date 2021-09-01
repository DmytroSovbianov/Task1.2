#!/usr/bin/env python3

# Import modules

import os
import sys

# Define parsing function with string input and string return

def lineParser(str):

  parsedLine = str
  i = 1 # iterator for our happy three symbols. 

  while parsedLine.find(" ") != -1 : 
    if i == 1:
      parsedLine = parsedLine.replace(" ","_",1) # changes only first char
      i +=1
    elif i == 2:
      parsedLine = parsedLine.replace(" ","-",1)
      i +=1
    elif i == 3:
      parsedLine = parsedLine.replace(" ","/",1)
      i = 1
    else:
      print("Internal parse method error") 
      break;

  return parsedLine

# Main function. Script receives file as an argument and creates another file 'parsed' with parsed lines

def main():
  try:
    readFile = str(sys.argv[1]) # our file as an arg

  except Exception as e:
    print('File not specified, or something else')
    exit()

# Check if input file exists

  if not os.path.exists(readFile):
    print('File doesnt exist, or input is invalid')
    exit()

# Open target file and read lines. After iterate through lines, parse them and write to a newly created file

  with open(readFile, 'r') as reader:
    lines = reader.readlines()
  with open('parsed', 'w') as writer:
    for line in lines:
      writer.write(lineParser(line))

  print('Parsed file is located: ', os.path.abspath('parsed'))

if __name__ == '__main__':
  main()
