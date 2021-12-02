""" Posts views """
from django.http import HttpResponse

# Utilities
from datetime import datetime

hour = datetime.now().strftime('%d , %b , %Y - %H:%M hrs')

posts = [
    {
        'name': 'Blog Post 1',
        'user': 'User 1',
        'timestamp': hour,
        'picture': 'http://picsum.photos/200/200/?image=10',
    },
    {
        'name': 'Blog Post 2',
        'user': 'User 2',
        'timestamp': hour,
        'picture': 'http://picsum.photos/200/200/?image=20',
    },
    {
        'name': 'Blog Post 3',
        'user': 'User 3',
        'timestamp': hour,
        'picture': 'http://picsum.photos/200/200/?image=30',
    },
]

def list_posts(request):
    """ List all posts """
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <span>{user} -  <small>{timestamp}</small></span>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
