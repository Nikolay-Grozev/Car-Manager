import json

with open('data/json_data.json', 'r') as file:
    data_dict = json.load(file)

car_models_list = [car['name'] for car in data_dict]

print(car_models_list)
print([car["models"] for car in data_dict if car['id'] == 'CITROEN'])
print([models['name'] for models in data_dict if models['id'] == 'AMI'  ])
print(len(car_models_list))
all_models = [models['models'] for models in data_dict]
print(type(all_models))
print(type(car_models_list))


