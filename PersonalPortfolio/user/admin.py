from django.contrib import admin
from .models import profession , SocialLinks,AboutMe,Skills,Workingjourney,ServicesColor,Services,username,JobExperience,Educations,Resent_work,Resent_work_category

# Register your models here.

admin.site.register(username)
admin.site.register(profession)
admin.site.register(SocialLinks)
admin.site.register(AboutMe)
admin.site.register(Skills)
admin.site.register(Workingjourney)
admin.site.register(ServicesColor)
admin.site.register(Services)
admin.site.register(Educations)
admin.site.register(JobExperience)
admin.site.register(Resent_work)
admin.site.register(Resent_work_category)
