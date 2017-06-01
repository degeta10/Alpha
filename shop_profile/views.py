from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader
from .models import CreateShop
from django.db.models import Q
from .forms import ShopForm,UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'shop_profile/index.html')
            else:
                return render(request, 'shop_profile/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'shop_profile/login.html', {'error_message': 'Invalid login'})
    return render(request, 'shop_profile/login.html')

def create_shop(request):
    if not request.user.is_authenticated():
        return render(request, 'shop_profile/login.html')
    else:
        form = ShopForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.logo = request.FILES['logo']
            file_type = shop.logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'shop': shop,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'shop_profile/create_shop.html', context)
            shop.save()
            return render(request, 'shop_profile/detail.html', {'shop': shop})
        context = {
            "form": form,
        }
        return render(request, 'shop_profile/create_shop.html', context)

def shop_detail(request, shop_id):
    shop = get_object_or_404(CreateShop, pk=shop_id)
    return render(request, 'shop_profile/shop.html', {'shop': shop})



def index(request):
        if not request.user.is_authenticated():
            return render(request, 'shop_profile/login.html')
        else:
            shops = CreateShop.objects.filter(user=request.user)
            query = request.GET.get("q")
            if query:
                shops = shops.filter(
                    Q(bname__icontains=query) |
                    Q(phone__icontains=query)
                ).distinct()
                return render(request, 'shop_profile/index.html', {
                    'shops': shops,
                })
            else:
                return render(request, 'shop_profile/index.html', {'shops': shops} )

class UserFormView(View):
    form_class = UserForm
    template_name = 'shop_profile/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render_to_response('shop_profile/ask.html')


















