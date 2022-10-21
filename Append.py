from google.cloud import firestore
import pyjq
data = {
    'data': [ {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
     {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
    ]
}

def addData(project_id,collection_name,document_id,data):
    db = firestore.Client(project=project_id)
    db.collection(collection_name).document(document_id).set(data)

def readData(project_id,collection_name):
    db = firestore.Client(project=project_id)
    users_ref = db.collection(collection_name)
    docs = users_ref.stream()
    # for doc in docs:
    #   print(f'{doc.id} => {doc.to_dict()}')
    return docs

def updateData(read_project_id, write_project_id, read_collection_name, write_collection_name, write_document_id):
    docs = readData(read_project_id,read_collection_name)
    for doc in docs:
      print(f'{doc.id} => {doc.to_dict()}')
      data = doc.to_dict()
      #result1 = pyjq.one("country: .[]., data )
      result1 = pyjq.one("{data: [{ country: .data[].full_name}]}",data)
      print(result1)
      addData(write_project_id,write_collection_name,write_document_id,result1)
    

      
updateData("psychic-bliss-365216","flowing-sign-366006","cities","test","list")
#addData("psychic-bliss-365216","cities","ndel",data)
#readData("psychic-bliss-365216","cities")
# addData("flowing-sign-366006","test","list",readData)

