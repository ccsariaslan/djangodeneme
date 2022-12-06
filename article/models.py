from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class article(models.Model):
    
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=60,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma zamanı")
    artimg = models.FileField(blank = True,null = True ,verbose_name = "Görsel ekle")
    
    def __str__(self) -> str:
            return self.title
    

    
    
class Comment(models.Model):
    
    makale = models.ForeignKey(article,on_delete= models.CASCADE,verbose_name = "Makale",related_name="comments")
    
    commentauthor = models.CharField(max_length=50,verbose_name="isim")
    commentarea   = models.CharField(max_length=300,verbose_name="yorum")
    commentdate   = models.DateTimeField(auto_now_add=True,verbose_name="yorum tarihi")    
    
    def __str__(self):
        return self.commentarea

    
    

    