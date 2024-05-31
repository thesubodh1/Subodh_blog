from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) :
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Author"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="post")
    tag = models.ManyToManyField(Tag,null=False)

    def __str__(self):
        return f"{self.title} {self.excerpt} {self.content}"


