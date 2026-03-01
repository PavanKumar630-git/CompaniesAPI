from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .controllers import NICController
from .serializers import LoginSerializer, LoginResponseSerializer
from drf_spectacular.utils import extend_schema

@api_view(["GET"])
def list_policies(request):
    data = NICController.get_policies()
    return Response({"policies": data})


@api_view(["POST"])
def create_policy(request):
    result = NICController.create_policy(request.data)
    return Response(result, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def bulk_insert(request):
    count = NICController.bulk_insert(request.data)
    return Response({"inserted": count}, status=status.HTTP_201_CREATED)

@extend_schema(
    request=LoginSerializer,
    responses=LoginResponseSerializer
)
@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    result = NICController.login(request.data)

    if not result["status"]:
        return Response(result, status=401)

    return Response(result)