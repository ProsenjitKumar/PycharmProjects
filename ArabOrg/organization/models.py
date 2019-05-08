from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# -------- Organization type as drop list or category
class OrgType(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to Organization Type name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(OrgType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- State type as drop list or category
class State(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to state name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- City type as drop list or category
class City(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to city name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- Bank Name type as drop list or category
class Bank(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to Bank name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bank, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- Organization All Field
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=200)
    org_short_name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='org_logo/', blank=True)
    address = models.CharField(max_length=260)
    telephone = models.IntegerField(blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=50)
    p_o_box = models.CharField(max_length=80)
    permit_number = models.CharField(max_length=15)
    permit_date = models.CharField(max_length=10)
    board_members = models.TextField()
    info = models.TextField()
    org_types = models.ForeignKey(OrgType, on_delete=models.CASCADE)
    goals = models.TextField()
    projects = models.TextField()
    # permit Issuer
    permit = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    org_links = models.URLField(blank=True)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True)
    bank_account_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_no = models.CharField(max_length=100, unique=True, blank=True)
    bank_account_short_info = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(blank=True,  null=True)
    photo = models.ImageField(upload_to='user_photo/', blank=True, null=True)
    # Created at, updated at by(user name), ip, mac, address
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('org_name',)
        index_together = (('id', 'slug'),)

    # Auto create slug according to Organization name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_name)
        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.org_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Organization.objects.create(user=instance)
    instance.organization.save()






































