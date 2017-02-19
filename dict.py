cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

person = dict(name='Rafael',last_name='Santos',birthday='19/03/1983')

print('Cars', cars)
for key, value in cars.items():
    print(key + " = " + value)

print('-----------------------')
print('Person', person)
print('Name', person['name'])

