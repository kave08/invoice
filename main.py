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

# While the total price is greater than the minimum product price
while total_price > min(products.values()):
    # Choose a random product
    product, price = random.choice(list(products.items()))

    # If the chosen price is greater than the total price, continue with the next iteration
    if price > total_price:
        continue

    # Calculate the maximum possible count for the chosen price
    max_count = total_price // price

    # Choose a random count up to the maximum
    count = random.randint(1, max_count)

    # Subtract the total cost of these products from the total price
    total_price -= price * count

    # Add the combination to the list
    combinations.append((product, price, count))

    # Remove the chosen product from the products dictionary
    del products[product]

combinations.append(("تخفیف", total_price, 1))

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

