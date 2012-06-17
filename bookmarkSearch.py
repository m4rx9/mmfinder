#!/usr/bin/python
import sys

show_path = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/magnus/.mozilla/firefox/ssfbppfu.default/places.sqlite',
        'HOST': '',
        'PORT': '',
        }
    }
from django.conf import settings

settings.configure(DATABASES=DATABASES)

## default value test unless sys.argv is set
if len(sys.argv) == 1:
    phrase = 'test'
else:
    phrase = sys.argv[1].strip()

print 'phrase:', phrase

from orm.models import *
bookmarks = MozBookmarks.objects.all()
c = 0
for b in bookmarks:
    if b.fk == None and b.title != '':  # b.fk = has bookmarks
        try:
            path = b.title.strip()
        except AttributeError:
            print '-- b.title:', b.title
        while b.parent != 1:
            parent = MozBookmarks.objects.get(id=b.parent)
            path = parent.title.strip() + '/' + path
            b = parent
        if show_path:
            print path
        if path.lower().find(phrase.lower()) > -1:
            print path
    c += 1
    #if c>30:
     #   break
