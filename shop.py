menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750
total = 0
############################# Start Here! ##############################
cupcake_shop_name = "Bakers"
signature_flavors = ["Carrot", "Marble", "Blueberry Swirl", "pumpkin", "red velvet"]
order_list = []


   
def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("This is our menu:")
    for a in menu:
      print(a+"  "+ str(menu[a]))  
  
      
     
def print_originals():
  """
  Print the original flavor cupcakes.
  """
  print("Our original flavor cupcakes (KD %s each):" % original_price)
  for b in original_flavors:
     print (b) 


def print_signatures():
  """
  Print the signature flavor cupcakes.
  """
  print("Our signature flavor cupcake (KD %s each):" % signature_price)
  for c in signature_flavors:
    print (c) 


def is_valid_order(order):
  """
  Check if an order exists in the shop.
  ***NOTE***: i wrote what i have in mind for validating the order, yet it didn't work. i think i'm not getting passing variables between functions
  """
  for y in order:
    if y not in original_flavors or y not in original_flavors or y not in signature_flavors:
      return False 
    else:
      return True
    



def get_order():
  """
  Repeatedly ask customer for order until they end their order by typing "Exit".
  """
  o=' '
  cond=True
  order_list = []
  print("Please provide your order as written in the menu. Type 'exit' to end your order")
  
  while cond: 
    o= input() 
    f=is_valid_order(o)
    if o !="exit":
      if  is_valid_order() :
        order_list.append(o)
      else:
        return order_list   
    else: 
      cond==False
      break
  return order_list
    
    


def accept_credit_card(total):
  """
  Return whether an order is eligible for credit card payment.
  """
  if total>=5:
    print ("Credit Card payment is accepted")
  else:
    print ("Credit Card is not accepted for this order")


def get_total_price(order_list):
  """
  Calculate and return total price of the order.
  """
  total = 0
  for item in order_list:
    if item in menu:
      total= total+ menu[item]
    elif item in original_flavors:
      total= total+ original_price
    elif item in signature_flavors:
      total= total+ signature_price
  return total


def print_order(order_list):
  """
  Print the order of the customer.
  """
  print("Your order is:%s " % order_list) 
  print("Your bill is:%s"  %get_total_price(order_list))
  print (accept_credit_card(total))
  print("Thank you for visiting %s" %cupcake_shop_name)
  
