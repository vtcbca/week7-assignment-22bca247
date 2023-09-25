import pandas as pd

# import csv

# # Function to add a new record with user input
# def add_record():
#     prod_no = input("Enter Product Number: ")
#     prod_name = input("Enter Product Name: ")
#     jan = int(input("Enter January Sales: "))
#     feb = int(input("Enter February Sales: "))
#     mar = int(input("Enter March Sales: "))
#     apr = int(input("Enter April Sales: "))
#     may = int(input("Enter May Sales: "))
#     jun = int(input("Enter June Sales: "))
#     return [prod_no, prod_name, jan, feb, mar, apr, may, jun]

# # Initialize the data with records for 5 products
# data = [
#     ["P1", "apple", 1000, 1500, 1200, 1800, 2000, 2500],
#     ["P2","potato", 900, 1300, 1100, 1700, 1900, 2400],
#     ["P3", "tomato", 800, 1200, 1000, 1600, 1800, 2300],
#     ["P4", "kivi", 1100, 1600, 1300, 1900, 2100, 2600],
#     ["P5", "orange", 950, 1400, 1150, 1750, 1950, 2450],
# ]

# # Prompt the user to add 12 additional records
# for _ in range(12):
#     data.append(add_record())

# # CSV file path


# # Write data to the CSV file
# with open("product.csv","w", newline="") as file:
#     writer = csv.writer(file)
#     # Write header
#     writer.writerow(["Prod_No", "Prod_Name", "Jan", "Feb", "Mar", "Apr", "May", "Jun"])
#     # Write data rows
#     writer.writerows(data)


# 1. Add 12 Records. Take input from the user.

# 2. Create a DataFrame
df = pd.read_csv("product.csv")
# 3. Change Column Names
df.columns = ["Product No", "Product Name", "January", "February", "March", "April", "May", "June"]

# 4. Add "Total Sell" and "Average Sell" columns
df["Total Sell"] = df.iloc[:, 2:].sum(axis=1)
df["Average Sell"] = df.iloc[:, 2:8].mean(axis=1)

#to csv final sheet
df.to_csv("final_product.csv")

# 5. Add 2 rows at the end
df = df.append({"Product No": "P6", "Product Name": "Product6", "January": 100, "February": 200, "March": 300,
                "April": 400, "May": 500, "June": 600, "Total Sell": 2100, "Average Sell": 350}, ignore_index=True)
df = df.append({"Product No": "P7", "Product Name": "Product7", "January": 700, "February": 800, "March": 900,
                "April": 1000, "May": 1100, "June": 1200, "Total Sell": 5700, "Average Sell": 950}, ignore_index=True)

# 6. Add 2 rows after the 3rd row
row3 = pd.Series(["P8", "Product8", 50, 60, 70, 80, 90, 100, 500, 75],
                 index=["Product No", "Product Name", "January", "February", "March", "April", "May", "June",
                        "Total Sell", "Average Sell"])
df = pd.concat([df.iloc[:3], row3, df.iloc[3:]]).reset_index(drop=True)

# 7. Print the first 5 rows
print("First 5 rows:")
print(df.head())

# 8. Print the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# 9. Print rows 6 to 10
print("\nRows 6 to 10:")
print(df.iloc[5:10])

# 10. Print only the product name
print("\nProduct Names:")
print(df["Product Name"])

# 11. Print sales of January with product ID and product name
print("\nJanuary Sales with Product ID and Name:")
print(df[["Product No", "Product Name", "January"]])

# 12. Print only those product ID and product name where January sales > 5000 and February sales > 8000
print("\nProducts with January > 5000 and February > 8000:")
print(df[(df["January"] > 5000) & (df["February"] > 8000)][["Product No", "Product Name"]])

# 13. Print records in sorting order of Product name
print("\nSorted by Product Name:")
print(df.sort_values("Product Name"))

# 14. Display only odd index number column records
print("\nOdd Index Columns:")
print(df.iloc[:, 1::2])
