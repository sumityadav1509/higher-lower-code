# Display Art  
from art import logo 
from game_data import data 
import random
print(logo)   
account_a=random.choice(data) 
account_b=random.choice(data) 
if account_a==account_b:
  account_b=random.choice(data) 


account_name= account_a["name"] 
account_descr= account_a["description"] 
account_country= account_a["country"] 
print(f"{account_name} , a {account_descr}  , from {account_country} ")  



 




# Generate a random account from game data.

# Format the account data into printable format. 

# Ask a user for guess
 

# Check if user is correct 
# Get follower count 
