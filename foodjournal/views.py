from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from foodjournal.models import FoodJournal, FoodLogItem, User
from foodjournal.serializers import FoodJournalSerializer, FoodLogItemSerializer, UserSerializer
from datetime import date
from datetime import datetime
from django.utils.timezone import localdate
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


wanted_date = localdate()

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

@api_view(['GET', 'POST'])
def food_journal_entry_list(request):
    """
    List all journal entries or create a new entry
    """
    if request.method == 'GET':
        entries = FoodJournal.objects.filter(date=localdate())
        serializer = FoodJournalSerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # check db if date already exists, modify existing entry
        print("HERE", wanted_date)

        serializer = FoodJournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         

@api_view(['GET', 'PUT', 'DELETE'])
def food_journal_entry_detail(request, pk):
    """
    Retrieve, update or delete a journal entry instance
    """
    try:
        entry = FoodJournal.objects.get(pk=pk)
    except FoodJournal.DoesNotExist:
        return Response({'message': 'Sorry, that item does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodJournalSerializer(entry)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print("HERE")
        serializer = FoodJournalSerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        entry.delete()
        return Response({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def food_log_item_list(request):
    """
    List all journal entries or create a new entry
    """

    if request.method == 'GET':
        foods = FoodLogItem.objects.all()
        serializer = FoodLogItemSerializer(foods, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoodLogItemSerializer(data=request.data)
        print("HERE!!", serializer)
        if serializer.is_valid():
            serializer.save()

            journal_entry = {
                "date": wanted_date,
                "food_entries": [request.data]
            }
            
            entry_serializer = FoodJournalSerializer(data=journal_entry)
            print("AKEJGAJG", entry_serializer)

            if entry_serializer.is_valid():
                entry_serializer.save()
                return Response(entry_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def food_log_item_detail(request, pk):
    """
    Retrieve, update or delete a journal entry instance
    """
    try:
        food = FoodLogItem.objects.get(pk=pk)
    except FoodLogItem.DoesNotExist:
        return Response({'message': 'Sorry, that item does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodLogItemSerializer(food)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FoodLogItemSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        food.delete()
        return Response({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users or create a new user
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print("USERREQ", request.data)
        if serializer.is_valid():
            serializer.save()

            user_data = serializer.data
            #grabbing data
            m_or_f = user_data['male_or_female']
            user_weight = user_data['weight']
            user_height = user_data['height']
            user_age = user_data['age']
            user_act_level = user_data['activity_level']

            #calling model function
            bmr = User().calculate_bmr(m_or_f = m_or_f, user_weight = user_weight, user_height = user_height, user_age = user_age)
            rec_daily_cal = User().daily_caloric_needs(bmr, user_act_level)
            to_lose_weight = User().lose_weight(rec_daily_cal)

            response = {
                "user_name": request.data['user_name'],
                "male_or_female": request.data['male_or_female'],
                'weight': request.data['weight'],
                'height': request.data['height'],
                'age': request.data['age'],
                'activity_level': request.data['activity_level'],
                "rec_bmr": bmr,
                "rec_calories": rec_daily_cal,
                "rec_cal_lose": to_lose_weight
            }
            response_serializer = UserSerializer(data=response)
            if response_serializer.is_valid():
                response_serializer.save()
            return Response({"rec_bmr" : bmr, "rec_calories" : rec_daily_cal, "rec_cal_lose" : to_lose_weight}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a user instance
    """
    try:
        user = User.objects.get(pk=pk)
    except FoodLogItem.DoesNotExist:
        return Response({'message': 'Sorry, that item does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



