from django.contrib.auth.models import User
from django.db import models
#  kita buat dulu modelnya lalu di konfigurasi menggunakan python manage.py makemigrations
# untuk menambah data dan kategori ke proyek kita, kita perlu login ke admin userface
class Category(models.Model):
    name = models.CharField(max_length=255)
    # untuk mengubah nama di Item django administration
    # meta adalah semacam konfigurasi atou opsi untuk model
    # class Meta adalah cara untuk mendefinisikan metadata tambahan untuk model Django Anda. Ini memungkinkan Anda untuk mengontrol berbagai aspek dari perilaku model Anda, seperti membuat model abstrak, menentukan urutan default, menetapkan nama tabel khusus, dan banyak lagi. Dengan menggunakan class Meta, Anda dapat mengkonfigurasi model Anda dengan lebih fleksibel dan sesuai dengan kebutuhan aplikasi Anda.
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
    def __str__(self):
        return self.name

    
