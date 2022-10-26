from google.cloud import firestore
import pyjq
import requests
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
   # db.collection(collection_name).document(document_id).set(data)
    db.collection(collection_name).document(document_id).update({u'rdata': firestore.ArrayUnion([data])})

def readData(project_id,collection_name):
    # db = firestore.Client(project=project_id)
    # users_ref = db.collection(collection_name)
    # docs = users_ref.stream()
    # for doc in docs:
    #   print(f'{doc.id} => {doc.to_dict()}')
    url = "https://api.github.com/repos/stedolan/jq/contributors"
    r = requests.get(url)
    #docs = r.json()
    docs = [{
    "login": "nicowilliams",
    "id": 604851,
    "node_id": "MDQ6VXNlcjYwNDg1MQ==",
    "avatar_url": "https://avatars.githubusercontent.com/u/604851?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/nicowilliams",
    "html_url": "https://github.com/nicowilliams",
    "followers_url": "https://api.github.com/users/nicowilliams/followers",
    "following_url": "https://api.github.com/users/nicowilliams/following{/other_user}",
    "gists_url": "https://api.github.com/users/nicowilliams/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/nicowilliams/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/nicowilliams/subscriptions",
    "organizations_url": "https://api.github.com/users/nicowilliams/orgs",
    "repos_url": "https://api.github.com/users/nicowilliams/repos",
    "events_url": "https://api.github.com/users/nicowilliams/events{/privacy}",
    "received_events_url": "https://api.github.com/users/nicowilliams/received_events",
    "type": "User",
    "contributions": 519
  },
  {
    "login": "stedolan",
    "id": 79765,
    "node_id": "MDQ6VXNlcjc5NzY1",
    "avatar_url": "https://avatars.githubusercontent.com/u/79765?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/stedolan",
    "html_url": "https://github.com/stedolan",
    "followers_url": "https://api.github.com/users/stedolan/followers",
    "following_url": "https://api.github.com/users/stedolan/following{/other_user}",
    "gists_url": "https://api.github.com/users/stedolan/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/stedolan/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/stedolan/subscriptions",
    "organizations_url": "https://api.github.com/users/stedolan/orgs",
    "repos_url": "https://api.github.com/users/stedolan/repos",
    "events_url": "https://api.github.com/users/stedolan/events{/privacy}",
    "received_events_url": "https://api.github.com/users/stedolan/received_events",
    "type": "User",
    "contributions": 327
  },
]
    return docs

def updateData(read_project_id, write_project_id, read_collection_name, write_collection_name, write_document_id):
    docs = readData(read_project_id,read_collection_name)
    for doc in docs:
      #print(f'{doc.id} => {doc.to_dict()}')
      #data = doc.to_dict()
      #result1 = pyjq.one("country: .[]., data )
      #result1 = pyjq.one("{newdata: [{ country: .data[].full_name}]}",data)
      result1 = pyjq.one("{ country: .login, id: .id}",doc)
      print(result1)
      addData(write_project_id,write_collection_name,write_document_id,result1)
    

      
updateData("psychic-bliss-365216","flowing-sign-366006","cities","test","list")
#addData("psychic-bliss-365216","cities","ndel",data)
#readData("psychic-bliss-365216","cities")
# addData("flowing-sign-366006","test","list",readData)

