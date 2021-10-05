from django.contrib import admin

from testapp.models import MyExampleModel, MyReferencedModel


@admin.register(MyReferencedModel)
class MyExampleModelAdmin(admin.ModelAdmin):
    pass


@admin.register(MyExampleModel)
class MyExampleModelAdmin(admin.ModelAdmin):
    pass
