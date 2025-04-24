from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .forms import TruckForm, LoadForm




def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    if request.user.role not in ['load_owner', 'truck_owner']:
        return redirect('login')
    
    '''if request.user.role == 'truck_owner':

        my_trucks = Truck.objects.filter(owner=request.user)
        all_loads = Load.objects.all()

        return render(request, 'dashboard_truck.html', {
            'my_trucks': my_trucks,
            'loads': all_loads
        })

    if request.user.role != 'load_owner':

        my_loads = Load.objects.filter(owner=request.user)
        all_trucks = Truck.objects.all()

        return render(request, 'dashboard_load.html', {
            'my_loads': my_loads,
            'trucks': all_trucks
        })'''
    
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def create_truck_view(request):
    if request.user.role != 'truck_owner':
        return redirect('dashboard')

    if request.method == 'POST':
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.owner = request.user
            truck.save()
            return redirect('dashboard')
    else:
        form = TruckForm()
    
    return render(request, 'create_truck.html', {'form': form})

@login_required
def create_load_view(request):
    if request.user.role != 'load_owner':
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoadForm(request.POST)
        if form.is_valid():
            load = form.save(commit=False)
            load.owner = request.user
            load.save()
            return redirect('dashboard')
    else:
        form = LoadForm()
    
    return render(request, 'create_load.html', {'form': form})
