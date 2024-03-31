import pprint
import pymongo as pyM

# Conecta-se ao banco de dados MongoDB
client = pyM.MongoClient("mongodb+srv://user:senha@cluster1.vpn3ilq.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

post = {
    "nome": "Mike",
    "cpf": "023",
    "endereco": "mongo"}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

pprint.pprint(db.posts.find_one())


# Define os documentos a serem inseridos
new_posts  = [{
    "nome": "Mike",
    "cpf": "023",
    "endereco": "mongo"},
    {
    "nome": "Mik",
    "cpf": "0234",
    "endereco": "mong"},
    {
    "nome": "Outro",
    "cpf": "5678",
    "endereco": "outra rua"}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)