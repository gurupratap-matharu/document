class Document:
    """
    Represents a generic document that can be parsed by text editors or document
    processors
    """

    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''

    def insert(self, character):
        """
        Insert a new character in the document at the current cursor position
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        """Deletes the character at current cursor position"""
        del self.characters[self.cursor]

    def save(self):
        """Saves the document to persistent memory storage on the computer"""
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        """Moves the cursor ahead by one unit"""
        self.cursor += 1

    def back(self):
        """Moves the cursor back by one unit"""
        self.cursor -= 1
