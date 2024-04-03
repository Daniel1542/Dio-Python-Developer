from pymongo import MongoClient, ASCENDING
import certifi
import pprint

ca = certifi.where()


# Conecta-se ao banco de dados MongoDB
client = MongoClient(
    "mongodb+srv://user:senha@cluster1.vpn3ilq.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=ca)


db = client.banco
clientes = db.clientes

for cliente in clientes.find():
    pprint.pprint(cliente)

print(clientes.count_documents({}))
print(clientes.count_documents({"nome": "Mike"}))
print(clientes.count_documents({"endereco": "mongo"}))

pprint.pprint(clientes.find_one({"nome": "Mike"}))

print("\nRecuperando info da coleção cliente de maneira ordenada")
for cliente in clientes.find({}).sort("nome"):
    pprint.pprint(cliente)

result = db.profiles.create_index([('nome', ASCENDING)],
                                  unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'nome': 'Luke'},
    {'user_id': 212, 'nome': 'Joao'}]

result = db.profile_user.insert_many(user_profile_user)

print("\nColeções armazenadas no mongoDB")
collections = db.list_collection_names()


print("coleção")
for collection in collections:
    print(collection)

print("achar cliente")
for cliente in clientes.find():
    pprint.pprint(cliente)

print("deletando cliente")
print(clientes.delete_one({"nome": "Mike"}))
# print(db.profile_user.drop())

print("deletando banco de dados")
# client.drop_database('banco')

print(db.list_collection_names())
