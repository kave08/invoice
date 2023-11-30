import itertools
import random
import pandas as pd

# Define your data
products = {
   'اکسیدان': 95871,
   'ژل مو': 268814,
   'ماسک مو': 907951,
   'واکس مو': 349019,
   'شامپو رنگ': 699918,
   'نرم کننده مو': 323955,
   'کرم دست و صورت': 356539,
   'شامپو': 256282,
   'شیر مو': 681120,
   'بلک ماسک': 430478,
   'ریممور': 828398,
   'رنگ مو':231217
}

# Get user input for total price
total_price = int(input("Enter the total price: "))

# Initialize an empty list to store the combinations
combinations = []

# Define the weight coefficients for each product
weight_coefficients = {
  'اکسیدان': 0.4,
  'رنگ مو': 0.2,
  'واکس مو': 0.1,
  # add other products with their corresponding weight coefficients
}

# Create a list of products with their weight coefficients
products_with_weights = [(product, price, weight_coefficients[product]) for product, price in products.items()]

# Generate all combinations of the products
for combination in itertools.product(products_with_weights, repeat=len(products)):
   # Initialize the total price for this combination
   total_price_for_combination = total_price

   # For each product in the combination
   for product, price, weight in combination:
       # Calculate the maximum possible count for the chosen price
       max_count = total_price_for_combination // price

       # Choose a random count up to the maximum
       count = random.randint(1, max_count)

       # If the count is equal to 1, choose a random count up to the maximum again
       while count == 1:
           count = random.randint(1, max_count)

       # Subtract the total cost of these products from the total price
       total_price_for_combination -= price * count

       # Add the combination to the list
       combinations.append((product, price, count))

   # If the total price for this combination is greater than the minimum product price, add it to the combinations
   if total_price_for_combination > min(products.values()):
       combinations.append(("تخفیف", total_price_for_combination, 1))

# Print the combinations
for product, price, count in combinations:
   print("Product: ", product, "Price: ", price, "Count: ", count)

# Convert the combinations to a pandas DataFrame
df = pd.DataFrame(combinations, columns=['Product', 'Price', 'Count'])

# Rename the DataFrame columns
df = df.rename(columns={
   'Product': 'sstt شرح کالا / خدمت',
   'Price': 'fee مبلغ واحد',
   'Count': 'am تعداد / مقدار',
})

# Define the columns you want to write to Excel
columns = ['sstt شرح کالا / خدمت', 'fee مبلغ واحد', 'am تعداد / مقدار']

# Write the DataFrame to an Excel file
df.to_excel('C:/Users/z.mehrasa/Desktop/invoice/combinations.xlsx', index=False)
