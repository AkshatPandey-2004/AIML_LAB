person = {
    "name": "Akshat",
    "age": 20,
    "city": "Ghaziabad"
}
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
person["email"] = "akshatpandey26.2004@gmail.com"
print("Updated dictionary with email:", person)
person["age"] = 20
print("Updated dictionary with modified age:", person)
if "city" in person:
    print("Key 'city' exists in the dictionary")

keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))