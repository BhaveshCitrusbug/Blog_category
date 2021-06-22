from django.shortcuts import render,redirect
from .models import Blog,Category
from .forms import BlogForm
from django.core.paginator import Paginator


# Create your views here.
def base(request):
    category_data=Category.objects.all()
    return render(request,'base.html',{'category_data':category_data})

def blog_add(request):
    blog_data = BlogForm(request.POST)
    category_data = Category.objects.all()
    if request.method == "POST":
        cate = request.POST["category"]
        title = request.POST["title"]
        description = request.POST["description"]
        author = request.POST["author"]
        category = Category.objects.get(id=cate)
        blog = Blog(category=category,title=title,description=description,author=author)
        blog.save()
        return redirect("index")
    return render(request, "blog_add.html", {"blog": blog_data, "category": category_data})

def view_blog(request,id):
    View_detail=Blog.objects.get(id=id)
    return render(request,'view.html',{'View_detail':View_detail})

def delete(request,id):
    blog_data= Blog.objects.get(id=id)
    blog_data.delete()
    return redirect('index')

def blog_list(request,name=None,datef=None,datet=None,search=None):
    print(search)
    category_data=Category.objects.all()
    sort=request.GET.get('sort','')
    datef=request.GET.get('datef','')
    datet = request.GET.get('datet', '')
    if 'searchData' in request.GET:
        search = request.GET.get('searchData', '')
    date_data=None
    search_data=None
    blog_data=None
    date_search_data=None



    if name and datef and datet and search and sort:
        blog_data=Blog.objects.filter(category__name=name,title__contains=search,publised_date__gte=datef,publised_date__lte=datet).order_by(sort)
    elif name and datef and datet and search:
        blog_data = Blog.objects.filter(category__name=name, title__contains=search, publised_date__gte=datef,
                                        publised_date__lte=datet)
    elif name and datef and datet and sort:
        blog_data = Blog.objects.filter(category__name=name, publised_date__gte=datef,publised_date__lte=datet).order_by(sort)
    elif datef and datet and search and sort:
        blog_data = Blog.objects.filter(title__contains=search, publised_date__gte=datef,
                                        publised_date__lte=datet).order_by(sort)
    elif name and datef and datet:
        blog_data = Blog.objects.filter(category__name=name, publised_date__gte=datef, publised_date__lte=datet)
    elif name and search and sort:
        blog_data = Blog.objects.filter(category__name=name, title__contains=search).order_by(sort)
    elif datef and datet and search:
        date_search_data = Blog.objects.filter(title__contains=search, publised_date__gte=datef,publised_date__lte=datet)
    elif name and search:
        blog_data = Blog.objects.filter(category__name=name, title__contains=search)
    elif datef and datet and sort:
        blog_data = Blog.objects.filter(publised_date__gte=datef,publised_date__lte=datet).order_by(sort)
    elif datef and datet:
        date_data = Blog.objects.filter(publised_date__gte=datef, publised_date__lte=datet)
    elif search and sort:
        blog_data = Blog.objects.filter(title__contains=search).order_by(sort)
    elif name and sort:
        blog_data =Blog.objects.filter(category__name=name).order_by(sort)
    elif search:
        search_data = Blog.objects.filter(title__contains=search)
    elif name:
        blog_data=Blog.objects.filter(category__name=name)
    elif sort:
        blog_data = Blog.objects.all().order_by(sort)
    else:
        blog_data=Blog.objects.all()
    if blog_data:
        paginator = Paginator(blog_data, 2)
        page_number = request.GET.get('page')
        blog_data = paginator.get_page(page_number)
    elif date_data:
        paginator = Paginator(date_data, 2)
        page_number = request.GET.get('page')
        date_data = paginator.get_page(page_number)
    elif search_data:
        paginator = Paginator(search_data, 2)
        page_number = request.GET.get('page')
        search_data = paginator.get_page(page_number)
    elif date_search_data:
        paginator = Paginator(date_search_data, 2)
        page_number = request.GET.get('page')
        date_search_data = paginator.get_page(page_number)

    context={
        'category_data':category_data,
        'blog_data':blog_data,
        'datefrom':datef,
        'dateto':datet,
        'search1':search,
        'date_data':date_data,
        'search_data':search_data,
        'date_search_data':date_search_data

    }
    return render(request,'home.html',context)
