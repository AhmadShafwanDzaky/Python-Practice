uname = ['admin'] #list for username
pw = ['admi123'] #list for password

while True: #while loop if user wrong iput username or password
     i = str(input("login or register? >> ").lower()) #conditional if
     if i == "register":
          l = str(input("Input your username: ")) #user input new username
          uname.append(l) #append user input to list
          m = str(input("Input your password: ")) #user input new password
          pw.append(m) #append user input to list
          continue
     elif i == "login":
          j = str(input("Input username: ")) #user input username
          k = str(input("Input password: ")) #user input password
          if j in uname and k in pw:
               print("Congratulation, you're logged in")
               break #break keywords to end while loop
          elif j not in uname and k in pw:
               print("!! Please input correct username !!")
               continue #continue keywords to continue while loop
          elif j in uname and k not in pw:
               print("!! Please input correct password !!")
               continue #continue keywords to continue while loop
          else:
               print("!! Please input correct username and password !!")
               continue #continue keywords to continue while loop
     else:
          print("!! Input 'login' or 'register' !!")