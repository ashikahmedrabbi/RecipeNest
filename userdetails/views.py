
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt 
from django.conf import settings
import datetime
from rest_framework import status

class RegisterView(APIView):
    def post(self,request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token=jwt.encode(payload,'secret',algorithm='HS256')

        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data=({'jwt':token})

        return response
    
class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user=User.objects.filter(id=payload['id']).first()
        serializer=userSerializer(user)
        return Response(serializer.data)
class LogoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'logout success'
        }
        return response

