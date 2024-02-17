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
        'price': 25,
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
        'name': 'Recycle',
        'description': 'Recycle something today.',
        'xp': 3
    },
    {
        'name': 'Carpool',
        'description': 'Carpool with a friend.',
        'xp': 6
    },

    {
        'name': 'Pick up litter',
        'description': 'Pick up a piece of litter.',
        'xp': 5
    },

    {
        'name': 'Reusable Bag',
        'description': 'Use a reusable bag instead of a plastic bag.',
        'xp': 2
    },

    {
        'name': 'Short shower',
        'description': 'Take a 10 minute shower.',
        'xp': 3
    },

    {
        'name': 'Stay Informed',
        'description': 'Read an article about recent environmental news.',
        'xp': 5
    },

    {
        'name': 'Save Electricity',
        'description': 'Make sure all your lights are off before you leave for the day.',
        'xp': 3
    },

    {
        'name': 'Save Water',
        'description': 'Turn off the faucet when you brush your teeth.',
        'xp': 2
    },

    {
        'name': 'Donate',
        'description': 'Donate an old item you don\'t use anymore.',
        'xp': 10
    },

    {
        'name': 'Bike',
        'description': 'Bike or walk to a destination instead of driving.',
        'xp': 5
    },

    {
        'name': 'Bus',
        'description': 'take the bus instead of driving.',
        'xp': 5
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
    if len(userTasks) != 0:
        user.tasks = join(userTasks)
    else:
        user.tasks = ""

    # Get xp
    for task in taskList:
        if task['name'] == data['taskName']:
            user.xp += task['xp']

    # Check if leveled up
    if user.xp >= user.lvlxp:
        user.level += 1
        user.xp -= user.lvlxp
        user.lvlxp = user.level*10
        user.gold += 5



    user.save()
    
    return JsonResponse({
        "removed": data['taskName'],
        "tasks": userTasks,
        "xp": user.xp,
        "level": user.level,
        "lvlxp": user.lvlxp
    })

@csrf_exempt
def buyCosmetic(request):
    # Getting sent: id, item name
    data = json.loads(request.body)
    user = User.objects.get(id=data['id'])

    userCosmetics = split(user.cosmetics)
    userCosmetics.append(data['itemName'])
    user.cosmetics = join(userCosmetics)

    user.save()

    JsonResponse({
        "username"
        "itemName": data['itemName'],
        "inventory": userCosmetics
    })

    

def join(array):
    if isinstance(array[0], int):
        return ','.join(str(num) for num in array)
    else:
        return ','.join(map(str, array))
    
    
def split(x):
    return x.split(",")

    
