from datetime import datetime

class TimestampMixin:
    def __init__(self):
        self._creation_time = datetime.now()
        self._modification_time = self._creation_time

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time

    def update_modification_time(self):
        self._modification_time = datetime.now()

class File(TimestampMixin):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def rename(self, new_name):
        self.file_name = new_name
        self.update_modification_time()

class User(TimestampMixin):
    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name

    def change_username(self, new_name):
        self.user_name = new_name
        self.update_modification_time()


file = File("document.txt")
print("File Created At:", file.get_creation_time())
print("File Modified At:", file.get_modification_time())

file.rename("new_document.txt")
print("\nAfter Renaming File:")
print("File Created At:", file.get_creation_time())
print("File Modified At:", file.get_modification_time())

user = User("Gaga")
print("\nUser Created At:", user.get_creation_time())
print("User Modified At:", user.get_modification_time())

user.change_username("Gaga")
print("\nAfter Changing Username:")
print("User Created At:", user.get_creation_time())
print("User Modified At:", user.get_modification_time())

