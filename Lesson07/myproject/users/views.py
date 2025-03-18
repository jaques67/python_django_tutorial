from django.shortcuts import render


# Create your views here.
def register_view(request):
    # posts = Post.objects.all().order_by('-date')
    return render(request, 'users/register.html')
