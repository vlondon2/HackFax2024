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

@csrf_exempt
def createUser(request):
    try:
        data = json.loads(request.body)

        user = User.objects.create(
            username=data['username'],
            password=data['password'],
            level=1,
            xp=0,
            lvlxp=100,
            gold=0
        )

        user.save()

        return JsonResponse({
            'id':user.id,
            'username':user.username,
            'level':user.level,
            'cosmeticPaths':[],
            'tasks': []
        })
    
    except Exception as e:
        return JsonResponse({"Message": str(e)}, status=400)
    
@csrf_exempt
def getUser(request):
    try:
        data = json.loads(request.body)

        user = User.objects.get(username=data['username'])

        if data['password'] != user.password:
            raise ValueError

        # paths = []
        # cosmetics = separate(user.cosmetics)

        # while len(cosmetics) != 0:
        #     paths.append()

        return JsonResponse({
            'id': user.id,
            'username':user.username,
            'level': user.level,
            # 'cosmeticPaths': paths,
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
    
