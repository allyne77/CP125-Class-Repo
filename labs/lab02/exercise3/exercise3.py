# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    if (name == "Director" or pin == 1122):
        return True
    else (name == "Security" or pin == 9900):
        return False

# Test your code here
print("Testing Secure Vault System...")
