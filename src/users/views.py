from django.contrib.auth import login, logout, authenticate
from .models import User
from django import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView, View
from django.urls import reverse_lazy
from .forms import UserCreationForm, UserLoginForm


class UserListView(ListView):
    model = User
    template_name = 'auth/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'auth/user_detail.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/user_form.html'
    success_url = reverse_lazy('users:user_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('core:dashboard')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/user_form.html'
    success_url = reverse_lazy('users:user_list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:user_list')


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        print("Login form is valid")
        self.user = form.get_user()
        login(self.request, self.user)
        return redirect('core:dashboard')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Email dan password tidak benar")

        return cleaned_data


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('core:home')


def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.is_staff = True
            user.save()

            login(request, user)
            return redirect('core:dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'auth/admin_signup.html', {'form': form})
