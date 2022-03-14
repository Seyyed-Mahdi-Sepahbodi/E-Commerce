from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

shop_users = get_user_model()

class StoreType(models.Model):
    """Types of shops model"""

    title = models.CharField(max_length=20, verbose_name='Title')
    # image = models.ImageField(upload_to='', verbose_name='Image')
    parent = models.ForeignKey('self', name='child', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Parent Type')
    craeted_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Tag model"""

    title = models.CharField(max_length=30, verbose_name='Tag')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class RegisteredStoreManager(models.Manager):
    """Registered stores manager model"""

    def get_queryset(self):
        return super().get_queryset().filter(status='REG')


class PendingStoreManager(models.Manager):
    """Pending stores manager model"""

    def get_queryset(self):
        return super().get_queryset().filter(status='PEN')


class ShutDownStoreManager(models.Manager):
    """Registered stores manager model"""

    def get_queryset(self):
        return super().get_queryset().filter(status='SHD')


class Store(models.Model):
    """Store model"""

    REGISTERED = 'REG'
    PENDING = 'PEN'
    SHUTDOWN = 'SHD'
    STORE_STATUS_CHOICES = [
        (REGISTERED, 'Registered'),
        (PENDING, 'Pending'),
        (SHUTDOWN, 'Shutdown')
    ]

    name = models.CharField(max_length=20, verbose_name='Name')
    owner = models.ForeignKey(shop_users, verbose_name='Owner', on_delete=models.DO_NOTHING)
    # logo = models.ImageField(upload_to='shop/stores/logos/', verbose_name='Logo')
    store_type = models.ForeignKey(StoreType, verbose_name='Type',on_delete=models.PROTECT, null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number')
    status = models.CharField(
        max_length=3,
        choices=STORE_STATUS_CHOICES,
        default=PENDING,
        verbose_name='Status'
    )

    objects = models.Manager()
    registered_stores = RegisteredStoreManager()
    pending_shops = PendingStoreManager()
    shutdown_shops = ShutDownStoreManager()

    class Meta:
        # unique_together = (('name', 'owner'), ('name', 'store_type'))
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""

    AVAILABLE = 'AVA'
    UNAVAILABLE = 'UNA'
    PRODUCT_STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
    ]

    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    # image = models.ImageField(upload_to='shop/product', verbose_name='Image')
    tag = models.ManyToManyField(Tag, verbose_name='Tag(s)')
    store = models.ForeignKey(Store, verbose_name='Store', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Price', default=0)
    stock = models.PositiveIntegerField(verbose_name='Stock')
    status = models.CharField(
        max_length=3,
        choices=PRODUCT_STATUS_CHOICES,
        default= AVAILABLE,
        verbose_name='Status'
    )
    class Meta:
        # unique_together = ('name', 'store')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # def image_tag(self):
    #     return format_html(f"<img src='{self.image.url}' height='100px' width='100px' style='border-radius: 5px;'")
    # image_tag.short_description = 'تصویر'

    # def set_status(self, cls):
    #     if self.supply > 0:
    #         self.status = cls.AVILABLE
    #     if self.supply == 0:
    #         self.status = cls.UNAVAILABE

    def __str__(self):
        return self.name
