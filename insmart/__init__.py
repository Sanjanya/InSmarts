from firebase_admin import firestore
import firebase_init
# Initialize Firestore DB
db = firestore.client()

# Add a new document to the 'users' collection
user_ref = db.collection('users').document()
user_ref.set({
    'name': 'John Doe',
    'email': 'john.doe@example.com'
})