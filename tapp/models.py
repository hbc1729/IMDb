from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class admin_table(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    base_price = models.IntegerField()
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    display_type = models.CharField(max_length=200)
    display_size = models.CharField(max_length=200)
    display_resolution = models.CharField(max_length=200)
    refresh_rate = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    rom = models.CharField(max_length=200)
    battery_capacity = models.CharField(max_length=200)
    rear_cameras = models.CharField(max_length=200)
    front_cameras = models.CharField(max_length=200)
    operating_system = models.CharField(max_length=200)
    charger = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200, default="21-10-1999")
    network_connectivity = models.CharField(max_length=200, default="LTE")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Reviews(models.Model):
    username = models.ForeignKey(Users, related_name='Users', default=1, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Product', default=1, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    rating = models.FloatField()

    def __str__(self):
        return str(self.username)
 