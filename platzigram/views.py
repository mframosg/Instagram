from django.http import HttpResponse
import json
from django.http import JsonResponse

def helloWorld(request):
    return HttpResponse('Hello World!')

def numbers(request):
    array = request.GET['numbers'].split(',')
    array = list(map(int, array))
    array.sort()
    data = {
        'status' : 'ok',
        'numbers' : array,
        'total' : sum(array),
        'message' : 'Integer successfully sorted'
    }
    #return HttpResponse(json.dumps(data, indent = 4) , content_type='application/json')
    return JsonResponse(data, safe=False)

def hi(request, name, age):
    # if age < 18:
    #     message = 'Sorry {}, you are not old enough'.format(name)
    # else:
    #     message = 'Welcome {}!'.format(name)
    # return HttpResponse(message)
    message = 'Welcome {}!'.format(name) if int(age) >= 18 else 'Sorry {}, you are not old enough'.format(name)

    return HttpResponse(message)

    