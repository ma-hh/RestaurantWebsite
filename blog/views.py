from django.shortcuts import render , get_object_or_404
from .models import Blog, Tag, Category, Coments
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def blog_list(request):
    Blogs = Blog.objects.all()

    paginator = Paginator(Blogs, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)

    context = {
        "blog_list" : blog_list
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    blog = Blog.objects.all().get(id=id)
    tags  = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created_at") [:5]
    categories = Category.objects.all()
    comments = Coments.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]

            new_comment = Coments(blog=blog, name = new_name, email=new_email, message=new_message)
            new_comment.save()

    context = {
        "blog" : blog,
        "tags" : tags,
        "recents" : recents,
        "categories" : categories,
        "comments" : comments
    }
    return render(request, "blog/blog_detail.html",context)


def blog_tag(request,tag):
    Blogs = Blog.objects.filter(tag__slug=tag)

    context = {
        "blogs" : Blogs
    }

    return render(request, "blog/blog_list.html", context)

def blog_category(request,category):
    Blogs = Blog.objects.filter(Category__slug=category)

    context = {
        "blogs" : Blogs
    }

    return render(request, "blog/blog_list.html", context)

def search(request):
    if request.method == "GET":
        q = request.GET.get("search")
    blog_list = Blog.objects.filter(title__icontains=q)
    return render (request, "blog/blog_list.html", {"blog_list":blog_list})