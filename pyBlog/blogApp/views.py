from django.http import HttpResponse
from django.template import loader
from .models import BlogTable
from django.db.models import Q
# Create your views here.
def Blog(request):
    myblog = BlogTable.objects.all().values()
    
    template = loader.get_template('all_blog.html')
    context = {
        'myblog': myblog,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myblog = BlogTable.objects.get(id= id)
    template = loader.get_template('details.html')
    context = {
        'myblog': myblog,
    }
    return HttpResponse(template.render(context, request))

def testBlog(request):
    template = loader.get_template('blogPost.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'fruits': ['Apple', 'Banana', 'Cherry', 'Mango', 'Apricot'],
#     }
#     return HttpResponse(template.render(context, request))

def testing(request):
    # myblog = BlogTable.objects.all()
    # myblog = BlogTable.objects.filter(Q(name='Kashif Iqbal') | Q(name='Rameez Bashir')).values()
    # myblog = BlogTable.objects.filter(name__startswith="S").values
    # myblog=BlogTable.objects.all().order_by('name').values()
    # myblog = BlogTable.objects.all().order_by('-name').values()
    myblog = BlogTable.objects.all().order_by('name', '-id').values()
    template = loader.get_template('template.html')
    context = {
        'blogs': myblog,
    }
    return HttpResponse(template.render(context, request))
