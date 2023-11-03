from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
import random

class VerifyCode(APIView):
    def post(self, request):
        code = request.data.get('code')
        email = request.data.get('email')

        if not code or not email:
            return Response({'message': 'Код или email отсутствуют'}, status=status.HTTP_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'message': 'Пользователь не найден'}, status=status.HTTP_NOT_FOUND)

        
        if code == user.verification_code:
          
            user.is_active = True
            user.save()
            return Response({'message': 'Пользователь активирован'}, status=status.HTTP_OK)
        else:
            
            return Response({'message': 'Неверный код аутентификации'}, status=status.HTTP_UNAUTHORIZED)
        
class UserRegistration(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            verification_code = random.randint(1000, 9999)
            send_mail(
                'Код подтверждения',
                f'Ваш код подтверждения: {verification_code}',
                'your_email@example.com',
                [user.email],
                fail_silently=False,
            )

            return Response({'message': 'Письмо с кодом отправлено успешно'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
