from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import *
import requests , re
from django.contrib import messages

def homePageC(request):
    return render(request,'index.html')

def aboutusC(request):
    return render(request,'about.html')

def bookingC(request):
    return render(request,'booking.html')

def contactusC(request):
    return render(request,'contact.html')


def is_valid_email(email):
    # Define the regex pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)


def is_valid_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one lowercase letter, one uppercase letter, and one digit
    if (
        not re.search(r"[a-z]", password)
        or not re.search(r"[A-Z]", password)
        or not re.search(r"\d", password)
    ):
        return False

    # Check if the password contains at least one special character (you can customize the set of special characters)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

def is_valid_phone(phone):
    # Check if the phone number contains exactly 10 digits
    if not re.match(r"^\d{10}$", phone):
        return False
    return True


def registrationC(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        c_pwd = request.POST.get("c_pwd")
        address = request.POST.get("address")
        phone_no = request.POST.get("phone_no")
        email = request.POST.get("email")
        p_document = request.FILES.get("p_document")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already exists!")
            return redirect("/registrationC/")

        if not re.match(r"^\w+$", username):
            messages.error(
                request, "Username can only contain letters, numbers, and underscores"
            )
            return redirect("/registrationC/")

        # Check if the username is between 5 and 20 characters long
        if not (5 <= len(username) <= 20):
            messages.error(request, "Username must be between 5 and 20 characters long")
            return redirect("/registrationC/")

        if not is_valid_email(email):
            messages.error(request, "Please enter a valid email address!")
            return redirect("/registrationC/")

        if not is_valid_password(password):
            messages.info(
                request,
                "Please enter a valid password! The password must be at least 8 characters long and include at least one lowercase letter, one uppercase letter, one digit, and one special character.",
            )
            return redirect("/registrationC/")
        
        if password != c_pwd:
            messages.info(
                request,
                "Password and confirmation password should be same!",
            )
            return redirect("/registrationC/")
        
        if not is_valid_phone(phone_no):
            messages.error(request, "Please enter a valid 10-digit phone number!")
            return redirect("/registrationC/")

        user = User.objects.create(
            username=username,
        )

        # user.set_password(password) to encrypt password
        user.set_password(password)

        user = UserAccount.objects.create(
            email=email,
            address =address,
            phone_no = phone_no,
            personal_document = p_document,
        )
        user.save()
        messages.success(request, "Account created successfully")

        return redirect("/loginC/")
    return render(request,'registration.html')


def loginC(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username doesn't exists!")
            return redirect("/loginC/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(
                request,
                "Incorrect password. Please double-check your password and try again.!",
            )
            return redirect("/loginC/")

        else:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")