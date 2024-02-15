from examples.class_ex import Valami

a = Valami(1, "körte")
a.__str__()
print(a.get_a())
print(a.get_b())
a.set_b("cékla")
a.set_a(3)
a.__str__()
a.inc_a()
a.__str__()
