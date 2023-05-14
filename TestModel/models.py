from django.db import models

# Create your models here.


from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class People(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    name = models.CharField(max_length=20)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    city = models.CharField(max_length=64)
    age = models.IntegerField()


