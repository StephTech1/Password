#create a program that asks the user to input a password 
print("Please choose a strong password")
password1 = str(input("What is your chosen password?"))
#re-enter the password
password2 = str(input("Please re-enter your password..."))
#determine if they match or not
while (password1 == password2):
  print ("Your passwords match")
  break 
if (password1 != password2):
  print ("Your passwords don't match")

#tells the user if password is weak, medium or strong
strength = str(input("Is your password good?"))
if (strength > 0 and strength is < 5):
  print("Your password is weak - please choose a stronger one")
if (strength > 5 and strength is < 8):
  print("Your password is medium - try adding more characters")
if (strength > 8 and strength < 12):
  print("Well done, your password strength is strong")


#def (password1):
#if len (password1) < 3 and len (password1) == 3 :
  #print("Your password is too weak")
#if len (password1) len >3 and <5:
  #print("Your password is medium")
#if len (password1) 1 len >5:
  #print("Your password is stong!")