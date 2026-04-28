# Global variable
counter = 10

def scope_demo():
    # Shadowing: This creates a local 'counter' that masks the global one
    counter = 5 
    local_var = "I only exist inside this function"
    
    print(f"Inside function (local counter): {counter}")
    print(f"Inside function: {local_var}")

def modify_global():
    global counter
    counter += 1
    print(f"Global counter modified to: {counter}")

# Execution
print(f"Before function (global counter): {counter}")

scope_demo()

print(f"After function (global counter is still): {counter}")

# Modifying the global variable
modify_global()

# Demonstration of NameError
try:
    print(local_var)
except NameError as e:
    print(f"Accessing local_var outside: {e}")
