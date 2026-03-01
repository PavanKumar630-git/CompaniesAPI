import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .controllers import NICController

@csrf_exempt
def list_policies(request):
    return JsonResponse({"policies": NICController.get_policies()})

@csrf_exempt
def create_policy(request):
    data = json.loads(request.body)
    return JsonResponse(NICController.create_policy(data))

@csrf_exempt
def bulk_insert(request):
    data = json.loads(request.body)
    count = NICController.bulk_insert(data)
    return JsonResponse({"inserted": count})