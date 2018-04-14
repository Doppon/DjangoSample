from django.db import models

# Create your models here.
class Book(models.Model):
  """書籍"""
  name = models.CharField('書籍名')
  publisher = models.CharField('出版社')
  page = models.IntegerField('ページ数')

class Impresstion(models.Model):
  """感想"""
