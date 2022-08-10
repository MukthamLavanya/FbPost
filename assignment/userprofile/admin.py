from django.contrib import admin
from .models import User, Education, Company, Achievement

admin.site.register(User),
admin.site.register(Education),
admin.site.register(Company),
admin.site.register(Achievement)
