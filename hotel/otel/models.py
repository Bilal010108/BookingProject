from django.db import models
from django .contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField
from phonenumber_field.modelfields import PhoneNumberField


STATUS_CHOICES = (
    ('client', 'client'),
    ('owner', 'owner')
)



class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(16),
                                           MaxValueValidator(50)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    status = models.CharField(max_length=17,choices=STATUS_CHOICES,default='client')

    def __str__(self):
       return f'{self.first_name},{self.last_name}'


class Hotel(models.Model):

    hotel_name =models.CharField(max_length=32)
    hotel_owner=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.hotel_name





class HotelPhoto(models.Model):
    hotel_photo = models.ForeignKey(Hotel, related_name='hotel', on_dalete=models.CASCADE)
    hotel_image =models.ImageField(upload_to='hotel_image',null=True,blank=True)


    def __str__(self):
       return self.hotel_photo




class Room(models.Model):
      hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
      room_name = models.CharField(max_length=32)
      description = models.TextField()
      created_date = models.DateTimeField(auto_now_add=True)



      TYPE_CHOICES=(
      ('free', 'free'),
      ('booked', 'booked'),
      ('occupied', 'occupied')
      )

      types = models.CharField(max_length=32, choices=TYPE_CHOICES)

      STATUS_CHOICES=(
          ('двухместный номер', 'двухместный номер'),
          ('трехместный номер', 'трехместный номер'),
          ('Семейный номер', 'Семейный номер')
      )

      status = models.CharField(max_length=32, choices=STATUS_CHOICES)

      def __str__(self):
          return self.room_name


class Review (models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    hotel = models.ForeignKey(Hotel, related_name='review', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Booking(models.Model):
   book_hotel= models.ForeignKey(Hotel,max_length=32,n_delete=models.CASCADE)
   book_room= models.ForeignKey(Room,max_length=32,n_delete=models.CASCADE)
   book_user=models.ForeignKey( UserProfile,max_length=32,n_delete=models.CASCADE)
   entered = models.DateTimeField(auto_now_add=True)
   got_out = models.DateTimeField(auto_now_add=True)
   hotel_price=models.PositiveSmallIntegerField(default=0)

   BOOKING_CHOICES = (
       ('двухместный номер', 'двухместный номер'),
       ('трехместный номер', 'трехместный номер'),
       ('Семейный номер', 'Семейный номер')
   )

   status = models.CharField(max_length=32, choices=BOOKING_CHOICES, max_choices=3)

   def __str__(self):
       return self.book_user















