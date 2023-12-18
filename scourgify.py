import sys
import csv

def main():
  command_check()
  output = []
  try:
    with open(sys.argv[1]) as file:
      reader = csv.DictReader(file)
      for row in reader:
        split_name = (row['name']).split(',')
        output.append({'first':split_name[1].lstrip() , 'last':split_name[0] , 'house': row['house'].lstrip()})  
  except FileNotFoundError:
    sys.exit('File not found')


  with open(sys.argv[2], 'w') as file :
    writer = csv.DictWriter(file, fieldnames = ["first", "last" , "house"])
    writer.writerow({'first': 'first', 'last':'last', 'house': 'house'})
    for row in output :
      writer.writerow({'first':row['first'] , 'last':row['last'] , 'house': row['house']}) 





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