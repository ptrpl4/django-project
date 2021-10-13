from django.shortcuts import render


example_posts = [
    {
        'author': 'admin',
        'title': 'The beginning',
        'content': 'post content',
        'date_posted': ' Today'
    },
{
        'author': 'user',
        'title': 'The ending',
        'content': 'post content',
        'date_posted': ' Yesterday'
    }
]

def home(request):
    context = {
        'posts': example_posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')