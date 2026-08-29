class Str:
    def __init__(self, s):
        self.s = s
    def upper(self,):
        print(self.s.upper())

s1 = input("Enter a word: ")
obj = Str(s1)

obj.upper()