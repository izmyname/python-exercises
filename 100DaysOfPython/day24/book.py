class Book:
    def __init__(self,title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, smh):
        if isinstance(smh, bool):
            self._available = smh
        else:
            print("Must use bool")
        
    def summary(self):
        print(f"TItle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nAvailable: {self.available}")
    
    def borrow(self):
        if self.available == True:
            self.available = False
            print("Enjoy your reading")
        else:
            print("Sorry, the book is not available ")
            
            
necrobook = Book("Necromancy for beginners", "izmyname", 2025, True)

bloodbook = Book("Introduction to blood magic", "someoneelse", 2022, True)

bloodbook.borrow()

bloodbook.summary()

bloodbook.borrow()