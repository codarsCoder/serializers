from django.db import models

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model):   # related_name='students'  ile bu modeli path üzerinden istediğimiz  path modelinde çağıracağız  yani burası path_id ile kayıt edilecek , path modei sıralanırken buradan path_id ile uyuşan data yı studen ile alabileceğiz  örneği serializers.py de var 
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE) #override yaptık ...burada üstte tanımlanmış olan path_name klası path olarak field yapılmış
    first_name = models.CharField(max_length=30) ## üsttek on_delete sayesinde bu path silinirse bu path ile kaydedilmiş tüm veriler buradan  silincek 
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.last_name} {self.first_name}"