from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others')
    )
   
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
           
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
           
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name=models.CharField( max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    state=models.CharField(max_length=15,choices=STATE_CHOICES,null=True,blank=True)
    mobile_number=models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin