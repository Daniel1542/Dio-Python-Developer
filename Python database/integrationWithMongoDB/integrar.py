from pymongo import MongoClient
import certifi
import pprint


ca = certifi.where()


# Conecta-se ao banco de dados MongoDB
client = MongoClient(
    "mongodb+srv://user:senha@cluster1.vpn3ilq.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=ca)

db = client.banco
collection = db.banco_collection
print("\ncolection")
print(db.banco_collection)

cliente = {
    "nome": "Michel",
    "cpf": "0245",
    "endereco": "monga"}

clientes = db.clientes
cliente_id = clientes.insert_one(cliente).inserted_id
print("\npostar id")
print(cliente_id)

print(db.clientes.find_one())
pprint.pprint(db.clientes.find_one())


# Define os documentos a serem inseridos
new_clientes = [{
    "nome": "Mike",
    "cpf": "0233",
    "endereco": "mongo"},
    {
    "nome": "Mik",
    "cpf": "0234",
    "endereco": "mong"},
    {
    "nome": "Outro",
    "cpf": "5678",
    "endereco": "outra rua"}]

result = clientes.insert_many(new_clientes)
print("\npostar ids")
print(result.inserted_ids)

print("\nRecuperação final")
pprint.pprint(db.clientes.find_one({"nome": "Outro"}))

print("\n Documentos presentes na coleção clientes")
for post in clientes.find():
    pprint.pprint(post)
