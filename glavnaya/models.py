from django.db import models
from django.utils import timezone
import datetime


class New(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    preview=models.TextField(max_length=200)
    published=models.DateTimeField(blank=True, null=True)

    def publish_now(self):
        now=self.published.date()
        return now.strftime('%d.%m.%Y')

    def __str__(self):
        return f" id-{self.id}_{self.title}"

class  Team(models.Model):
    TRENER = 'Тренер'
    SOTRUDNIK = 'Сотрудник'
    STATUS = ((TRENER, 'Тренер'), (SOTRUDNIK, 'Сотрудник'),)
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default=TRENER,)
    name = models.CharField(max_length=150)
    place = models.TextField(default=' ')
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return f" {self.name}_{self.status}"

class  Kurs(models.Model):
    ON = 'Онлайн'
    OFF = 'Очный'
    STATUS = ((ON, 'Онлайн'), (OFF, 'Очный'),)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=OFF,)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f" {self.name}_{self.status}"


class  Faq(models.Model):
    question = models.TextField(max_length=500)
    answer = models.TextField()
    url = models.URLField(blank=True, null=True, help_text="не обязательно")
    urlname=models.TextField(blank=True, null=True, help_text="не обязательно")

    def __str__(self):
        return f" {self.question}"


#class Foto(models.Model):
#    image = StdImageField(upload_to=UploadToClassNameDirUUID())
#    place = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
#
#    def __str__(self):
#        return SafeText('<img src="{0}" />'.format(self.image.thumbnail.url))
#
#    class Meta:
#        ordering = ('id',)
#        verbose_name = 'Fotka'
#        verbose_name_plural = 'Fotky'
