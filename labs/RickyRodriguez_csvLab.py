'''
Ricky Rodriguez
Cist 5B: Lab 3

Generation:
saleId,saleDate,amount,product
0,2024-01-15,150.00,Widget

Options:
1. Retrieve Latest Sale
2. Compute total Revenue
3. Check for duplicate ids 
4. Search for a sale by Id
5. exit

generation numbers to graph time: 10, 100, 1000, 10000, 100000


'''
import csv
import os
from datetime import datetime, timedelta
import random
import time

def generateToCsv(filename, numRows): # Function to create and write sales data, arguments are name and number of entries
    headers = ["saleId", "saleDate", "amount", "product"]             # Defines headers and data
    data = []                                                           # Empty array for data
    products = ['Widget', 'Gadget', 'Thingamajig', 'Doohickey']         # Product names
    
    initialDate = datetime.strptime("2024-01-15", "%Y-%m-%d")            # Current date for sales data

    for i in range(numRows): # Loop to generate sales data
        saleId = i                                                        # Id increments by 1

        nextSaleDay  = random.randint(1,10)                               # Creates random date within 10 days                      
        saleDate = initialDate + timedelta(days=nextSaleDay)              # adds next sale day to initial date
        initialDate = saleDate                                            # sets initial date to sale date for next iteration
        
        amount = round(random.uniform(100.00, 300.00), 2)                 # random price bewteen 100 and 300
        
        product = random.choice(products)                                 # random product from list

        data.append({"saleId": saleId, "saleDate": saleDate.strftime("%Y-%m-%d"), "amount": amount, "product": product}) # Appends data to array

    initialDate = saleDate                                              # Updates initialDate to ensure dates are in order
    
    filepath = os.path.join('labs', filename)               # looks for labs director
    
    with open(filepath, mode='w', newline='') as file:      # Opens a file and writes data to it (puts it in filepath)
        writer = csv.DictWriter(file, fieldnames=headers)   # creates dictionary writer object and assigns headers from headers array
        writer.writeheader()                                # Writes a header to the file
        
        for row in data:                                    # Loops through the data array
            writer.writerow(row)                            # Writes the row to the file

def generateCsvTime(filename, numRows): # function that generates a sales file and measure the time it takes to complete
    initial_time = time.time() # gets the current time using the built in time module in python
    
    generateToCsv(filename, numRows) # generates a file to be tested
    
    stop_time = time.time() # gets the time after the file has been generated
    duration = stop_time - initial_time # calculates the time it took to create the file
    
    print (f"Time taken to generate {numRows} rows: {duration:.4f} seconds") # displays the time for the user to see

'''
# generating csv file to test the time it takes to create each one
generateCsvTime("sales_100.csv", 10)
generateCsvTime("sales_1000.csv", 100)
generateCsvTime("sales_10000.csv", 1000)
generateCsvTime("sales_100000.csv", 10000)
generateCsvTime("sales_1000000.csv", 100000)
'''

def readCsv(filename): # function that reads the csv with the name filename
    filepath = os.path.join('labs', filename) # looks for labs directory
    sales_data = []                           # Empty array for sales data
    
    with open(filepath, mode='r', newline='') as file:  # opens file in read mode
        reader = csv.DictReader(file)                   # dictionary reader object for reading 
        
        for row in reader:                              # Iterates over every element in the header, applies variables 
            row['saleId'] = int(row['saleId'])
            row['amount'] = float(row['amount'])
            row['saleDate'] = datetime.strptime(row['saleDate'], "%Y-%m-%d")
            
            sales_data.append(row)
    
    return sales_data

def get_latest_sale(sales_data):
    latest_sale = max(sales_data, key=lambda x: x['saleDate'])
    return latest_sale

def compute_total_revenue(sales_data):
    total_revenue = sum(sale['amount'] for sale in sales_data)
    return total_revenue

def check_duplicate_saleIds(sales_data):
    saleId_counts = {}
    duplicates = []
    
    for sale in sales_data:
        saleId = sale['saleId']
        if saleId in saleId_counts:
            saleId_counts[saleId] += 1
        else:
            saleId_counts[saleId] = 1
    
    for saleId, count in saleId_counts.items():
        if count > 1:
            duplicates.append(saleId)
    
    return duplicates

def search_sale_by_id(sales_data, saleId):
    for sale in sales_data:
        if sale['saleId'] == saleId:
            return sale
    return None

generateToCsv('sales_data.csv', 10)
sales_data = readCsv('sales_data.csv')

while True:
    print("\nOptions:")
    print("1. Retrieve the latest sale")
    print("2. Compute the total revenue")
    print("3. Check for duplicate sale IDs")
    print("4. Search for a sale by its ID")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        latest_sale = get_latest_sale(sales_data)
        print("Latest Sale:", latest_sale)
    elif choice == '2':
        total_revenue = compute_total_revenue(sales_data)
        print("Total Revenue:", total_revenue)
    elif choice == '3':
        duplicates = check_duplicate_saleIds(sales_data)
        if duplicates:
            print("Duplicate Sale IDs:", duplicates)
        else:
            print("No duplicate sale IDs found.")
    elif choice == '4':
        saleId = int(input("Enter the sale ID to search: "))
        sale = search_sale_by_id(sales_data, saleId)
        if sale:
            print("Sale Found:", sale)
        else:
            print("Sale ID not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")