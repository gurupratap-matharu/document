from cursor import Cursor


class Document:
    """
    Represents a generic document that can be parsed by text editors or document
    processors
    """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self._filename = ''

    def insert(self, character):
        """
        Insert a new character in the document at the current cursor position
        """
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """Deletes the character at current cursor position"""
        del self.characters[self.cursor.position]

    def save(self):
        """Saves the document to persistent memory storage on the computer"""
        with open(self._filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        return ''.join(self.characters)

    @property
    def filename(self):
        print('getting filename...')
        return self._filename

    @filename.setter
    def filename(self, name):
        print('setting filename...')
        self._filename = name

    def __repr__(self):
        return self._filename
