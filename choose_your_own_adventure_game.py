name = input("Type your name: ")
print ("wilcome", name , " to  this Adventure!")

answer = input(
    "You are on a dirt road , it has come to a end and you can go left or right.Wich way you go?"
).lower()
 
if answer == "left":
   answer =  input("You come to a river , you can walk around it or swim acrross?")

   if answer == "swim":
     print("You swam acrross and were eaten by an alligator.")
   elif answer =="walk":
     print("You walked for many miles, ran out of water and lost the game ")
   else:
     print('Not a valid option. You lose')

elif answer == "right":
  answer = input ("You come to bridge , it looks wobbly , do  you want to cross it or head back (cross/back) ")
  
  if answer == "back":
    print("You go back  and lose.")
  elif answer =="cross":
    print("You cross the bridge and meet a stranger . do you talk to them?(yes/no) ")

    if answer =="yes":
      print("You talk to the stranger and tehy give you gold. You Win !!")
    elif answer == "no":
      print("You ignore the stranger and they are offended and you lose")
    else:
      print('Not a valid option. You lose')
 
else:
  print('Not a valid option  . You lose.')

print("thank" , name ,"for playing")