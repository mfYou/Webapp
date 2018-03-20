from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import UserInfo, Community
from .serializers import UserSerializer, CommunitySerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import json
import jieba
from collections import OrderedDict

# Create your views here.
def hello(request):
    return HttpResponse("Hello world! ")

class UserViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

    @list_route()
    def getUser(self, request, *args, **kwargs):
        get = request.GET
        a = get.get('idnum')
        user = UserInfo.objects.filter(idnum = a)
        ser = UserSerializer(user, many=True)
        result = dict()
        result['code'] = 1
        result['data'] = dict()
        result['data'] = ser.data
        return JsonResponse(result)

    @list_route()
    def getWord(self, request, *args, **kwargs):
        get = request.GET
        a = get.get('content')
        list = jieba.cut(a)
        str = ','.join(list)
        return HttpResponse(str)