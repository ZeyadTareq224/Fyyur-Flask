x = [{'id': 1, 'type': 'sport'}, {'id': 2, 'type': 'geography'}]
new_dict = {item['id']:item['type'] for item in x}
print(new_dict)