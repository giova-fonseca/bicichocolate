from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=30, blank=False, unique=True)
    descripcion = models.CharField(max_length=250, blank=False)
    
    def __str__(self):
        self.titulo = self.titulo.upper()
        super(Categoria,self).save()
        
    class Meta:
        verbose_name_plural = "Categorias"
        
        
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, verbose_name=("Categorias"), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30, blank=False, unique=True)
    descripcion = models.CharField(max_length=250, blank=False)
    imagen = models.ImageField(default='',blank=True, upload_to='img')
    precio = models.FloatField(default=0)
    
    def __str__(self):
        self.titulo = self.titulo.upper()
        super(Producto, self).save()
        
    class Meta:
        verbose_name_plural = "Productos"
        
        