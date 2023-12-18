"""
en so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""


import sys

def main():
  check_command_line()
  file = open(sys.argv[1])
  lines = file.readlines()
  counter_lines = 0
  for line in lines:
    if check_comment_or_space(line) == False :
      counter_lines += 1
  print(counter_lines)    


def check_comment_or_space(line):
  if line.startswith('#'):
    return True
  if line.lstrip().isspace():
    return True
  return False
      

def check_command_line():
  if len(sys.argv) > 2 :
    sys.exit('Too many arguements')
  elif len(sys.argv) < 2 :
    sys.exit('Too few arguements')
  else:
    if not '.py' in sys.argv[1]:
      sys.exit('Not a Python file')  

if __name__ == '__main__' :
  main()