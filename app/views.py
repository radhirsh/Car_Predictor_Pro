from django.shortcuts import render
from django.views import View
from sklearn.impute import SimpleImputer
from app import forms
from app import models
from django.shortcuts import redirect, render
import pickle


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, "landing.html",
                      {"car_post": models.VehiclePost.objects.all()})


class PostVehicle(View):
    def get(self, request):
        return render(request, "post-vehicle.html",
                      {"post_form": forms.PostVehicleForm()})

    def post(self, request):
        form = forms.PostVehicleForm(data=request.POST)
        if form.is_valid():
            car_img = form.cleaned_data["car_img"]
            year = form.cleaned_data["year"]
            make = form.cleaned_data["make"]
            model = form.cleaned_data["model"]
            mileage = form.cleaned_data["mileage"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]

            models.VehiclePost.submit_vehicle_post(car_img, year, make, model,
                                                   mileage, price, description)
            return redirect("landing")
        else:
            return render(request, "post-vehicle.html", {"post_form": form})


class VehicleSale(View):
    def get(self, request, id):
        return render(request, "car-page.html",
                      {"car_post": models.VehiclePost.objects.get(id=id)})


class BuyingVehicle(View):
    def get(self, request):
        return render(request, "buy-vehicle.html",
                      {"buy_vehicle": forms.BuyingCarForm()})

    def post(self, request):
        form = forms.BuyingCarForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            z_code = form.cleaned_data["z_code"]
            p_number = form.cleaned_data["p_number"]

            models.BuyVehicle.submit_vehicle_purchase(name, street, city,
                                                      state, z_code, p_number)
            return redirect("receipt")
        else:
            return render(request, "buy-vehicle.html", {"buy-vehicle": form})


class VehicleReceipt(View):
    def get(self, request):
        return render(request, "receipt.html",
                      {"car_receipt": models.BuyVehicle.objects.all()})


class ViewingReceipt(View):
    def get(self, request, id):
        return render(request, "receipt-page.html",
                      {"read_receipt": models.BuyVehicle.objects.get(id=id)})

model = pickle.load(open('./models/New_DT_model.pkl', 'rb'))

def index(request):
    return render(request,"index.html")

def prediction(request):
    if request.method== 'POST':
        engine_size=int(request.POST['engine_size'])
        horsepower =int( request.POST['horsepower'])
        city_mpg = int(request.POST['city_mpg'])



        prediction = model.predict([[engine_size,horsepower,city_mpg]])

        output = round(prediction[0], 2)
        if output < 0:
            return render(request,'index.html',{'prediction_texts':"Sorry you cannot sell this car"})
        else:
            contex={"output":output}
            return render(request,'prediction.html',contex)