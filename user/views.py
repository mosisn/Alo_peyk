from .models import OTP
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import random 
import json

class OTPView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone_number = body['phone_number']
        otp = random.randint(10000,99999)
        OTP.objects.create(
            phone_number = phone_number,
            otp = otp
        )
        return Response(otp)
    
class LoginView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone = body['phone_number']
        otp = body['otp']
        try:
            saved_otp = OTP.objects.get(phone_number = phone)
            if saved_otp.otp == otp:
                saved_otp.delete()
                try:
                    current_user = User.objects.get(username = phone)
                except:
                    current_user = User.objects.create(
                        username = phone
                    )
                access_token = create_access_token(current_user.id)
                refresh_token = create_refresh_token(current_user.id)
                res = Response(access_token)
                res.set_cookie('refresh_token', refresh_token, httponly=True)
                return res
            else:
                return Response('OTP is WRONG!', status=403)
        except:
            return Response('some thing is wrong!', status=500)