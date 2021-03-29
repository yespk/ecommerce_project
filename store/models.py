from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='brands/')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(default=0)
    mrp = models.FloatField()
    discount = models.FloatField()
    price = models.FloatField()
    image = models.FileField(upload_to=f'products/', null=False)
    # color = models.ManyToManyField()
    # storage = models.IntegerField()
    # highlight = models.TextField()
    short_description = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    meta_title = models.CharField(max_length=200, null=False)
    meta_description = models.TextField(null=False, blank=False)
    meta_keyword = models.CharField(max_length=200)
    added_on = models.DateTimeField("added on")

    def __str__(self):
        return self.name


# class Specification(models.Model):
#     product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
#     in_the_box = models.CharField(max_length=500)
#     model_number = models.CharField(max_length=50)
#     part_number = models.CharField(max_length=50)
#     model_name = models.CharField(max_length=100)
#     series = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     browse_type = models.CharField(max_length=100)
#     suitable_for = models.CharField(max_length=150)
#     Battery_backup = models.CharField(max_length=100)
#     ms_office_provided = models.BooleanField()
#     processor_brand = models.CharField(max_length=100)
#     processor_name = models.CharField(max_length=100)
#     ssd = models.BooleanField()
#     ssd_capacity = models.IntegerField()
#     ram = models.IntegerField()
#     ram_type = models.CharField(max_length=100)
#     processor_variant = models.CharField(max_length=100)
#     clock_speed = models.CharField(max_length=200)
#     cache_size = models.IntegerField()
#     graphic_processor = models.CharField(max_length=100)
#     number_of_cores = models.IntegerField()
#     os_architecture = models.CharField(max_length=10)
#     operating_system = models.CharField(max_length=100)
#     system_architecture = models.CharField(max_length=10)
#     mic_in = models.BooleanField()
#     touchscreen = models.BooleanField()
#     screen_size = models.IntegerField()
#     screen_resolution = models.IntegerField()
#     screen_type = models.CharField(max_length=100)
#     speakers = models.CharField(max_length=100)
#     internal_mic = models.CharField(max_length=100)
#     sound_properties = models.CharField(max_length=100)
#     wireless_LAN = models.CharField(max_length=100)
#     bluetooth = models.CharField(max_length=50)
#     Dimensions = models.CharField(max_length=100)
#     weight = models.CharField(max_length=10)
#     disk_drive = models.CharField(max_length=100)
#     web_camera = models.CharField(max_length=100)
#     fingerprint_sensor = models.CharField(max_length=40)
#     keyboard = models.CharField(max_length=100)
#     backlit_keyboard = models.BooleanField()
#     pointer_device = models.CharField(max_length=100)
#     included_software = models.CharField(max_length=100)
#     laptop_bag = models.BooleanField()
#     additional_features = models.CharField(max_length=200)
#     warranty_summary = models.CharField(max_length=100)
#     warranty_service_type = models.CharField(max_length=100)
#     covered_in_warranty = models.CharField(max_length=100)
#     not_covered_in_warranty = models.CharField(max_length=100)
#     domestic_warranty = models.IntegerField()
