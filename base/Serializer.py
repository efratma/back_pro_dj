from rest_framework import serializers
from .models import  problems

class Distributive_property_Serializer(serializers.ModelSerializer):#חוק הפילוג 2 הרמות
    class Meta:
        model = problems
        fields = ('id', 'problem_str', 'solution')


class Equation_System_h_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ('id','equation1', 'equation2', 'solution_x', 'solution_y')


class Equation_System_m_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','solution_x','solution_y','equation1', 'equation2', ]


class Equation_System_e_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','solution_x','solution_y','equation1', 'equation2', ]


class Equation_h_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','equation_text', 'correct_answer']


class Equation_m_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id', 'equation', 'correct_answer_fl',] 


class Equation_e_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','correct_answer_fl','equation',]


class Pythagoras_h_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','a_fl', 'b_fl','c_fl','option' ,]

class Pythagoras_e_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id', 'a', 'b', 'c_fl']

class line_equation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','point1_x','point1_y','point2_x','point2_y','slope','y_intercept','equation',]


class Cutting_points_with_hinges_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['equation', 'x_when_y_zero', 'y_when_x_zero']



class Triangle_hm_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','area','height','base','line1_equation','line2_equation','y_intersection','x_intersection',]

class Triangle_e_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','area','height','base','line_equation','y_intersection','x_intersection',]


class Meeting_Point_2_functions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = ['id','line1_equation','line2_equation','intersection_point',]


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = problems
        fields = '__all__'

