from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.


class POS(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)
    direction = models.CharField(max_length=250, blank=False)
    direccion = models.CharField(max_length=250, blank=False)
    telephone = models.CharField(max_length=12)
    logo = models.ImageField(
        upload_to='logo', default='sitio/static/images/no-img.jpg')

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        self.nombre = self.nombre.upper()
        super(POS, self).save()

    class Meta:
        verbose_name_plural = "POS"


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=250, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        self.nombre = self.nombre.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categorys"


class ChocolateType(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        self.nombre = self.nombre.upper()
        super(ChocolateType, self).save()

    class Meta:
        verbose_name_plural = "Types"


class Flavor(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        self.nombre = self.nombre.upper()
        super(Flavor, self).save()

    class Meta:
        verbose_name_plural = "Flavors"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    chocolateType = models.ForeignKey(ChocolateType, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=250, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)
    #image = models.ForeignKey(Image, on_delete=models.CASCADE)
    #image = ImageField(upload_to='whatever')
    price = models.FloatField(default=0)

    def __str__(self):
        return '{} {}'.format(self.name, self.description)

    @property
    def imageURL(self):
        try:
            url = self.featured.url
        except:
            url = ''
        print('URL:', url)
        return url

    def save(self):
        self.name = self.name.upper()
        self.nombre = self.nombre.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = "Products"


class Image(models.Model):
    image = models.ImageField(
        upload_to='gallery', default='sitio/static/images/no-img.jpg')
    name = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        print('URL:', url)
        return url
