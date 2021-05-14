from django.shortcuts import render, HttpResponse, redirect
import random
from django.core.files.storage import FileSystemStorage
from . models import *
from django.http import JsonResponse
import json
import time
# Create your views here.


def index(request):
    if(request.session.has_key('user')):
        username = request.session['user']
    else:
        username = False
    context = {'username': username}
    print(context)
    return render(request, "tapp/main.html", context)


def home(request):
    try:
        if(request.session.has_key('productId')):
            del request.session['productId']
        products = Product.objects.all()
        if(request.session.has_key('user')):
            username = request.session['user']
        else:
            username = False
        context = {'products': products, 'username': username}
    except:
        pass
    return render(request, 'tapp/home.html', context)


def productView(request):
    avg = 0
    time.sleep(0.3)
    print("party")
    if(request.session.has_key('user')):
        username = request.session['user']
        reviewText = "Write Your Review"
        readonly = ""
        disabled = ""
    else:
        username = False
        reviewText = "Login to Review"
        readonly = "readonly"
        disabled = "disabled"
    if request.session.has_key('productId'):
        productId = int(request.session['productId'])
        print(productId)
        product = Product.objects.get(id=productId)
        try:
            review = request.POST['review']
            rating = request.POST['rating']
            rating = float(rating)
            userData = Users.objects.get(username=username)
            reviewData, created = Reviews.objects.get_or_create(
                username=userData, product=product, review=review, rating=rating)
            #print(reviews)
            #print(review, '\n', rating, '\n', username, '\n', product)
        except Exception as e:
            pass
        try:
            reviews = Reviews.objects.filter(product=product)
            avg = sum([review.rating for review in reviews])/len(reviews)
        except:
            pass
        cards_colors = ['bg-primary', 'bg-secondary', 'bg-success',
                        'bg-danger', 'bg-warning', 'bg-info', 'bg-dark']
        context = {'list': list(range(25)), 'cards_colors': cards_colors, 'product': product,
                   'username': username, 'reviewText': reviewText, 'readonly': readonly, 'disabled': disabled, 'reviews':list(reviews), 'avg':avg}
        return render(request, 'tapp/productview.html', context)
    else: 
        return render(request, 'tapp/404.html',{})




def admin_home(request):
    print('Hello')
    key = request.session.has_key('admin')
    print(key, type(key))
    if(request.session.has_key('admin')):
        return render(request, 'tapp/admin_home.html', context={'key':key})
    else:
        return HttpResponse( "<script>alert('Please Login!'); window.location = '/cpanel/';</script>")
    


def admin_addproducts(request):
    if not request.session.has_key('admin'):
        return HttpResponse( "<script>alert('Please Login!'); window.location = '/cpanel/';</script>")
    else:
        try:
            product_name = request.POST['name']
            category = request.POST['category']
            base_price = request.POST['price']
            manufacturer = request.POST['manufacturer']
            model = request.POST['model']
            processor = request.POST['processor']
            display_type = request.POST['displaytype']
            display_size = request.POST['displaysize']
            display_resolution = request.POST['displayres']
            refresh_rate = request.POST['refreshrate']
            ram = request.POST['ram']
            rom = request.POST['rom']
            battery_capacity = request.POST['battery']
            rear_cameras = request.POST['rearc']
            front_cameras = request.POST['frontc']
            operating_system = request.POST['os']
            charger = request.POST['charger']
            release_date = request.POST['release_date']
            network = request.POST['network']
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            phone, created = Product.objects.get_or_create(product_name=product_name, category=category, base_price=base_price, manufacturer=manufacturer, model=model, processor=processor, display_type=display_type, display_size=display_size, network_connectivity=network, release_date=release_date,
                                                        display_resolution=display_resolution, refresh_rate=refresh_rate, ram=ram, rom=rom, battery_capacity=battery_capacity, rear_cameras=rear_cameras, front_cameras=front_cameras, operating_system=operating_system, charger=charger, image=image)
            print(phone, created)
            return redirect(admin_home)
        except Exception as e:
            print(e)
        return render(request, 'tapp/admin_addproducts.html', context={})


