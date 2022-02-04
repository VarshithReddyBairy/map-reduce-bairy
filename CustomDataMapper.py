# Varshith Bairy - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 20) : 
    id,address,categories,city,country,keys,latitude,longitude,menuPageURL,amountMax,amountMin,currency,dateSeen,description,name,postalCode,priceRangeCurrency,priceRangeMin,priceRangeMax,province = datalist

    # print intermediate key-value pairs to standard output
    print(city,"\t",1)