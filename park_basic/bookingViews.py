
from rest_framework.decorators import api_view,parser_classes
from django.http import JsonResponse
from park_basic.models import booking
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, ReserverSerializer, BookingSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import Token
from rest_framework import status
from .models import reserver, User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404



@api_view(['POST'])
@csrf_exempt
@parser_classes([JSONParser])
def insert_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        time_id_data = data.get("timeId")
        slotId_data = data.get("slotId")
        current_time = timezone.now().time()
        current_date = timezone.now().date()
        provided_token = request.META.get('HTTP_AUTHORIZATION')
        if provided_token and provided_token.startswith('Bearer '):
            token_key = provided_token.split(' ')[1]
            try:

                token = Token.objects.get(key=token_key)
                user = token.user
                Reserver = reserver.objects.filter(userId=user.id).first()
                reserver_id = Reserver.id;
                booking_serializer = BookingSerializer(data={
                    "Date" : current_date,
                    "Time" : current_time,
                    "reserverId" : reserver_id,
                    "timeId" : time_id_data,
                    "slotId" : slotId_data
                })
                bookings = booking.objects.filter(Date=current_date,
                    timeId=time_id_data,
                    slotId=slotId_data).first()

                if bookings:
                    return JsonResponse({
                        "message": "Already"
                    }, status=400)

                else:
                    if booking_serializer.is_valid():
                        if booking_serializer.save():
                            return JsonResponse({
                                "message": "syvc"
                            }, status=200)
                        else:
                            return JsonResponse({
                                "message": "failed"
                            }, status=400)

                    else:
                        return JsonResponse({
                            "message": "val"
                        }, status=status.HTTP_401_UNAUTHORIZED)




            except Token.DoesNotExist:
                return JsonResponse({
                    "message": "Invalid token"
                }, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return JsonResponse({
                "message" : "Not Authorized",

            }, status=401 )
