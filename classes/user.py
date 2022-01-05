class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

    def has_permission_for(self, key):
        if self.permissions.get(key):
            return True
        else:
            return False


class Admin(User):
    def has_permission_for(self, key):
        return True

# The get() method returns the value of the item with the specified key.
