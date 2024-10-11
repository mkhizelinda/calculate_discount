# Define a function named calculate_discount that takes two parameters: price and discount_percent
def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    Parameters:
    - price: The original price of the item
    - discount_percent: The discount percentage to be applied

    Returns:
    - The final price after applying the discount if the discount is 20% or higher
    - The original price if the discount is less than 20%
    """
    
    # Check if the discount percent is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount by multiplying the price by discount percent divided by 100
        discount_amount = price * (discount_percent / 100)
        
        # Calculate the final price by subtracting the discount amount from the original price
        final_price = price - discount_amount
        
        # Return the final price after applying the discount
        return final_price
    else:
        # If the discount percent is less than 20%, return the original price
        return price

# Prompt the user to enter the original price of the item
original_price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function with the user inputs and store the result in a variable
final_price = calculate_discount(original_price, discount_percentage)

# Check if the final price is equal to the original price (no discount applied)
if final_price == original_price:
    # Print the original price if no discount was applied
    print(f"No discount applied. The original price is: ${original_price:.2f}")
else:
    # Print the final price after applying the discount
    print(f"The final price after applying the discount is: ${final_price:.2f}")
