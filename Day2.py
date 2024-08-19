meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

def solve(meal_cost, tip_percent, tax_percent):
    # Calculate the tip
    tip = (tip_percent / 100) * meal_cost
    
    # Calculate the tax
    tax = (tax_percent / 100) * meal_cost
    
    # Calculate the total cost
    total = meal_cost + tip + tax
    
    # Print the total cost rounded to the nearest integer
    print(round(total))

solve(meal_cost, tip_percent, tax_percent)

