""" Posts views """
from django.shortcuts import render

# Utilities
from datetime import datetime

hour = datetime.now().strftime('%d , %b , %Y - %H:%M hrs')

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': hour,
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': hour,
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': hour,
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
]


def list_posts(request):
    """ List all posts """
    return render(request, 'feed.html', {'posts': posts})
