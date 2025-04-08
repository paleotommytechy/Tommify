from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, EmailAuthenticationForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.views import LoginView,PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = False 
    authentication_form = EmailAuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, "Invalid email password. Please try again.")
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return str(reverse_lazy('social:home'))
    
class CustomerPasswordResetView(PasswordResetView):
    template_name='password_reset_form.html'
    email_template_name='password_reset_email.html'
    success_url = reverse_lazy("password_reset_done")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                messages.error(self.request, "This email is not registered.")
                return render(self.request, self.template_name, {'form':form})
            return self.form_valid(form)
        return self.form_invalid(form)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        
        #Validate passwords
        if password1 != password2:
            messages.error(request,'Passwords do not match')
            return redirect('register')
        
        #Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')
        
        #Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')
        
        #Create and save user
        user = User.objects.create_user(username=username,email=email, password=password1)
        user.save()

        messages.success(request, 'Registration Successful! You can now log in.')
        return redirect('login')
    return render(request, 'register.html')
    
    
def logout_view(request):
    logout(request)
    return redirect('login')

