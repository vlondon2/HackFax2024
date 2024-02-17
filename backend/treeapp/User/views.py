from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from .models import User

# Create your views here.

cosmeticsMap = {
    'item1': {
        'name': 'item',
        'price': 10,
        'path': 'path/to/item'
    },
    'item2': {
        'name': 'item2',
        'price': 200,
        'path': 'path/to/item2'
    }
}

taskList = [
    {
        'name': 'task1',
        'description': 'do some shit?',
        'xp': 25
    },

    {
        'name': 'task2',
        'description': 'do some more shit',
        'xp': 25
    },

    {
        'name': 'task3',
        'description': 'do some shit 3',
        'xp': 25
    },

    {
        'name': 'task4',
        'description': 'do some shit 4',
        'xp': 25
    },

    {
        'name': 'task5',
        'description': 'do some shit 5',
        'xp': 25
    },

    {
        'name': 'task6',
        'description': 'do some shit 6',
        'xp': 25
    },

    {
        'name': 'task7',
        'description': 'do some shit 7',
        'xp': 25
    },

    {
        'name': 'task8',
        'description': 'do some shit 8',
        'xp': 25
    },

    {
        'name': 'task9',
        'description': 'do some shit 9',
        'xp': 25
    },

    {
        'name': 'task10',
        'description': 'do some shit 10',
        'xp': 25
    }

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
            achievements="",
            cosmetics = "",
            tasks = ""
        )

        user.save()

        return JsonResponse({
            'id':user.id,
            'username':user.username
        })
    except ValueError:
        return JsonResponse({"error": "User already exists"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
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
            tasks = data['tasks'],
            achievements = data['achievements'],
            cosmetics = data['cosmetics']
        )
    except ValueError:
        JsonResponse({"error": "User already exists"}, status=400)
    except Exception as e:
        JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def getUser(request):
    try:
        data = json.loads(request.body)

        user = User.objects.get(username=data['username'])

        if data['password'] != user.password:
            raise ValueError    

        cosmeticObjects = []

        if user.cosmetics != "":
            for cosmetic in split(user.cosmetics):
                cosmeticObjects.append(cosmeticsMap[cosmetic])

        taskOutput = []

        if user.tasks == "":
            newTasks = []

            while len(newTasks) < 4:
                num = random.randint(0,len(taskList)-1)
                if (num not in newTasks):
                    newTasks.append(num)
                    taskOutput.append(taskList[num])
            
            user.tasks = join(newTasks)
        else:
            for task in split(user.tasks):
                taskOutput.append(taskList[int(task)])


        return JsonResponse({
            'id': user.id,
            'username':user.username,
            'level': user.level,
            'cosmetics': cosmeticObjects,
            'tasks': taskOutput
        })
    
    except User.DoesNotExist:
        return JsonResponse({"eror": "User not found."}, status=404)
    except ValueError as e:
        return JsonResponse({"error": "Incorrect Password"}, status=401)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    


def join(array):
    return ','.join(array)
    
def split(array):
    return array.split(",")

    
