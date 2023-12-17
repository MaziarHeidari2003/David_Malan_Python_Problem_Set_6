"""
en so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""



import sys

def main():
  check_command_line()
  file = open(sys.argv[1],'r')
  lines = file.readlines()
  count_lines = 0
  for line in lines:
    if check_space_or_comment(line) == False :
      count_lines += 1
  print(count_lines)      



def check_command_line():
  if len(sys.argv) > 2 :
    sys.exit('Too many arguements')
  elif len(sys.argv) < 2 :
    sys.exit('Too few arguements')
  else:
    if not '.py' in sys.argv[1]:
      sys.exit('Not a Python file')  

def check_space_or_comment(line):
    if line.lstrip().startswith('#'):
      return True
    if line.isspace():
      return True
    return False


if __name__ == '__main__' :
  main()