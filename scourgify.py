import sys
import csv

def main():
  command_check()
  try:
    with open(sys.argv[1]) as file :
      reader = csv.DictReader(file)
      for row in reader:
         split_name = row['name'].split(',')
         print(split_name)     


  except FileNotFoundError:
    sys.exit('File not found')





def command_check():
  if len(sys.argv) > 3 :
    sys.exit('Too many arguements')
  elif len(sys.argv) < 3 :
    sys.exit('Too few arguements')
  else:
    if not '.csv' in sys.argv[1] or not '.csv' in sys.argv[2]:
      sys.exit('Not a CSV file')  




if __name__ == '__main__' :
  main()      