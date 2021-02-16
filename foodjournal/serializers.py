from rest_framework import serializers, fields
from foodjournal.models import FoodJournal, FoodLogItem, User

#Serializers define the API representation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'male_or_female', 'weight', 'height', 'age', 'activity_level', 'rec_bmr', 'rec_calories', 'rec_cal_lose']
        # depth = 1

class FoodLogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLogItem
        fields = ['id', 'name', 'calories', 'fat', 'carbs', 'protein', 'entry']


class FoodJournalSerializer(serializers.ModelSerializer):
    food_entries = FoodLogItemSerializer(many=True)

    class Meta:
        model = FoodJournal
        fields = ['id', 'date', 'user', 'food_entries']

    def create(self, validated_data):
        foods_data = validated_data.pop('food_entries')
        journal = FoodJournal.objects.create(**validated_data)
        for food in foods_data:
            FoodLogItem.objects.create(entry=journal, **food)
        return journal 
    
    def update(self, instance, validated_data):
        foods_data = validated_data.pop('food_entries')
        foods = (instance.journal_items).all()
        foods = list(foods)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        for food in foods_data:
            food = foods.pop(0)
            food.date = food.get('date', food.date)
            food.name = food.get('name', food.name)
            food.calories = food.get('calories', food.calories)
            food.fat = food.get('fat', food.fat)
            food.carbs = food.get('carbs', food.carbs)
            food.protein = food.get('protein', food.protein)
            food.save()
        return instance

