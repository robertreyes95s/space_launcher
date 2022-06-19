from django.db import models

class futureLaunch(models.Model):
    title = models.CharField(max_length = 200)
    launch_date = models.CharField(max_length=200)
    launch_info = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.title
   
    class Meta:
        ordering = ['title']

    class Admin:
        pass
    