from django.contrib import admin
from polls import models as polls_models

# Register your models here).
admin.site.register(polls_models.Users)
admin.site.register(polls_models.Company)