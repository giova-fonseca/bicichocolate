import datetime
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.


class PointSale(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    direction = models.CharField(max_length=250, blank=False)
    telephone = models.CharField(max_length=12)
    logo = models.ImageField(upload_to='logo',blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(PointSale, self).save()

    class Meta:
        verbose_name_plural = "PointSales"


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=250, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(Category, self).save()

    class Meta:
        verbose_name_plural = "Categorys"


class ChocolateType(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(ChocolateType, self).save()

    class Meta:
        verbose_name_plural = "Types"


class Flavor(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=50, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(Flavor, self).save()

    class Meta:
        verbose_name_plural = "Flavors"
              
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    chocolateType = models.ForeignKey(ChocolateType, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=250, blank=False)
    imagen = models.ImageField(upload_to='gallery', blank=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    year_of_validity = models.DateField()
    

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def imageURL(self):
        try:
            url = self.featured.url
        except:
            url = ''
        print('URL:', url)
        return url

    @property
    def only_year(self):
        return self.year_of_validity.strftime('%Y')

    '''
    @admin.display
        def colored_name(self):
            return format_html(
                '<span style="color: #{};">{} {}</span>',
                self.color_code,
                self.first_name,
                self.last_name,
            )
    '''        
                    
    def save(self):
        self.name = self.name.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = "Products"


class Image(models.Model):
    image = models.ImageField(
        upload_to='gallery')
    name = models.CharField(max_length=200)
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



YEAR_CHOICES = []
for r in range(2015, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((r,r))

class ApproveStopModelField(models.DateField):
    pass

class PruebaFecha(models.Model):
    # Other fields
    year_of_validity = models.DateField('Year of Validity', null=True, blank=True)

    '''
    @property
    def yaer_only(self):
        return self.year_of_validity.strftime('%Y')
    '''    