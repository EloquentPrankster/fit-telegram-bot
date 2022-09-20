class Dictionary:
    def __init__(self,dictionary:dict):
        self.dictionary=dictionary
    def pop(self,param:str):
        try:
            self.dictionary.pop(param)
        except Exception:
            print(f'Нет такого свойства {param}')
        return self
    def getdict(self):
        return self.dictionary