def admin_updateproducts(request):
    return render(request, 'tapp/admin_updateproducts.html', context={})


def fetch_productId(request):
    data = json.loads(request.body)
    action = data['action']
    productId = data['productId']
    request.session['productId'] = productId
    print(productId, action)
    return JsonResponse('Hello', safe=False)


def login(request):
    try:
        username = request.POST['inusername']
        password = request.POST['inpassword']
        user = Users.objects.get(username=username, password=password)
        request.session['user'] = user.username
        return HttpResponse( "<script>alert('Welcome "+ username +"!'); window.location = '/';</script>")
    except:
        return HttpResponse( "<script>alert('Username or password or both are incorrect!'); window.location = '/';</script>")
    #return redirect(home)


def signup(request):
    email = request.POST['upemail']
    username = request.POST['upusername']
    password = request.POST['uppassword']
    user, created = Users.objects.get_or_create(
        username=username, email=email, password=password)
    request.session['user'] = user.username
    return redirect(home)


def delete_product(request):
    if not request.session.has_key('admin'):
       return HttpResponse( "<script>alert('Please Login!'); window.location = '/cpanel/';</script>")
    try:
        if(request.session.has_key('productId')):
            del request.session['productId']
        products = Product.objects.all()
        if(request.session.has_key('user')):
            username = request.session['user']
        else:
            username = False
        context = {'products': products, 'username': username}
    except:
        pass
    return render(request, 'tapp/delete_product.html', context)

def delete(request):
    try:
        if(request.session.has_key('productId')):
            productId = request.session['productId']
            product = Product.objects.get(id=int(productId))
            print(product.product_name)
            product.delete()
    except Exception as e:
        print(e)
    return redirect(delete_product)


def admin_logout(request):
    del request.session['admin']
    return redirect(cpanel)

def your_reviews(request):
    if(request.session.has_key('user')):
        username = request.session['user']
        user = Users.objects.get(username=username)
        reviews = Reviews.objects.filter(username=user)
        context = {'reviews': list(reviews)}
        return render(request, 'tapp/your_reviews.html', context)
    else:
        return render(request, 'tapp/404.html', context={})


def logout(request):
    del request.session['user']
    return redirect(home)

def fetch_reviewId(request):
    data = json.loads(request.body)
    reviewId = data['reviewId']
    print(reviewId)
    review = Reviews.objects.get(id=int(reviewId))
    review.delete()
    return JsonResponse('Hello', safe=False)

def budget(request):
    try:
        if(request.session.has_key('productId')):
            del request.session['productId']
        products = Product.objects.filter(category="Budget")
        if(request.session.has_key('user')):
            username = request.session['user']
        else:
            username = False
        context = {'products': products, 'username': username}
    except:
        pass
    return render(request, 'tapp/budget.html', context)

def flagship(request):
    try:
        if(request.session.has_key('productId')):
            del request.session['productId']
        products = Product.objects.filter(category="Flagship")
        if(request.session.has_key('user')):
            username = request.session['user']
        else:
            username = False
        context = {'products': products, 'username': username}
    except:
        pass
    return render(request, 'tapp/flagship.html', context)

def mid_range(request):
    try:
        if(request.session.has_key('productId')):
            del request.session['productId']
        products = Product.objects.filter(category="Mid-Range")
        if(request.session.has_key('user')):
            username = request.session['user']
        else:
            username = False
        context = {'products': products, 'username': username}
    except:
        pass
    return render(request, 'tapp/mid_range.html', context)


def cpanel(request):
    if(request.session.has_key('admin')):
        return redirect(admin_home)
    try:
        username = request.POST['username']
        password = request.POST['passwd']
        admin = admin_table.objects.get(admin_name=username, admin_password=password)
        print(admin)
        if(admin):
            request.session['admin'] = True
            #return HttpResponse( "<script>window.location = '/admin_home/';</script>")
            return redirect(admin_home)
            # return render(request, 'tapp/admin_home.html', context={})
        else:
            raise RuntimeError
    except:
        pass
    return render(request, 'tapp/cpanel.html', context={})


def load(request):
        return render(request, 'tapp/loading.html')

def landing_page(request):
    return render(request, 'tapp/landing_page.html')