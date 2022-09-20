class Dictionary:
    def __init__(self,dictionary:dict):
        self.dictionary=dictionary
    def pop(self,params:list[str]):
        try:
            for i in params:
                self.dictionary.pop(i)
        except Exception:
            print(f'Нет такого свойства {i}')
        return self
    def getdict(self):
        return self.dictionary