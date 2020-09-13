from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, CustomRegisterSerializer,LoginS

class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.create(user=user).key
            })
        else:
            return Response ({
                "error":"Something is wrong"
            }
            )



from rest_framework.views import APIView
class LoginAPI(APIView):
    serializer_class = LoginS

    def post(self,request,*args,**kwargs):
        ser=self.serializer_class(data=self.request.data)
        if ser.is_valid(raise_exception=True):
            from django.contrib.auth import authenticate
            user = authenticate(self.request, username=ser.validated_data['username'],
                                password=ser.validated_data['password'])
            if user:
                instance, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'key':instance.key,
                    'user':user.id,
                    'is_student':user.is_student,
                    'is_teacher':user.is_teacher


                })
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
