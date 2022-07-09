#EXAMPLE: SURFSIDE BEACH TRIP 0705 - 0708
#code for the trip is 0705
dict = {"buckee1" : 35, "gas1": 41, "Pha Lau": 50, "starbucks1": 15, "pier 30": 75,
        "wingstop": 36, "Hotel1": 162, "hotel2": 99, "Chibahotpot": 105, "gas2": 41,
        "LuckyLand": 30, "buckee2": 34, "starbucks2": 30}
#pull up each elements in dict print(dict)
#print(dict.values())
#print(dict.keys())

#OR USING FOR LOOP BUT IT WILL SHOW IN SEPERATE LINES
for theValue in dict.values():
    print(theValue)
    
for theKeys in dict.keys():
    print(theKeys)

a = list(dict.values())
print(a)
b = sum(a)
print(b)

##show detail of the trip
tripday = input("Please enter your trip days: ") ##mmdd
if tripday == "0705":
    print(dict)
    print("Total of the trip is: ","$",b,sep="")
else:
    print("Please check date format!")


##FIND THE HIGHEST PRICE THAT YOU PAID FOR THE TRIP
c = max(dict.values())
print(c)

##let's try
def get_keys_from_value(dict, val):
    return [k for k, v in dict.items() if v == val]

keys = get_keys_from_value(dict, c)
print(keys)


##FIND THE LOWEST PRICE THAT YOU PAID FOR THE TRIP
d = min(dict.values())
print(d)
##taking an opportunity from the def function above, we change keys to lowest value.
keys = get_keys_from_value(dict, d)
print(keys)


