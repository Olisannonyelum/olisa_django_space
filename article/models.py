from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
import random
from django.dispatch import receiver
from django.urls import reverse 
from django.db.models import Q
from django.conf import settings



user = settings.AUTH_USER_MODEL

class articlequeryset(models.QuerySet):
    def search(query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(titile__icontains=query)| Q(content__icontains=query)
        return self.filter(lookups)
 
class article_manager(models.Manager):
    def get_queryset(self):
        return articlequeryset(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset()#.search(query=query)

# Create your models here.
class article(models.Model): #this model enable us to interect with a database or craete a database field that can store data
    user = models.ForeignKey(user, blank=True, null=True, on_delete=models.SET_NULL)#auth.user....> was here 
    title = models.CharField(unique=True, max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True) 
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)

    objects = article_manager()

    def get_absolute_url(self):
        #return f'/articles/{self.slug}' 
        # print('this shit is not worcking at all boy')
        return reverse("article:detail", kwargs={'slug': self.slug})
        

    def save(self, *args, **kwargs):
        # if self.slug is None:
            # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# def article_pre_save(*args, **kwargs):
    # print('pre_save')
    # print(args, kwargs)
    # obj = kwargs.get('instance')
    # print('..............', obj.title)

    # if obj.slug is None:
    #     obj.slug = slugify(obj.title)

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
        Klass = instance.__class__
        qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
        if qs.exists():
            rand_int = random.randint(300_000, 500_000)
            slug = f"{slug}-{rand_int}"
            return slugify_instance_title(instance, save=save, new_slug=slug)
        instance.slug = slug
        if save:
            instance.save()
        return instance

        

def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save') 
    # print(instance) 
    print(dir(instance))
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=article)

def article_post_save(sender, created, instance, *args, **kwargs): 
    print('post_save')
    if created:
        # instance.slug = "this is my slug!"
        # instance.save()
        slugify_instance_title(instance, save=True)
        

post_save.connect(article_post_save, sender=article)

# @receiver(pre_save, sender=article)
# def ramdom_save(sender, instance, **kwargs):
#     instance.slug = slugify(instance.title)
