class Item():
    def __init__(self, name, kind, exists):
        self.name = name
        self.kind = kind
        self.exists = exists

    def __str__(self):
        return f"{self.kind.title()}: {self.name} (Exists: {self.exists})"
