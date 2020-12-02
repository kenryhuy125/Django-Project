import os

os.environment.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print("Topic ID:", topic.id, "Topic:", topic)


t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all()  #access entry by using t because there is a relation between entry and Topic

for entry in entries:
    print(entry)


from djnago.contrib.auth.models import User
for user in User.objects.all():
    print(user.username, user.id)