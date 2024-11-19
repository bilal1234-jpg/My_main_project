from pyrebase_init import storage, db


class RealTimeFirebase():
    def __init__(self, filename,local_file,email,password):
        self.filename = filename
        self.local_file = local_file
        self.email = email
        self.password =  password

    def get_and_put(self):

        try:
            format_email = self.email.replace(".",",")
            storage.child(self.filename).put(self.local_file)
            vid_url = storage.child(self.filename).get_url(None)
            current_data = db.child("users").child(format_email).child("urls").get().val()
            if current_data is None:
                current_data = []

            current_data.append(vid_url)

            db.child("users").child(format_email).child("urls").set(current_data)
            db.child("users").child(format_email).child("password").set(self.password)

        
        except Exception as e:
            print(f"file_error:{e}")
        