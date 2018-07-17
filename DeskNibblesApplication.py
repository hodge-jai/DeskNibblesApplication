import urllib.request, json

#Data sources
snacker_url = "https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json"

stock_url = "https://desknibbles.ca/products.json?limit=250"


#Pull the json data from both web sources
with urllib.request.urlopen(snacker_url) as url1,urllib.request.urlopen(stock_url) as url2:
    snacker_json = json.loads(url1.read().decode())
    stock_json = json.loads(url2.read().decode())
    #parsed = json.dumps(data, indent = 4, sort_keys = True)
    #print(parsed)

#Initialize two empty dictionaries to store relevant customer and stock information
stock_data = {}
snacker_data = {}

#Refine stock data to just the product name and the product price
for stock in stock_json["products"]:
    stock_data[stock["title"]] = stock["variants"][0]["price"]


#Iterate over snacker data, checking the stock data to see if the customer's favourite snack is in stock
#If the item is in stock, store the email and price information
#If multiple people want the same item, simply append their email to the array
for snacker in snacker_json:
    if snacker["fave_snack"] in stock_data:
        if snacker["fave_snack"] not in snacker_data:
            snacker_data[snacker["fave_snack"]] =  {"emails" : [snacker["email"]], "price" : float(stock_data[snacker["fave_snack"]])}
        else:
            snacker_data[snacker["fave_snack"]]["emails"].append(snacker["email"])

#Print the answers to the test questions:

#Question A
print(list(snacker_data))

#Question B
for e in snacker_data:
    print(list(snacker_data[e]["emails"]))

#Question C
total_cost = 0
for cost in snacker_data:
    total_cost += len(snacker_data[cost]["emails"])*snacker_data[cost]["price"]

print(total_cost)
