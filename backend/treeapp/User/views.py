import string
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from .models import User

# Create your views here.

cosmeticsMap = {
    'Bench': {
        'name': 'Bench',
        'price': 20,
        'path': 'assets/Bench.png'
    },

    'Book': {
        'name': 'Book',
        'price': 5,
        'path': 'assets/Bench.png'
    },

    'LampPost': {
        'name': 'LampPost',
        'price': 10,
        'path': 'assets/LampPost.png'
    },

    'Lantern': {
        'name': 'Lantern',
        'price': 10,
        'path': 'assets/LanternVer2.png'
    }
}

taskList = [
    {
        'name': 'task0',
        'description': 'do some shit',
        'xp': 3
    },

    {
        'name': 'task1',
        'description': 'do some shit?',
        'xp': 3
    },

    {
        'name': 'task2',
        'description': 'do some more shit',
        'xp': 3
    },

    {
        'name': 'task3',
        'description': 'do some shit 3',
        'xp': 3
    },

    {
        'name': 'task4',
        'description': 'do some shit 4',
        'xp': 3
    },

    {
        'name': 'task5',
        'description': 'do some shit 5',
        'xp': 3
    },

    {
        'name': 'task6',
        'description': 'do some shit 6',
        'xp': 3
    },

    {
        'name': 'task7',
        'description': 'do some shit 7',
        'xp': 3
    },

    {
        'name': 'task8',
        'description': 'do some shit 8',
        'xp': 3
    },

    {
        'name': 'task9',
        'description': 'do some shit 9',
        'xp': 3
    },

    {
        'name': 'task10',
        'description': 'do some shit 10',
        'xp': 3
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
        user = User.objects.get(username=request.GET.get('username'))

        if request.GET.get('password') != user.password:
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
                if task:
                    taskOutput.append(taskList[int(task)])

        user.save()

        return JsonResponse({
            'id': user.id,
            'username':user.username,
            'level': user.level,
            'cosmetics': cosmeticObjects,
            'xp': user.xp,
            'lvlxp': user.lvlxp,
            'gold': user.gold,
            'tasks': taskOutput
        })
    
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=401)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def completeTask(request):
    # Getting sent: id, taskName
    data = json.loads(request.body)
    user = User.objects.get(id=data['id'])
    userTasks = split(user.tasks)

    userTasks = [index for index in userTasks if taskList[int(index)]['name'] != data['taskName']]
    user.tasks = join(userTasks)

    user.save()
    
    return JsonResponse({
        "removed": data['taskName'],
        "tasks": userTasks
    })

@csrf_exempt
def buyCosmetic(request):
    # Getting sent: id, item name
    data = json.loads(request.body)
    user = User.objects.get(id=data['id'])
    userCosmetics = split(user.cosmetics)

    newItem = cosmeticsMap[data.itemName]
    userCosmetics.append(newItem['name'])

    user.cosmetics = join(userCosmetics)

    user.save()

    JsonResponse({
        "itemName": newItem['name'],
        "inventory": userCosmetics
    })

    

def join(array):
    if isinstance(array[0], int):
        return ','.join(str(num) for num in array)
    else:
        return ','.join(map(str, array))
    
    
def split(x):
    return x.split(",")

    
