from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class VehiclePost(models.Model):
    car_img = models.URLField()
    year = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    mileage = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=100)

    # def __str__(self):
    #     return '''
    #     Car Image: {}
    #     Car Make: {}
    #     '''.format(self.car_img, self.make)

    @staticmethod
    def submit_vehicle_post(car_img, year, make, model, mileage, price,
                            description):
        VehiclePost(
            car_img=car_img,
            year=year,
            make=make,
            model=model,
            mileage=mileage,
            price=price,
            description=description).save()


class BuyVehicle(models.Model):
    name = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    z_code = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    p_number = models.CharField(validators=[phone_regex], max_length=10)

    @staticmethod
    def submit_vehicle_purchase(name, street, city, state, z_code, p_number):
        BuyVehicle(
            name=name,
            street=street,
            city=city,
            state=state,
            z_code=z_code,
            p_number=p_number,
        ).save()




class Car(models.Model):
    engine_size = models.FloatField()
    horsepower = models.IntegerField()
    city_mpg = models.FloatField()
