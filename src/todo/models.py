from django.db import models
# Utility that stores the date and time in our Timezone
from django.utils import timezone
# Imports the User - This maps the Task to the Users of our App.(Users as in Admin console)
from django.contrib.auth.models import User


class Task(models.Model):
    T_name = models.CharField(max_length=60)

    T_status = models.BooleanField(default=False)

    T_published = models.DateTimeField(auto_now_add=True,auto_now=False)

    T_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='U_tasks')

    def __str__(self):
        return self.T_name

    class Meta:
        ordering = ('-T_published',)

