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
    for doc in docs:
      print(f'{doc.id} => {doc.to_dict()}')

addData("psychic-bliss-365216","cities","ndel",data)
readData("psychic-bliss-365216","cities")
