django-migreme
==============

A django application to provides filter to short urls with migre.me


Installation
==============
```
pip install django-migreme
```

Usage
==============

Add migreme to your INSTALLED_APPS

Load migreme in your template:
```
{% load migreme %}
```

And use migreme filter:
```
{{ "http://google.com"|migreme }}
```
