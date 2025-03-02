from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model) :
    title = models.CharField(max_length=100,verbose_name='电影名')
    description = models.TextField(verbose_name='电影简介')
    image = models.ImageField(upload_to='movie/images/' ,verbose_name='电影海报')
    url = models.URLField(blank=True,verbose_name='电影资源')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class Review(models. Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text