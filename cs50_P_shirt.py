import sys
from PIL import Image,ImageOps
from os.path import splitext



def main():
  check_comman_line()

  try:
    imagefile =Image.open(sys.argv[1])
  except FileNotFoundError:
    sys.exit('File not found, idiot') 

  shirtfile = Image.open('shirt.png')
  size = shirtfile.size
  muppet = ImageOps.fit(imagefile,size)
  muppet.paste(shirtfile,shirtfile)  
  muppet.save(sys.argv[2])


  



def check_comman_line():
  if len(sys.argv) != 3 :
    sys.exit('You should have exactly two arguements')
  file1 = splitext(sys.argv[1])
  file2 = splitext(sys.argv[2])  
  if check_extension(file1[1]) and check_extension(file2[1]) == False :
    sys.exit('Incalid input')
  if file1[1].lower() != file2[1].lower():
    sys.exit('Input and output have different extensions') 
 

def check_extension(file):
  if file in ['jpeg','jpg','png']:
    return True
  return False





if __name__ == '__main__' :
  main()          
         