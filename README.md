# random invoice generator

# Product Combination Generator

This Python script generates random combinations of products based on a given total price. It then writes these combinations to specific fields in an Excel template.

## How it works

The script starts with a dictionary of products, where the keys are product names and the values are product prices. It then asks the user to input a total price.

The script generates combinations of products such that their total price is less than or equal to the user's input. It does this by randomly selecting a product and subtracting its price from the total price. This process is repeated until the total price is less than the minimum product price.

The combinations of products are stored in a list, which is then converted to a pandas DataFrame. The DataFrame is written to an Excel file, with the product names, prices, and counts written to specific fields in the Excel template.

## Usage

1. Ensure that you have the required Python libraries installed. You can install them with pip:

```bash pip install pandas openpyxl```


2. Run the script:

```bash python main.py```


3. When prompted, enter the total price.

4. The script will generate the product combinations and write them to an Excel file at the specified path.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
