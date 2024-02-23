def generate_cols(number_of_parts:int):
  for i in range(number_of_parts):
    name = input("What is the name of this column?")
def greater(val:float):
   #making the nav bar height 20% or less
  if val>=5 and val<100:
    return True
  else:
    raise Exception
def lesser(val:float):
  #making the nav bar width 20% or more
  if val<=5 and val>=1:
    return True
  else:
    raise Exception
def main():
  screen_width= int(input("Enter screen width"))
  screen_height= int(input("Enter screen height"))
  while True:
    nav_height = int(input("Enter nav bar height in px"))
    val = screen_height/nav_height
    try:
      greater(val=val)
      break
    except:
      print("Nav_height must be atmost 20% of the screen")   
  while True:
    nav_width = int(input("Enter nav bar width in px"))
    val2 = screen_width/nav_width
    try:
      lesser(val=val2)
      break
    except:
      print("Nav_width must be atleast 20% of the screen")      
  # the nav bar can only have a maximum of 20% of the screen height
  while True:
    cols = input("How many parts do you need the nav bar to be broken into?")
    try:
      int(cols)
      cols = int(cols)
      generate_cols(cols)
    except:
      print("try again")  

main()
