from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

# Create your views here.

cosmeticsMap = {
    'item': 'path'
}

dailies = [
    "task1",
    "task2",
    "task3",
    "task4",
    "task5",
    "task6",
    "task7",
    "task8"
]

@csrf_exempt
def createUser(request):
    try:
        data = json.loads(request.body)

        if User.objects.filter(username=data['username']).exists():
            raise ValueError

        user = User.objects.create(
            username=data['username'],
            password=data['password'],
            level=1,
            xp=0,
            lvlxp=10,
            gold=0,
            day=0,
            achievements=""
        )

        user.save()

        return JsonResponse({
            'id':user.id,
            'username':user.username
        })
    except ValueError:
        return JsonResponse({"Message": "User already exists"})
    except Exception as e:
        return JsonResponse({"Message": str(e)}, status=400)
    
@csrf_exempt
def createDevUser(request):
    try:
        data = json.loads(request.body)

        if User.objects.filter(username=data['username']).exists():
            raise ValueError
        
        user = User.objects.create(
            username = data['username'],
            password = data['password'],
            level = int(data['level']),
            xp = int(data['xp']),
            lvlxp = int(data['lvlxp']),
            gold = int(data['gold']),
            day = int(data['day']),
            cosmetics = data['cosmetics'],
            tasks = data['tasks'],
            achievements = data['achievements']
        )
    except ValueError:
        JsonResponse({"message": "User already exists"}, status=400)
    except Exception as e:
        JsonResponse({"message": str(e)}, status=400)
    
@csrf_exempt
def getUser(request):
    try:
        data = json.loads(request.body)

        user = User.objects.get(username=data['username'])

        if data['password'] != user.password:
            raise ValueError

        paths = []
        cosmetics = separate(user.cosmetics)

        for i in range(len(cosmetics)):
            paths.append(cosmeticsMap[cosmetics[i]])

        

        return JsonResponse({
            'id': user.id,
            'username':user.username,
            'level': user.level,
            'cosmeticPaths': paths,
            'tasks': []
        })
    except User.DoesNotExist:
        return JsonResponse({"Message": "User not found."}, status=404)
    except ValueError as e:
        return JsonResponse({"Message": "Incorrect Password"}, status=401)
    except Exception as e:
        return JsonResponse({"Message": str(e)}, status=400)

def join(array):
    return ','.join(array)
    
def separate(array):
    return array.split(",")
    
