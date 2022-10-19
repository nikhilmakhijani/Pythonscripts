from google.cloud import firestore
data = {
    u'name': u'New Delhi',
    u'state': u'Delhi',
    u'country': u'India'
}
def addData(project_id,collection_name,document_id,data):
    db = firestore.Client(project=project_id)
    db.collection(collection_name).document(document_id).set(data)

def readData(project_id,collection_name):
    db = firestore.Client(project=project_id)
    users_ref = db.collection(collection_name)
    docs = users_ref.stream()
    return docs

def updateData(read_project_id, write_project_id, read_collection_name, write_collection_name, write_document_id):
    docs = readData(read_project_id,read_collection_name)
    for doc in docs:
      print(f'{doc.id} => {doc.to_dict()}')
      data = doc.to_dict()
      result1 = pyjq.one('{Country: .country , Address: .name}', data )
      addData(write_project_id,write_collection_name,write_document_id,result1)
    

      
updateData("psychic-bliss-365216","flowing-sign-366006","cities","test","list")
