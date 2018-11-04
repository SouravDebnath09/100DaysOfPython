# This is to explain how sets work in Python
import sys
country = { "India", "Pakistan", "China", "Bangladesh", "Indonesia", "South Korea", "SriLanka" }
state = {"West Bengal", "Delhi", "Karnataka", "Madhya pradesh", "Arunachal"}

country.update(state)
country.add(1947)

# Wrong key value
try:
    country.remove("Delh")
except KeyError as error:
    print(error)
    print("it's hell not found")

# We can also try discard method. We don't need to worry about exception handling

country.discard("Delh")

# pop can also be used to remove an item
country.pop()
print(country)