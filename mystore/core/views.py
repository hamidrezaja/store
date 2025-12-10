from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import BlogCommentForm
from .models import BlogPost,blogCategory,BlogComment
from django.db.models import Q
# Create your views here.

def header(request):
    return render(request, "includes/header.html", {})
def footer(request):
    return render(request, "includes/footer.html", {})
def home_page(request):
    return render(request, "core/home.html", {})

def login_page(request):
    if request.method == "POST":
        user=request.POST.get("name")
        password=request.POST.get("password")
        user=authenticate(request,username=user,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("home")

    return render(request, "core/login.html", {})
def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        print(new_user)
        return redirect('login')

    return render(request, "core/register.html", {})
def about_us(request):
    return render(request, "core/about.html", {})
def contact_us(request):
    return render(request, "core/contact.html", {})
def faq_page(request):
    return render(request, "core/faq.html", {})
def blog_page(request):
    blog_posts=BlogPost.objects.all()
    if blog_posts:
        paginator=Paginator(blog_posts,5)
        page_number=request.GET.get('page')
        blog_posts=paginator.get_page(page_number)
        context={'page_obj':blog_posts,}
    return render(request, "core/blog.html", context)
def search_blog(request):
    query=request.GET.get('query')
    if not query:
        return redirect('blog')
    qs=BlogPost.objects.prefetch_related('tags').filter(Q(tags__name__icontains=query) | Q(title__icontains=query)).distinct()
    paginator=Paginator(qs,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'page_obj':page_obj,'query':query}
    return render(request, "core/blog.html", context)
def category_blog(request, category_name):
    category=blogCategory.objects.get(name__iexact=category_name)
    blog_posts=BlogPost.objects.filter(categories=category)
    paginator=Paginator(blog_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'page_obj':page_obj,'category':category}
    return render(request, "core/blog.html", context)
def blog_details_page(request, id):
    try:
        post = BlogPost.objects.prefetch_related('comments').get(id=id)
    except BlogPost.DoesNotExist:
        return redirect('blog')
    post = BlogPost.objects.prefetch_related('comments').get(id=id)

    comments=BlogComment.objects.post_comments(post)
    comment_form=BlogCommentForm(request.POST or None)
    key = f"viewed_post_{post.id}"
    if request.method == "GET" and not request.session.get(key, False):
        post.counter_view += 1
        post.save(update_fields=["counter_view"])
        request.session[key] = True
    if request.method =="POST":
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.user=request.user
            new_comment.save()
            return redirect('blog-details', id=post.id)
    context = {'post': post, 'comment_form': comment_form,
                'comments': comments
                }
    return render(request, "core/blog-details.html", context)
def blog_left_sidebar(request):
    favorite_posts=BlogPost.objects.popular_posts()
    category=blogCategory.objects.all()
    context={'favorite_posts':favorite_posts,
             'category': category}
    return render(request, "core/blog_left_sidebar.html", context)
