def calculator():
  while True:
    num1 = int(input("Enter The First Number : "))
    num2 = int(input("Enter The Second Number : "))
    while True:
      print("\nOperation List : (+) (-) (×) (÷)")
      opt = input("\nEnter The Operation You Want (From The Above List) : ")
      if (opt == "+"):
        result = (num1+num2)
      elif (opt == "-"):
        result = (num1-num2)
      elif (opt == "×"):
        result = (num1*num2)
      elif (opt == "÷"):
        result = (num1/num2)
      else:
        print("Enter a Valid Operator")
        continue
      print("The Result is ", result)
      break
    while True:
      global cont
      cont = input("Do You Want You Use The Calculator Again ? (y or n)\n")
      if(cont != "y" and cont != "n"):
        print("Enter a Valid Input")
        continue
      elif (cont == "y"):
        print("Alright!\n")
        break
      break
    
    if (cont == "n"):   
      print("Thank U For Using It!")
      break


calculator ()

# I did it!
# Let's Go!!!
