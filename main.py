
class Ata:
    hobby = "farmer"
    age = 40
    def info(self):
        return f" {self.hobby}, {self.age}"

class Salima(Ata):
    hobby = "sew"
    age = 20


class Gamila(Ata):
    hobby = "paint"
    age = 15

a = Ata()
sa = Salima()
g = Gamila()
print(a.info())
print(sa.info())
print(g.info())






















