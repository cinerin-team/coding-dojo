class Valami:
    a = 0
    b = "alma"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print('a: ' + str(self.a) + " b: " + self.b)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def inc_a(self):
        self.a += 1
