from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


per = Person('sonvi', 13)
tm = Template('Hello {{ p.get_name().upper() }}, age {{ p.get_age()**2 }}')


dic = {'name': 'Frodo', 'age': 123}
tm2 = Template('Name: {{ r.name }}, age: {{ r.age }}')

# {% %} = template specifier
# {{ }} = expression to insert python into template
# {# #} = comment
# # ## = string comment
# return full temp

msg = tm.render(p=per)
msg2 = tm2.render(r=dic)

print(msg)
print(msg2)
