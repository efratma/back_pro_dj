from datetime import timezone
from math import sqrt
from random import randint
from django.db import models
from django.contrib.auth.models import User
import sympy
from sympy import Eq, Rational, symbols, solve
from sympy import randprime
from sympy.abc import x
from django.db import models
from sympy import symbols, Eq, solve
import random
from django.conf import settings
import sympy as sp
from sympy import symbols, expand
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token



#נסיון לאחד הכל במודל אחד:
class CustomUser(AbstractUser):
    # Add your custom fields here

    password_reset_token_expiration = models.DateTimeField(null=True, blank=True)
    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_set", blank=True, verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        verbose_name="user permissions",
    )

class problems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    is_correct = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=32, null=True, blank=True)
    password_reset_token_expiration = models.DateTimeField(null=True, blank=True)

    # נקודת מפגש ל 2 פונציות 
    line1_equation = models.CharField(max_length=100,null=True)
    line2_equation = models.CharField(max_length=100,null=True)
    intersection_point = models.CharField(max_length=255,null=True) 
    #שטח משולש בצירים רמה קלה
    line_equation = models.CharField(max_length=255)
    # וקשה שטח משולש רמה בינונית
    area = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    base = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    y_intersection = models.DecimalField(max_digits=10, decimal_places=2,null= True)
    x_intersection = models.DecimalField(max_digits=10, decimal_places=2,null= True)
######## חיתוך עם הצירים
    x_when_y_zero = models.FloatField(null=True, blank=True)
    y_when_x_zero = models.FloatField(null=True, blank=True)
    #  בינונית וקשה מציאת קו ישר רמה קלה
    point1_x = models.IntegerField(default=0)
    point1_y = models.IntegerField(default=0)
    point2_x = models.IntegerField(default=0)
    point2_y = models.IntegerField(default=0)
    slope = models.IntegerField(default=0)
    y_intercept = models.IntegerField(default=0)
    equation = models.CharField(max_length=100, default='')
   #פיתגורס רמה קשה וקלה
    a_fl =  models.FloatField(null=True, blank=True)
    b_fl =  models.FloatField(null=True, blank=True)
    c_fl =  models.FloatField(null=True, blank=True)
    option = models.CharField(max_length=1) 
    # משוואות כיתה ז רמה קלה
    result = models.IntegerField(null=True)
    # משוואות רמה בינונית 
    correct_answer_fl = models.FloatField(null=True, blank=True)  # Ensure the field is named "correct_answer"
    #משוואות רמה קשה כיתה ז
    equation_text = models.CharField(max_length=255, default='Default Equation')
    correct_answer = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    #משוואת בשתי נעלמים רמה קלה
    #משוואות בשני נעלמים רמה בינונית
    a = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    e = models.IntegerField(default=0)
    f = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    solution_x = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    solution_y = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    #משוואות בשני נעלמים רמה קשה
    equation1 = models.CharField(max_length=255)
    equation2 = models.CharField(max_length=255)
    #חוק הפילוג המורחב רמה קלה ומוגבר 
    problem_str = models.TextField(null=True)
    solution = models.TextField(null=True)