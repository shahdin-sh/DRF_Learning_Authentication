from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class TokenCreate(ObtainAuthToken):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # user is autheticated in serializer validate method
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(f'token: {token.key}', status=status.HTTP_200_OK)


class TokenDestroy(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def post(self, request):
        username = request.user.username
        request.user.auth_token.delete()
        return Response(f'successfully logged out as {username}.', status=status.HTTP_200_OK)

    