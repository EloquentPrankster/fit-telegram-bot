class Dictionary:
    def __init__(self,dictionary:dict):
        self.dictionary:dict=dictionary
    def pop(self,params:list[str]):
        for i in params:
            try:
                self.dictionary.pop(i)
            except:
                continue
        return self

    def clear(self):
        self.dictionary.clear()
        return self

    def update(self,updict:dict):
        self.dictionary.update(updict)
        return self
    def getdict(self):
        return self.dictionary