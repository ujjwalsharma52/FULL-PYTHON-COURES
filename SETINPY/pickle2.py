import pickle

file = open("data.txt", "rb")

data = pickle.load(file)

print(data)

file.close()