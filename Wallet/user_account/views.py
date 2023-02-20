from django.shortcuts import render
from .models import UserAccount, Wallet
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import CreateUserAccountSerializer
import random, string

def random_account_number():
    return ''.join(random.choice(string.digits) for _ in range(10))

class RegisterAccount(generics.CreateAPIView):
    permission_classes=[AllowAny]

    queryset = UserAccount.objects.all()
    serializer_class = CreateUserAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            token=RefreshToken.for_user(user).access_token
            user.token = token
            user.save()
            
            #user already has a wallet account from the signals
            #generate account number for wallet
            account_number = random_account_number()
            Wallet.objects.filter(customer=user).update(account_number=account_number,
                                                        account_name = user.first_name +' '+ 
                                                        user.last_name)
            
            if user:
                return Response({'success':True, 'message':'Account created successfully', 'entity': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success':False, 'message':'Error occured...', 'entity':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class BlacklistTokenUpdateView(APIView):
    # the reason we are blacklisting is that when the user logs out we have to black list the refresh token.
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("You are logged out", status=status.HTTP_408_REQUEST_TIMEOUT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # here we are extending the serializer class by customizing the token.
    @classmethod
    def get_token(cls, user):
        #get the token of the user by overwriting the function in the class
        token = super().get_token(user)
        #Add custom claims
        token['accountNumber']=user.accountNumber
        token['is_staff']=user.is_staff
        token['is_active']=user.is_active
        return token

class Login(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class GetAccountInfo(generics.RetrieveAPIView):
    queryset = Wallet
    serializer_class = CreateUserAccountSerializer
    def get(self, request, accountNumber, password):
        accountDetails=get_object_or_404(self.queryset, accountNumber=accountNumber)
        serializer = self.serializer_class(accountDetails)
        if accountDetails:
            return Response({'success':True,'message':'Get account statement successful', 'account':serializer.data}, status=status.HTTP_200_OK)
        return Response({'success':False, 'message':serializer.errors})
