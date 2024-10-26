from django.shortcuts import render, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import *
import requests , re
from django.contrib import messages
from Employee.models import Emp_login


def homePage(request):
    return render(request,'indexe.html')

def aboute(request):
    return render(request,'aboute.html')

def booking_details(request):
    return render(request,'booking_details.html')

def booking_verify(request):
    return render(request,'booking_verifye.html')

def logine(request):
    return render(request,'logine.html')

# def registratione(request):
#       return render(request,'registratione.html')

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


def registratione(request):
    if request.method == "POST":
        vusername = request.POST.get("username")
        vpassword = request.POST.get("password")
        vc_pwd = request.POST.get("c_pwd")
        # address = request.POST.get("address")
        vphone_no = request.POST.get("phone_no")
        vemail = request.POST.get("email")
        vp_document = request.FILES.get("p_document")

        user = Employee_reg.objects.filter(username=vusername)

        if user.exists():
            messages.error(request, "Username already exists!")
            return redirect("/registrationE/")

        if not re.match(r"^\w+$", vusername):
            messages.error(
                request, "Username can only contain letters, numbers, and underscores"
            )
            return redirect("/registrationE/")

        # Check if the username is between 5 and 20 characters long
        if not (5 <= len(vusername) <= 20):
            messages.error(request, "Username must be between 5 and 20 characters long")
            return redirect("/registrationE/")

        if not is_valid_email(vemail):
            messages.error(request, "Please enter a valid email address!")
            return redirect("/registrationE/")

        if not is_valid_password(vpassword):
            messages.info(
                request,
                "Please enter a valid password! The password must be at least 8 characters long and include at least one lowercase letter, one uppercase letter, one digit, and one special character.",
            )
            return redirect("/registrationE/")
        
        if vpassword != vc_pwd:
            messages.info(
                request,
                "Password and confirmation password should be same!",
            )
            return redirect("/registrationE/")
        
        if not is_valid_phone(vphone_no):
            messages.error(request, "Please enter a valid 10-digit phone number!")
            return redirect("/registrationE/")

        user = Employee_reg.objects.create(
            username=vusername,
        )

        # user.set_password(password) to encrypt password
        user.set_password(vpassword)

        user = UserAccount.objects.create(
            email=vemail,
            # address =address,
            phone_no = vphone_no,
            personal_document = vp_document,
        )
        user.save()
        messages.success(request, "Account created successfully")

        return redirect("/loginE/")
    return render(request,'registratione.html')

#login
# def insertlogin(request):
#     if request.method == "POST":
#         empusername = request.POST.get("eusername")
#         emppassword = request.POST.get("epassword")

#         if not Emp_login.objects.filter(eusername=empusername).exists():
#             messages.error(request, "Username doesn't exists!")
#             return redirect("/loginE/")

#         user = authenticate(eusername=empusername, epassword=emppassword)

#         if user is None:
#             messages.info(
#                 request,
#                 "Incorrect password. Please double-check your password and try again.!",
#             )
#             return redirect("/loginE/")

#         else:
#             login(request, user)
#             return redirect("/")

#     return render(request, "logine.html")

# def insertLogin(request):
#     if request.method == "POST":
#         empusername = request.POST.get('eusername')
#         emppassword = request.POST.get('epassword')
        
#         user=Emp_login(username=empusername,password=emppassword)
#         user.save()
#         return render(request,"logine.html")

def insertLogin(request):
    if request.method == "POST":
        empusername = request.POST.get('eusername')
        emppassword = request.POST.get('epassword')
        
        # User ko authenticate karein
        user = authenticate(username=empusername, password=emppassword)
        user.save()
        # Agar user sahi hai to use login karein
        if user is not None:
            login(request, user)
            return redirect('/homepageE/')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "logine.html")