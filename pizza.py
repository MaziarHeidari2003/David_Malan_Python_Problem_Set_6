"""
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

"""

import sys
import csv
from tabulate import tabulate

def main():
  command_check()
  table = []
  try:

    with open(sys.argv[1]) as file :
      reader = csv.reader(file)
      for row in reader:
        table.append(row)

  except FileNotFoundError:
    sys.exit('File not found')

  
  print(tabulate(table[1:], headers=table[0], tablefmt= "grid"))



def command_check():
  if len(sys.argv) > 2 :
    sys.exit('Too many arguements')
  elif len(sys.argv) < 2 :
    sys.exit('Too few arguements')
  else:
    if not '.csv' in sys.argv[1]:
      sys.exit('Not a CSV file')  


if __name__ == '__main__' :
  main()      
