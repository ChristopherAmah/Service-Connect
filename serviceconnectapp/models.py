from django.db import models
from django.contrib.auth.models import User



class Showcase(models.Model):
    show_name = models.CharField(max_length=50)
    show_txt = models.CharField(max_length=250)
    show_img = models.ImageField(upload_to='showcase', default='show.jpg')

    def __str__(self):
        return self.show_name
    
    class Meta:
        db_table = 'showcase'
        managed = True
        verbose_name = 'Showcase'
        verbose_name_plural = 'Showcases'

class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to='category')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    domestic = models.BooleanField(default=False)
    tech = models.BooleanField(default=False)
    events = models.BooleanField(default=False)
    catering = models.BooleanField(default=False)
    hair = models.BooleanField(default=False)
    automobile = models.BooleanField(default=False)
    beauty = models.BooleanField(default=False)
    more = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='providers', default='pix.png', blank=True, null=True)
    # email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='provider_logos', blank=True, null=True)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100, blank=True)
    payment_methods = models.CharField(max_length=255, blank=True)
    social_media_links = models.JSONField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    certifications = models.TextField(blank=True)
    special = models.BooleanField(default=False)
    # average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    # total_ratings = models.PositiveIntegerField(default=0)
    # providers = models.ManyToManyField('Provider', related_name='services')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'
        managed = True
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review for {self.service.name} by {self.user.username}"