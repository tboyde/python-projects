CAKE_TAX = 2
CUPCAKE_PRICE = 5
cupcakes_remaining = 100

def calculate_price (desired_cupcakes): 
  return (CUPCAKE_PRICE * desired_cupcakes) + CAKE_TAX
while cupcakes_remaining >= 1:
  print("There are {} cupcakes available." .format(cupcakes_remaining))
  user_name = input("Hello, what is your name? ")
  desired_cupcakes = input("Thank you {} . How many cupcakes would you like to buy? ".format(user_name))
  try: 
    desired_cupcakes = int(desired_cupcakes)

    if desired_cupcakes > cupcakes_remaining:
      raise ValueError("Sorry, looks like there are only {} cupcakes remaining.".format(cupcakes_remaining))
  except ValueError as err: 
      #Include the error
      print("Oh, no. We ran into an issue. {}. Please try again.".format(err))
  else: 
    total_price = calculate_price(desired_cupcakes)
    print("Thanks " + user_name + ". Your total cost for {} cupcakes".format(desired_cupcakes)  + " is ${}.".format(total_price))
    should_proceed = input("Would you like to confirm your purchase? Y/N ")
    if should_proceed.lower() == "y" :
      print("SOLD! We'll have {} cupcakes coming out for ya.".format(desired_cupcakes))
      cupcakes_remaining -= desired_cupcakes  
    else: 
      print("That's alright. Just visit us next time you have a sweet tooth {}".format(user_name))
    
print("We are all sold out! Come back tomorrow for our fresh baked batch.")