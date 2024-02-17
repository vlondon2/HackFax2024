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
        'price': 10,
        'requiredlvl': 2,
        'path': 'assets/Bench.png'
    },

    'Book': {
        'name': 'Book',
        'price': 5,
        'requiredlvl': 1,
        'path': 'assets/Book.png'
    },

    'Lamp Post': {
        'name': 'Lamp Post',
        'price': 15,
        'requiredlvl': 1,
        'path': 'assets/LampPost.png'
    },

    'Lantern': {
        'name': 'Lantern',
        'price': 5,
        'requiredlvl': 1,
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
        'name': 'Pick up Litter',
        'description': 'Pick up a piece of litter.',
        'xp': 5
    },

    {
        'name': 'Reusable Bag',
        'description': 'Use a reusable bag instead of a plastic bag.',
        'xp': 2
    },

    {
        'name': 'Short Shower',
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
        'description': 'Take the bus instead of driving.',
        'xp': 5
    }

]

achievementsMap = {
    'Newbie': {
        'name': 'Newbie',
        'description': 'Complete your first daily task.'
    },
    'Bronze': {
        'name': 'Bronze',
        'description': 'Complete 5 daily tasks.'
    },
    'Silver': {
        'name': 'Silver',
        'description': 'Complete 10 daily tasks.'
    },
    'Gold': {
        'name': 'Gold',
        'description': 'Complete 20 daily tasks'
    },
    'High Roller': {
        'name': 'High Roller',
        'description': 'Own every item.'
    }
}

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
            taskCount=0,
            achievements="",
            cosmetics = "",
            tasks = ""
        )

        taskOutput = []
        newTasks = []

        while len(newTasks) < 4:
            num = random.randint(0,len(taskList)-1)
            if (num not in newTasks):
                newTasks.append(num)
                taskOutput.append(taskList[num])
            
            user.tasks = join(newTasks)

        user.save()

        return JsonResponse({
            'id':user.id,
            'username':user.username,
            'tasks': taskOutput
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

        return JsonResponse({
            "username": user.username,
            "password": user.level,
            'level': user.level,
            'xp': user.xp,
            'lvlxp': user.lvlxp,
            'gold': user.gold,
            "tasks": user.tasks,
            "cosmetics": user.cosmetics
        })
    except ValueError:
        return JsonResponse({"error": "User already exists"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def getUser(request):
    try:
        user = User.objects.get(username=request.GET.get('username'))
        print(user)
        password = request.GET.get('password')
        print('PASSWORD TYPED IN: ', password)
        print('USER.PASSWORD: ', user.password)
        if request.GET.get('password') != user.password:
            print('FAILED TO GET THE PASSWORD!')
            raise ValueError    

        cosmeticObjects = []

        print("User.cosmetics before loop: ", user.cosmetics)
        if user.cosmetics != "":
            for cosmetic in split(user.cosmetics):
                if cosmetic:
                    cosmeticObjects.append(cosmeticsMap[cosmetic])
        print("User.cosmetics after loop: ", user.cosmetics)

        taskOutput = []

        if user.tasks == "":
            print('task output is empty')
            newTasks = []

            while len(newTasks) < 4:
                num = random.randint(0,len(taskList)-1)
                if (num not in newTasks):
                    newTasks.append(num)
                    taskOutput.append(taskList[num])
            
            user.tasks = join(newTasks)
        else:
            print('task output is not empty')
            for task in split(user.tasks):
                if task:
                    taskOutput.append(taskList[int(task)])

        print('User before save', user)
        user.save()
        print('User after save', user)

        print('user.id', user.id)
        print('user.username', user.username)
        print('user.level', user.level)
        print('user.cosmetics', user.cosmetics)
        print('user.xp', user.xp)
        print('user.lvlxp', user.lvlxp)
        print('user.gold', user.gold)
        print('tasks', taskOutput)
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
    print("userTasks: ", userTasks)
    remainingTasks = []
    for i in userTasks:
        remainingTasks.append(taskList[int(i)])

    print("remainingTasks: ", remainingTasks)

    for task in taskList:
        if task['name'] == data['taskName']:
            removedTask = task
            user.xp += removedTask['xp']

    # Check if leveled up
    if user.xp >= user.lvlxp:
        user.level += 1
        user.xp -= user.lvlxp
        user.lvlxp = user.level*10
        user.gold += 5

    if not user.newbie:
        user.newbie = True
        user.gold += 5

    user.taskCount += 1

    if not user.bronzeMedal and user.taskCount >= 5:
        user.bronze = True
    
    if not user.silverMedal and user.taskCount >= 10:
        user.silver = True
    
    if not user.goldMedal and user.taskCount >= 20:
        user.gold = True

    user.save()
    
    return JsonResponse({
        "removed": removedTask,
        "tasks": remainingTasks,
        "xp": user.xp,
        "level": user.level,
        "lvlxp": user.lvlxp,
        "gold": user.gold
    })


@csrf_exempt
def buyCosmetic(request):
    # Getting sent: id, item name
    data = json.loads(request.body)
    user = User.objects.get(id=data['id'])

    userCosmetics = split(user.cosmetics)
    userCosmetics.append(data['itemName'])
    user.cosmetics = join(userCosmetics)
    user.gold -= cosmeticsMap[data['itemName']]['price']
    user.save()

    owned = []
    for name in userCosmetics:
        if name:
            owned.append(cosmeticsMap[name])

    if not user.highRoller and len(userCosmetics) >= 4:
        user.highRoller = True


    return JsonResponse({
        "inventory": owned,
        "gold": user.gold
    })

@csrf_exempt
def getAllCosmetics(request):
    user = User.objects.get(id=request.GET.get('id'))

    allCosmetics = []
    for cosKey in cosmeticsMap:
        allCosmetics.append(cosmeticsMap[cosKey])

    for name in split(user.cosmetics):
        if name:
            allCosmetics.remove(cosmeticsMap[name])

    return JsonResponse({
        'cosmetics': allCosmetics
    })



    

def join(array):
    if isinstance(array[0], int):
        return ','.join(str(num) for num in array)
    else:
        return ','.join(map(str, array))
    
    
def split(x):
    return x.split(",")

    
