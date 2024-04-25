from django.contrib import admin

from .models import CustomUser, Task, Complexity, Status

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Complexity)
admin.site.register(Status)