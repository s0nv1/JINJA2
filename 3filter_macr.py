from turtle import clear
from jinja2 import Template
# --------------------------------------------------------------
# link https://jinja.palletsprojects.com/en/2.11.x/templates/
# --------------------------------------------------------------


cars = [{'model': 'aud', 'price': 10000},
        {'model': 'bmw', 'price': 25000},
        {'model': 'TESLA', 'price': 50000}
        ]

""" tml = "Sumarnaya cena auto: {{ cr | sum(attribute='price') }}"
tml2 = "Sumarnaya cena auto: {{ (cr | random).model }}"
tml3 = "Sumarnaya cena auto: {{ (cr | max(attribute='price')).price }}"
tm = Template(tml2)
msg = tm.render(cr=cars) """

s = '''
{% filter replace('a', 123) %}
    <a> {{ name }} ahahha </a>
{% endfilter %}'''

# tm = Template(s)
# msg = tm.render(name='ihor')

html = """
{% macro input(name, text='text', value='', size=20) -%}
    <input name='{{ name }}' text='{{ text }}' value='{{ value }}' size='{{ size }}'>
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('passwd') }}
"""

""" tm = Template(html)
msg = tm.render() """


persons = [{'name': 'vasya', 'age': 12, 'weight': 44},
           {'name': 'frank', 'age': 14, 'weight': 55},
           {'name': 'stiv', 'age': 14, 'weight': 42},
           ]

html = """
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.age}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
"""


tm = Template(html)
msg = tm.render(users=persons)
print(msg)
