# dict
my_dict = {"key": "value", "name": "mahdi", "famaily": "abbaszadeh"}

# if key in my_dict --> print value in my_dict
print(my_dict.get("key"))

# if key not in my_dict --> print None
print(my_dict.get("hasan"))

# How to change all key values ​​in a dictionary
# Whatever is key to the name of the name becomes Hasan.
my_dict.update({"name": "hasan"})
print(my_dict)

my_dic_2 = {"name": "mahdi", "family": "naseri", "id": 1223456}
# add key and value in dictionary
my_dic_2["age"] = 20
# change value key
my_dic_2["name"] = "hasan"
# remove key and value in dic
my_dic_2.pop("id")
print(my_dic_2)
