from django.shortcuts import render
from .models import Book, Genre
from django.shortcuts import get_object_or_404
# from .forms import CustomUserCreationForm
# books/views.py
from django.shortcuts import render, redirect  # Add redirect import

from .models import Book, SliderImage

def home(request):
    genre_filter = request.GET.get('genre')
    genres = Genre.objects.all()
    
    if genre_filter:
        books = Book.objects.filter(genres__name=genre_filter)
        current_genre = genre_filter
    else:
        books = Book.objects.all()
        current_genre = None
    
    # Get active slider images
    slider_images = SliderImage.objects.filter(is_active=True)
    
    context = {
        'books': books,
        'genres': genres,
        'current_genre': current_genre,
        'slider_images': slider_images,  # Add this line
    }
    
    return render(request, 'books/home.html', context)

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")
    return render(request, 'books/book_detail.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '')
    # Add search logic
    return render(request, 'search_results.html')

# books/views.py
# books/views.py
def home(request):
    genre_filter = request.GET.get('genre')
    featured_books = Book.objects.all()[:5]
    
    if genre_filter:
        books = Book.objects.filter(genres__name__iexact=genre_filter)
    else:
        books = Book.objects.all()
    
    genres = Genre.objects.all()
    return render(request, 'books/home.html', {
        'featured_books': featured_books,
        'books': books,
        'genres': genres,
        'current_genre': genre_filter
    })

from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'books/contact.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, CartItem
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    CartItem.objects.get_or_create(user=request.user, book=book)
    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'books/cart.html', {'items': items})

@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id, user=request.user).delete()
    return redirect('cart')

def account(request):
    return render(request, 'books/account.html')

from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm  # Make sure this matches the class name in forms.py

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Change here
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()  # Change here too
    return render(request, 'books/register.html', {'form': form})

from .models import ContactMessage
from .forms import ContactForm
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'books/contact.html')


from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'books/cart.html', {'cart': cart})


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, BookForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'books/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'books/register.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            form.save_m2m()  # For many-to-many fields
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def privacy(request):
    return render(request, 'books/privacy.html')