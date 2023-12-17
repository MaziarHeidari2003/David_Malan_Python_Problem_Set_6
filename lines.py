import sys


def main():
  check_command_line()

  try:
    file = open(sys.argv[1],'r')
    lines = file.readlines()


  except FileNotFoundError:  
    sys.exit('The file doesnt exist')
  count_lines = 0
  for line in lines:
    if check_if_comment_or_empty_line(line) == False :
      count_lines += 1

  print(count_lines)



def check_if_comment_or_empty_line(line):
  if line.isspace():
    return True
  if line.lstrip().startswith('#'):
    return True
  return False



def check_command_line():
  if len(sys.argv) > 2 :
    sys.exit('Too few command_line arguements')
  elif len(sys.argv) < 2 :
    sys.exit('Too many commant_line arguements')
  else:
    #if sys.argv[1][-3:] != '.py' :
    if not '.py' in sys.argv[1]:  
      sys.exit('Not a Python file')  


if __name__ == '__main__' :
  main()
