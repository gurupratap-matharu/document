class Cursor:
    """
    Represents the cursor of a document which is aware about its own position
    and has helper methods like forward, back, etc
    """

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        """
        Takes the cursor to the start of the current line. Meant for the `home`
        key on the keyboard
        """
        while self.document.characters[self.position] != '\n':
            self.position -= 1
            if self.position == 0:
                # reached the beginning of the document before newline
                break

    def end(self):
        """
        Takes the cursor to the end of the current line. Meant for the `end` key of the 
        keyboard.
        """
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1
