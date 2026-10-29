dict_1={"red":6,"blue":2,"violet":9,"white":7}
asscending_dict=dict(sorted(dict_1.items()))
print("asscending is:",asscending_dict)
descending_dict=dict(sorted(dict_1.items(),reverse=True))
print("descending is:",descending_dict)