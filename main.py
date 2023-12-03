import pandas as pd
import operator

# Define your data
# Create a list of products with their weight coefficients
products = [
   {'name': 'اکسیدان', 'price': 95871, 'weight': 40},
   {'name': 'ژل مو', 'price': 268814, 'weight': 20},
   {'name': 'ماسک مو', 'price': 907951, 'weight': 10},
   {'name': 'واکس مو', 'price': 349019, 'weight': 7},
   {'name': 'شامپو رنگ', 'price': 699918, 'weight': 5},
   {'name': 'نرم کننده مو', 'price': 323955, 'weight': 5},
   {'name': 'کرم دست و صورت', 'price': 323955, 'weight': 5},
   {'name': 'شامپو', 'price': 256282, 'weight': 3},
   {'name': 'شیر مو', 'price': 681120, 'weight': 3},
   {'name': 'بلک ماسک', 'price': 430478, 'weight': 1},
   {'name': 'ریممور', 'price': 828398, 'weight': 0.5},
   {'name': 'رنگ مو', 'price': 231217, 'weight': 0.5},
]

products = sorted(products, key=operator.itemgetter('price'))

# Get user input for total price
total_price = int(input("Enter the total price: "))
# Initialize an empty list to store the combinations
xlsx_name = "combination"+str(total_price/10000000)+".xlsx"
combinations = []

total_weight = 0
for product in products:
   total_weight += product['weight']

total_weights = total_price/total_weight;
for product in products:
    # For each product
    product_share = total_weights*product['weight']
    product_count = int(product_share/product['price'])

    # If max_count is 0, continue with the next product
    if product_count == 0:
        continue

    # Subtract the total cost of these products from the total price
    total_price -= product['price'] * product_count

    # Add the combination to the list
    combinations.append({'name': product['name'], 'price': product['price'], 'count': product_count, 'total_price': product['price']*product_count})

# If the total price for this combination is greater than the minimum product price, add it to the combinations
for combination in combinations:
    if total_price > combination['price']:
        product_count = int(total_price/combination['price'])
        total_price -= combination['price'] * product_count
        product_count += combination['count']
        new_combination = {'name': combination['name'], 'price': combination['price'], 'count': product_count, 'total_price': combination['price']*product_count}
        combination.update(new_combination)

if total_price > 0:
    combinations.append({'name': 'تخفیف', 'price': total_price, 'count': 1, 'total_price':total_price})

for combination in combinations:
    print(combination)

# Convert the combinations to a pandas DataFrame
df = pd.DataFrame.from_dict(combinations)

# Rename the DataFrame columns
df = df.rename(columns={
'Product': 'sstt شرح کالا / خدمت',
'Price': 'fee مبلغ واحد',
'Count': 'am تعداد / مقدار',
'Total Price': 'مجموع کل',
})

# Define the columns you want to write to Excel
columns = ['sstt شرح کالا / خدمت', 'fee مبلغ واحد', 'am تعداد / مقدار','مجموع کل']

# Write the DataFrame to an Excel file
# df.to_excel('C:/Users/z.mehrasa/Desktop/invoice/combinations.xlsx', index=False)
df.to_excel(xlsx_name, index=False)
