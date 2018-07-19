from django.db import models
class BukuTamu(models.Model):
    #field2 yang di inisialisasi
    #jangan lupa abis di inisialisasi ketik python manage.py makemigrations
    #maka file migration akan terbuat auto dan setelah itu baru migrate
    uid = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    nama = models.CharField(max_length=100, blank=True, default='')
    alamat = models.TextField()
    bio = models.TextField()
    nomortelepon = models.CharField(max_length=100, blank=True, default='')
    gambar = models.ImageField(upload_to='gambar')
# Create your models here.
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.nama)
