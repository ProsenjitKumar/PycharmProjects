from django.contrib.gis.db import models
from django.utils.text import slugify


class Kingdom(models.Model):
    kingdom = models.CharField(max_length=40, default='Animalia')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kingdom)
        super(Kingdom, self).save(*args, **kwargs)

    def __str__(self):
        return self.kingdom


class Phylum(models.Model):
    phylum = models.CharField(max_length=40)
    kingdom = models.CharField(max_length=40, default='Animalia')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.phylum)
        super(Phylum, self).save(*args, **kwargs)

    def __str__(self):
        return self.phylum


class Class(models.Model):
    birds_class = models.CharField(max_length=40)
    phylum = models.ManyToManyField(Phylum, help_text='Select Phylum Name...')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.birds_class)
        super(Class, self).save(*args, **kwargs)

    def __str__(self):
        return self.birds_class


class Order(models.Model):
    order = models.CharField(max_length=40)
    bird_class = models.ManyToManyField(Class, help_text='Select Class Name...')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.order)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order


class FamilyAuthor(models.Model):
    family_author = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.family_author)
        super(FamilyAuthor, self).save(*args, **kwargs)

    def __str__(self):
        return self.family_author


class Family(models.Model):
    family = models.CharField(max_length=40)
    family_author = models.ManyToManyField(FamilyAuthor, help_text='Select Family Author ...')
    order = models.ManyToManyField(Order, help_text='Select Order Name...')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.family)
        super(Family, self).save(*args, **kwargs)

    def __str__(self):
        return self.family


class GenusAuthor(models.Model):
    genus_author = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genus_author)
        super(GenusAuthor, self).save(*args, **kwargs)

    def __str__(self):
        return self.genus_author


class Genus(models.Model):
    genus = models.CharField(max_length=40)
    genus_author = models.ManyToManyField(GenusAuthor, help_text='Select Genus Author name ... ')
    family = models.ManyToManyField(Family, help_text='Select Family Name...')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genus)
        super(Genus, self).save(*args, **kwargs)

    def __str__(self):
        return self.genus


class Status(models.Model):
    status = models.CharField(max_length=20)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.status)
        super(Status, self).save(*args, **kwargs)

    def __str__(self):
        return self.status


class DistributionOfBengal(models.Model):
    distribution_in_bengal = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.distribution_in_bengal)
        super(DistributionOfBengal, self).save(*args, **kwargs)

    def __str__(self):
        return self.distribution_in_bengal


# class Birds(models.Model):
#     kingdom = models.CharField(max_length=40)
#     phylum = models.ManyToManyField(Phylum, help_text='Select Phylum Name...')
#     bird_class = models.ManyToManyField(Class, help_text='Select Class Name...')
#     order = models.ManyToManyField(Order, help_text='Select Order Name...')
#     family = models.ManyToManyField(Family, help_text='Select Family Name...')
#     family_author = models.ManyToManyField(FamilyAuthor, help_text='Select Family Author name ... ')
#     genus = models.ManyToManyField(Genus, help_text='Select Genus name ..')
#     genus_author = models.ManyToManyField(GenusAuthor, help_text='Select Genus Author name ... ')
#     scientific_name = models.CharField(max_length=50)
#     scientific_name_author = models.CharField(max_length=40)
#     year = models.PositiveIntegerField()
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)
#     accepted_as = models.CharField(max_length=70)
#     bengali_name = models.CharField(max_length=100)
#     english_name = models.CharField(max_length=100)
#     size_cm = models.PositiveIntegerField()
#     common_family = models.CharField(max_length=40)
#     common_group = models.CharField(max_length=40)
#     habit = models.CharField(max_length=20)
#     conservation_status = models.CharField(max_length=10)
#     distribution_in_bengal = models.ManyToManyField(DistributionOfBengal, help_text='Select Place ..')
#     reference = models.CharField(max_length=500)

class Birds(models.Model):
    kingdom = models.CharField(max_length=40)
    phylum = models.CharField(max_length=70)
    bird_class = models.CharField(max_length=70)
    order = models.CharField(max_length=70)
    family = models.CharField(max_length=70)
    family_author = models.CharField(max_length=70)
    genus = models.CharField(max_length=70)
    genus_author = models.CharField(max_length=70)
    scientific_name = models.CharField(max_length=50)
    scientific_name_author = models.CharField(max_length=40)
    year = models.IntegerField()
    status = models.CharField(max_length=70)
    accepted_as = models.CharField(max_length=70)
    bengali_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    size_cm = models.CharField(max_length=10)
    common_family = models.CharField(max_length=40)
    common_group = models.CharField(max_length=40)
    habit = models.CharField(max_length=20)
    conservation_status = models.CharField(max_length=10)
    distribution_in_bengal = models.CharField(max_length=70)
    reference = models.CharField(max_length=500)

    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kingdom)
        super(Birds, self).save(*args, **kwargs)

    def __str__(self):
        return self.kingdom
