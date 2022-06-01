from jinja2 import Template
from markupsafe import escape
# Экранирование. блоки raw, for, if
# {%raw#} ... {%endraw%}

""" data = ('''Modul jinja 
return {{ name }}
pass correct item''')

data2 = '''{% raw %}Modul jinja 
return {{ name }}
pass correct item{% endraw %}'''

tm = Template(data)
tm2 = Template(data2)

msg = tm.render(name='NaMe')
msg2 = tm2.render(name='Name')

print(msg)
print(msg2) """

# show teg in html
""" link = '''Link for html:
<a href='#'> link </a>'''

msg = escape(link)

print(msg) """


# for
# {% for<выражение>-%}
#    <repited text>
# {%endfor%}

# if 
# {%if <condition> %}
#   <if True>
# {% endif %}

""" link = '''<select name='cities'>
{% for c in cities -%}
{% if c.id > 6 %}
    <option value="{{dict['...']}}>{{dict['...']}}</option>
{% elif c.city == 'city' %}
    <optin>{{c['city']}}</option>
{% else %}
    {{dict['...']}}
{%endif%}
{%endfor%}
</select>''' """