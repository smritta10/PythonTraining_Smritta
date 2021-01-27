from django.shortcuts import render, redirect, get_object_or_404
from . models import blog_model
from . forms import ModelForm

# Create your views here.

def blog_posts_view(request, pk, template_name= "BLOG_POSTS/POST_DETAIL.html"):
    blog= get_object_or_404(blog_model, pk=pk)
    return render(request, template_name, {'object':blog})

def blog_posts_list(request):
    blog= blog_model.objects.all()
    context ={"object_list": blog}
    return render(request, "BLOG_POSTS/POST_LIST.html", context)

def blog_posts_create(request):
    form= blog_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts_list')
    return render(request, 'BLOG_POSTS/POST_FORM.html', {'form': form})

def blog_posts_update(request, pk, template_name='BLOG_POSTS/POST_FORM.html' ):
    blog= get_object_or_404(blog_model, pk=pk)
    form= blog_form(request.POST or None, instance=blog)
    if form.is_vaid():
        form.save()
        return redirect('blog_posts_list')
    return render(request, template_name, {'form': form})

def blog_posts_delete(request, pk, template_name='BLOG_POSTS/POST_DELETE.html'):
    blog= get_object_or_404(blog_model, pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_posts_list')
    return render(request, template_name, {'object': blog})

