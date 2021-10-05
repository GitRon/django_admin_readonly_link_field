from django.db import models


class MyReferencedModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MyExampleModel(models.Model):
    name = models.CharField(max_length=50)
    referenced_model = models.ForeignKey(MyReferencedModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
