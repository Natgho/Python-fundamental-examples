import pickle

data = {'name': 'Sezer', 'surname': 'Bozkir'}

# serialization
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# deserialization
with open('data.pkl', 'rb') as file:
    deserialized_data = pickle.load(file)

print(deserialized_data)
