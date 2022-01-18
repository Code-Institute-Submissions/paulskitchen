from django.shortcuts import render, HttpResponse
from .models import UserProfile, Booking, Contact
from .forms import  ContactForm, BookingForm



# Create your views here.
def index(request):
    """landing page entry point"""
    print(request.user)
    print(request.user.email)
    print(dir(request.user))
    # We expect a GET request for the users email client
    if request.method != "GET":
        return HttpResponse(f"<h1>{request.method} is not accepted</h1>")

    return render(request, 'restaurant/index.html', {})

def profile(request):
    """profile page entry point"""
    # We expect a GET request for the users email client
    if request.method == "GET":
        profile = UserProfile.objects.all()
        print(profile)
        return render(request, 'restaurant/profile.html', {})

    if request.method == "POST":
        #Handle incoming form data
        return render(request, 'restaurant/profile.html', {})


      #For all other request types, return not accepted HTML code  
    return HttpResponse(f"<h1>{request.method} is not accepted</h1>")

#Views for pages

"""Function to render contact hmtl page"""
def contact(request):
        return render(request, 'restaurant/contact.html', {})

"""Function to render menu hmtl page"""
def menu(request):
    return render(request, 'restaurant/menu.html', {})

"""Function to render create booking page"""
def create_booking(request):
    print(request.user.username)
    print(request.POST)
    form = BookingForm(request.POST or None)
        

    if request.method == 'POST': 
        if form.is_valid():
            form.save()
        context = {
            'form' : form
        }
        return render(request, "restaurant/manage_bookings.html", context)
    context = {
        'user': request.user,
        'form' : form
    }
    return render(request, 'restaurant/create_booking.html', context)
    

def about(request):
    return render(request, 'restaurant/about.html', {})

def index(request):
    return render(request, 'restaurant/index.html', {})

#function for contact form view

def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request, "/workspace/paulskitchen/templates/restaurant/contact_create.html", context)

#function for booking form view

def delete_booking_view(request, id):
    obj = get_object_or_404(Booking, id=id)
    if request.method == "POST":
        obj.delete()
    content = {
    "object": obj
    }
    return render(request, "/workspace/paulskitchen/templates/restaurant/delete_booking.html", context)

def manage_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user
    )
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/manage_bookings.html', context)