from django.template import RequestContext
from log.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def log(request):
    return render_to_response('log/log.html', {
        'categories': Category.objects.all(),
        'recent_posts': Blog.objects.all()[:5],
    })

def view_post(request, slug):
    return render_to_response('log/view_post.html', {
        'categories': Category.objects.all(),
        'recent_posts': Blog.objects.all()[:5],
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('log/view_category.html', {
        'categories': Category.objects.all(),
        'recent_posts': Blog.objects.all()[:5],
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

# def blog(request):
#   # request the context of the request.
#   # the context contains information such as the client's machine details, for example
#   context = RequestContext(request)

#   # construct a dictionary to pass to the template engine as its context.
#   content = {}

#   return render_to_response('blog/blog.html', content, context)

