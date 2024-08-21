from django.shortcuts import render, redirect, get_object_or_404
from blog.models import PostModel
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def post_list(request):
    posts = PostModel.objects.order_by("-created_at")
    # user_first_name = request.user.first_name
    context = {
        "posts": posts,
        # "user_first_name": user_first_name,
    }
    return render(request, "blog/post_list.html", context)
 

def post_detail(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    print("......................")
    print( request.user.is_authenticated )
    context = {
        "post": post
    }
    return render(request, "blog/post_detail.html", context)
   

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        else:
            return render(request, "blog/create_post.html", {'form': form})
    return render(request, "blog/create_post.html", {'form': form})    
   
             
             
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'invalid username')
            return redirect('login')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('post_list')
    return render(request, 'blog/login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, 'Username already exist')
            return redirect('register')
        
        user = User.objects.create_user(
           
            username=username    
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, 'Account created succesfully')
        return redirect('login')
    return render(request, 'blog/register.html')     
 
        
        
    
  

def post_edit(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
        else:
            form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
   
      
    

def post_delete(request, id):
    post = get_object_or_404(PostModel, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    context = {
        'post':post
    }
    return render(request, 'blog/confirm.html',context)

   


def logout_view(request):
    logout(request)
    return redirect("post_list")