my_dict = {"Jan": 1, "Feb": 2}
for _ in range(5):
    key, val = input('Enter key and value: ').split(":")
    my_dict[key] = val
for key, value in my_dict.items():
    print(f"{key}: {value}")
