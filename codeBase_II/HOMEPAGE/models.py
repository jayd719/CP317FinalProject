from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    class Types(models.TextChoices):
        SPY  = "spy"
        AGENT = "agent"
    type = models.CharField(gettext_lazy("type"),max_length=20,choices=Types,default=Types.AGENT)
    name = models.CharField(gettext_lazy("Name"),max_length=100,blank=True)
    
class SpyManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset().filter(type = User.Types.SPY)
    
class AgentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(type = User.Types.AGENT)




class Spy(User):
    objects = SpyManager()
    
    def save(self, *args,**kwargs):
        if not self.pk:
            self.type = User.Types.SPY
            return super().save(*args,**kwargs)
    class Meta:
        proxy = True


class Agent(User):
    objects = AgentManager()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.AGENT
        return super().save(*args,**kwargs)
    class Meta:
        proxy = True