from django.db import models
from datetime import date

class User(models.Model):
    user_name = models.CharField(max_length=50, blank=True)
    male_or_female = models.CharField(max_length=10, blank=False)
    weight = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    age = models.IntegerField(blank=False)
    activity_level = models.IntegerField(blank=False)

    rec_bmr = models.IntegerField(blank=True, null=True)
    rec_calories = models.IntegerField(blank=True, null=True)
    rec_cal_lose = models.IntegerField(blank=True, null=True)


    def calculate_bmr(self, user_weight, user_height, user_age, m_or_f):
        #Basal Metabolic Rate
        print("WEIGHT", type(user_weight))
        weight_in_kgs = float(user_weight) / 2.2
        height_in_cent = float(user_height) * 2.54
        if m_or_f == "M":
            bmr = int((10 * weight_in_kgs) + (6.25 * height_in_cent) - (5 * user_age) + 5)
        elif m_or_f == "F":
            bmr = int((10 * weight_in_kgs) + (6.25 * height_in_cent) - (5 * user_age) - 161)
        return bmr

    def daily_caloric_needs(self, bmr, user_activity):
        """
            1 = Sedentary
            2 = Exercise 1 - 3 times a week
            3 = Exercise 4 - 5 times a week
            4 = Daily Exercise or intense exercise 3-4 times a week
            5 = Intense Exercise 6 times a week
        """
        if user_activity == 1:
            level_index = 1.2
        elif user_activity == 2:
            level_index = 1.375
        elif user_activity == 3:
            level_index = 1.46
        elif user_activity == 4:
            level_index = 1.725
        elif user_activity == 5:
            level_index = 1.9
        #Recommended caloric intake to maintain weight
        daily_cal_intake = int(bmr * level_index)
        return daily_cal_intake
    
    def lose_weight(self, calories):
        #to lose .5lbs per week:
        cal_to_lose = int(calories - int((3500 / 2) / 7))
        return cal_to_lose

    #I don't think I'll include this 
    def calculate_macros(calories):
        #calories = dailyCalIntake
        #Calculate maintenance macros 
        #based on caloric intake, this calculates caloric intake of P/C/F and grams
        cal_from_protein = int(.4 * calories)
        grams_of_protein = int(cal_from_protein / 4)
        cal_from_carbs = int(.4 * calories)
        grams_of_carbs = int(cal_from_protein / 4)
        cal_from_fat = int(.2 * calories)
        grams_of_fat = int(cal_from_fat / 9)

class FoodJournal(models.Model):
    date = models.DateField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # items = models.ForeignKey('FoodLogItem', on_delete=models.CASCADE, related_name='journal_entries', blank=True, null=True)
    #how will I store nutrition meters?

      
class FoodLogItem(models.Model):
    entry = models.ForeignKey(FoodJournal, on_delete=models.CASCADE, related_name='food_entries', blank=True, null=True)
    # date = models.DateField(auto_now=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False)
    calories = models.IntegerField(blank=False)
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
