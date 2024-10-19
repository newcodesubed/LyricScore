from django.db import models

class UploadImage(models.Model):
    caption = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='images', default="file.png")

    def __str__(self):  
        return self.caption  
