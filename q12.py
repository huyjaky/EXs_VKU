import pandas as pd


class CustomerData:
    def __init__(self, customers, products, quantities):
        self.customers = customers
        self.products = products
        self.quantities = quantities
        self.df = pd.DataFrame(
            {
                "Customer": self.customers,
                "Product": self.products,
                "QuantityList": self.quantities,
            }
        )
        self._separate_quantity_unit()

    def _separate_quantity_unit(self):
        # Extract numerical quantity and unit from QuantityList column
        self.df[["Quantity", "Unit"]] = self.df["QuantityList"].str.extract(
            r"(\d+)\s*(\w+)"
        )
        self.df["Quantity"] = self.df["Quantity"].astype(int)

    def get_dataframe(self):
        return self.df

    def find_pork_customers(self, min_quantity):
        # Find customers who bought more than min_quantity kg of Pork
        pork_customers = self.df[
            (self.df["Product"] == "Pork")
            & (self.df["Quantity"] > min_quantity)
            & (self.df["Unit"] == "kg")
        ]
        return pork_customers


# Example usage:
CustomerList = ["John", "John", "Marry", "Marry", "Marry"]
ProductList = ["Beer", "Pork", "Milk", "Vegetable", "Pork"]
QuantityList = ["2 Bottles", "1 kg", "5 boxes", "2 bunches", "3 kg"]

customer_data = CustomerData(CustomerList, ProductList, QuantityList)
df = customer_data.get_dataframe()
pork_customers = customer_data.find_pork_customers(2)

print("DataFrame:")
print(df)
print("\nCustomers who bought more than 2kg of Pork:")
print(pork_customers)

customer_data = CustomerData(CustomerList, ProductList, QuantityList)
df = customer_data.get_dataframe()
pork_customers = customer_data.find_pork_customers(2)

print("DataFrame:")
print(df)
print("\nCustomers who bought more than 2kg of Pork:")
print(pork_customers)
