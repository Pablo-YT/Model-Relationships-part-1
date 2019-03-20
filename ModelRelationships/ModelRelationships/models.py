from django.db import models
#from .views import 


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.IntegerField()
    date = models.DateField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') 

    def __str__(self):
        return str(self.order_number)

#------------------------------------------------------------------------------------------------------

class role(models.Model):
    role_category = models.CharField(max_length=255)
    role_name = models.CharField(max_length=243) 

    def __str__(self):
        return self.role_name

class play(models.Model):
    play_name = models.CharField(max_length=255)
    role_id = models.ForeignKey(role, on_delete=models.CASCADE, related_name= 'play')
    play_category = models.CharField(max_length=234)

    def __str__(self):
        return self.play_name


class actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    role_id = models.ForeignKey(play, on_delete=models.CASCADE, related_name='actor')

    def __str__(self):
        return self.name


class director(models.Model):
    name = models.CharField(max_length=254)
    play_id = models.ForeignKey(play, on_delete=models.CASCADE, related_name='director')
    actor_id = models.ForeignKey(actor, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.name