from django import forms
from .models import Car


CHOICES = (
    ('Acura', 'Acura'),
    ('Audi', 'Audi'),
    ('Bentley', 'Bentley'),
    ('BMW', 'BMW'),
    ('Bugatti', 'Bugatti'),
    ('Buick', 'Buick'),
    ('Cadillac', 'Cadillac'),
    ('Chevy', 'Chevy'),
    ('Chrystler', 'Chrystler'),
    ('Dodge', 'Dodge'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('GMC', 'GMC'),
    ('Honda', 'Honda'),
    ('Hyundai', 'Hyundai'),
    ('Infiniti', 'Infiniti'),
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    ('Lamboghini', 'Lamboghini'),
    ('Land Rover', 'Land Rover'),
    ('Lexus', 'Lexus'),
    ('Maserati', 'Maserati'),
    ('Mazda', 'Mazda'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Nissan', 'Nissan'),
    ('Porsche', 'Porsche'),
    ('Rolls Royce', 'Rolls Royce'),
    ('Toyota', 'Toyota'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo')
)

STATES = (
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR' ,'OR'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY')
)


class PostVehicleForm(forms.Form):
    car_img = forms.URLField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text mb-1"
        }))
    year = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text mb-1",
        }))
    make = forms.CharField(
        widget=forms.Select(
            choices=CHOICES, attrs={"class": "input-feild black-text mb-1"}))

    model = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text mb-1"
        }))
    price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text mb-1"
        }))
    mileage = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text mb-1"
        }))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "materialize-textarea black-text mb-1"
        }))

class BuyingCarForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild  black-text mb-1"
        })
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild black-text mb-1",
        })
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild black-text mb-1"
        })
    )
    state = forms.CharField(
        widget=forms.Select(
            choices=STATES, attrs={"class": "input-feild black-text mb-1"}))

    z_code = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild black-text mb-1"
        })
    )
    p_number = forms.RegexField(
         regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
          widget=forms.TextInput(attrs={
            "class" : "input-feild black-text mb-1"
        })   
    )



# forms.py
from django import forms
from .models import Car
from .utils import predict_price

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['engine_size', 'horsepower', 'city_mpg']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        # Calculate the price using the machine learning model
        engine_size = self.cleaned_data['engine_size']
        horsepower = self.cleaned_data['horsepower']
        city_mpg = self.cleaned_data['city_mpg']
        calculated_price = predict_price(engine_size, horsepower, city_mpg)

        # Set the calculated price to the instance
        instance.calculated_price = calculated_price

        if commit:
            instance.save()

        return instance
