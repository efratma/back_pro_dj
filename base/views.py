import random
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from sympy import expand, symbols,Eq, linsolve
from .Serializer import Distributive_property_Serializer, Equation_System_e_Serializer, Equation_System_h_Serializer, Equation_System_m_Serializer, Equation_e_Serializer, Equation_h_Serializer, Equation_m_Serializer, Pythagoras_h_Serializer, SolvedExerciseSerializer, Triangle_hm_Serializer, line_equation_Serializer,Meeting_Point_2_functions_Serializer,Cutting_points_with_hinges_Serializer,Triangle_e_Serializer,Pythagoras_e_Serializer,ProblemsSerializer
from .models import SolvedExercise, problems
from rest_framework.views import APIView
import math
import sympy as sp
from random import randint
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics





# register


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("new user born")

###########חוק הפילוג המורחב מוגבר
x, y = symbols('x y')

def generate_problem():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    e = random.randint(-10, 10)
    problem_type = random.randint(1, 5)

    if problem_type == 1:
        problem_str = f"{a}({b}{x}+{c})({x}+{d})"
        solution = expand(a*(b*x+c)*(x+d))
    elif problem_type == 2:
        problem_str = f"{a}({x}+{c})({x}+{d})"
        solution = expand(a*(x+c)*(x+d))
    elif problem_type == 3:
        problem_str = f"{a}({b}{x}+{c})({y}+{d})"
        solution = expand(a*(b*x+c)*(y+d))
    elif problem_type == 4:
        problem_str = f"{a}({b}{y}+{c})({y}+{d})"
        solution = expand(a*(b*y+c)*(y+d))
    else:
        problem_str = f"{a}({b}{x}+{c})({e}{y}+{d})"
        solution = expand(a*(b*x+c)*(e*y+d))
    
    return problem_str, solution

def format_solution(expression):
    # Get the string representation of the expression and remove the * sign
    return str(expression).replace('*', '')

@api_view(['GET'])
def Law_of_Extended_Division_h(request):
    if request.method == 'GET':
        problem_str, solution = generate_problem()
        problem_instance = problems(problem_str=problem_str, solution=format_solution(solution))
        problem_instance.save()
        serializer = Distributive_property_Serializer(problem_instance)
        return Response(serializer.data)
########## חוק הפילוג המורחב רמה קלה



def generate_problem_1():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    problem_type = random.randint(1, 3)

    if problem_type == 1:
        problem_str = f"({x}+{a})({a}+{b})"
        solution = expand((x+a)*(a+b))
    elif problem_type == 2:
        problem_str = f"({a}{x}+{b})({x}+{c})"
        solution = expand((a*x+b)*(x+c))
    else:
        problem_str = f"({a}{x}+{b})({c}{y}+{d})"
        solution = expand((a*x+b)*(c*y+d))
    
    return problem_str, solution

def format_solution(expression):
    # Get the string representation of the expression and remove the * sign
    return str(expression).replace('*', '')

class Law_of_Extended_Division_e(APIView):
    def get(self, request, *args, **kwargs):
        problem, solution = generate_problem_1()
        solution_str = format_solution(solution)
        problem_obj = problems.objects.create(problem_str=str(problem), solution=solution_str)
        serializer = Distributive_property_Serializer(problem_obj)
        return Response(serializer.data)
######################מערכת 2 משוואת רמה קשה
class Equation_System_h(APIView):
    def get(self, request, *args, **kwargs):
        # Define variables
        x, y = symbols('x y')

        # Generate coefficients for three types of equations
        a, b, d, e, f, h, i, k, l = [random.randint(-5, 5) for _ in range(9)]
        c, g, j = [random.randint(1, 5) for _ in range(3)] # Ensure non-zero for divisors

        # Define equations as strings
        eq1_str = f"({a}x{'+' if b >= 0 else ''}{b})/{c}{'+' if d >= 0 else '-'}{abs(d)} = ({e}y{'+' if f >= 0 else ''}{f})/{g}"
        eq2_str = f"({a}x{'+' if b >= 0 else ''}{b})/{c} = ({e}y{'+' if f >= 0 else ''}{f})/{g}"
        eq3_str = f"({h}x{'+' if i >= 0 else ''}{i})/{j}{'+' if k >= 0 else '-'}{abs(k)}y{'+' if l >= 0 else ''}{l}/{g} = {d}"

        # Convert to sympy expressions
        eq1 = Eq((a * x + b) / c + d, (e * y + f) / g)
        eq2 = Eq((a * x + b) / c, (e * y + f) / g)
        eq3 = Eq((h * x + i) / j + k * y + l / g, d)

        # Randomly select two equations from the list
        eqs_str = [eq1_str, eq2_str, eq3_str]
        eqs = [eq1, eq2, eq3]
        selected_indices = random.sample(range(3), 2)

        # Solve the system of equations
        solution = linsolve([eqs[i] for i in selected_indices], (x, y))


        # Check for no solution or infinite solutions
        if len(solution) == 0:
            response_data = {
                "error": "The system of equations has no solution.",
                "equation1": eqs_str[selected_indices[0]],
                "equation2": eqs_str[selected_indices[1]],
            }
            return Response(response_data)
        elif len(solution.free_symbols) > 0:
            response_data = {
                "error": "The system of equations has infinite solutions.",
                "equation1": eqs_str[selected_indices[0]],
                "equation2": eqs_str[selected_indices[1]],
            }
            return Response(response_data)
        else:
            solution_list = list(solution)
            solution_x = round(float(solution_list[0][0]), 2)
            solution_y = round(float(solution_list[0][1]), 2)

            equation = problems.objects.create(
            solution_x=solution_x, solution_y=solution_y,
            equation1=eqs_str[selected_indices[0]], equation2=eqs_str[selected_indices[1]]
          )
        serializer = Equation_System_h_Serializer(equation)
        return Response(serializer.data)
##########מערכת משוואת בינוי
class Equation_System_m(APIView):
    def get(self, request):
        x, y = symbols('x y')
        a, b, c, d, e, f, g, h, i = [randint(1, 10) - 5 for _ in range(9)]

        equation1 = Eq(a * (x + b) + c * (y + d), e)
        equation2 = Eq(f * (g * x + h) + i * (y + a), b)
        solution = linsolve((equation1, equation2), (x, y))

        equation1_str = f"{a}(x{'+' if b >= 0 else ''}{b}) + {c}(y{'+' if d >= 0 else ''}{d}) = {e}"
        equation2_str = f"{f}({g}x{'+' if h >= 0 else ''}{h}) + {i}(y{'+' if a >= 0 else ''}{a}) = {b}"

        if len(solution) == 0:
            return Response({"error": "The system of equations has no solution."})
        elif len(solution.free_symbols) > 0:
            return Response({"error": "The system of equations has infinite solutions."})
        else:
            solution_list = list(solution)
            solution_x = round(float(solution_list[0][0]), 2)
            solution_y = round(float(solution_list[0][1]), 2)

            equation = problems.objects.create(
                solution_x=solution_x, solution_y=solution_y,
                equation1=equation1_str, equation2=equation2_str
            )

            serializer = Equation_System_m_Serializer(equation)

            response_data = serializer.data
            return Response(response_data)
    ################################## מערכת משוואת קל
@api_view(['GET'])
def Equation_System_e(request):
    x, y = sp.symbols('x y')
    a, b, e = [random.randint(1, 10)-5 for _ in range(3)]
    c, d, f = [random.randint(1, 10)-5 for _ in range(3)]
    
    eq1 = sp.Eq(a*x + b*y, e)
    eq2 = sp.Eq(c*x + d*y, f)
    
    solution = sp.linsolve((eq1, eq2), (x, y))
    
    # Extract the solution
    x_sol, y_sol = list(solution)[0]

    # Check if they are numbers and convert, else store as string
    if x_sol.is_number:
        solution_x = float(x_sol)
    else:
        solution_x = str(x_sol)

    if y_sol.is_number:
        solution_y = float(y_sol)
    else:
        solution_y = str(y_sol)

    equation1_str = f"{a}x + {b}y = {e}"  # Equation string
    equation2_str = f"{c}x + {d}y = {f}"  # Equation string

    equation_instance = problems(
        # Assuming you might have parameters a to f for the problems model. If not, comment/remove this line.
        # a=a, b=b, c=c, d=d, e=e, f=f,
        solution_x=solution_x,
        solution_y=solution_y,
        equation1=equation1_str,  # Store in database
        equation2=equation2_str   # Store in database
    )
    
    equation_instance.save()
    serializer = Equation_System_e_Serializer(equation_instance)
    return Response(serializer.data)






####################משוואה ז רמה קשה
def generate_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    d = random.randint(1,10)
    e = random.randint(1,10)
    f = random.randint(1,10)

    g = random.randint(-10, 10)

    # Solving for x in the equation: a*x + b*(x+c) - d*(e*x + f) - g = 0
    coefficient_x = a + b - d * e
    constant_term = b * c - d * f - g

    # Making sure the coefficient for x is not zero
    while coefficient_x == 0:
        a = random.randint(1,10)
        coefficient_x = a + b - d * e

    x = round(-constant_term / coefficient_x, 2)
    equation_text = f"{a}x + {b}(x + {c}) = {d}({e}x + {f}) + {g}"
    return equation_text, x

@api_view(['GET'])
def Equation_h(request):
    equation_text, correct_answer = generate_equation()
    equation = problems.objects.create(equation_text=equation_text, correct_answer=correct_answer)
    serializer = Equation_h_Serializer(equation)
    return Response(serializer.data)

######################### משוואה ז בינוני
def generate_equation_1():
    a = random.randint(1,10)
    c = random.randint(1,10)
    while a == c:
        c = random.randint(1,10)
    b = random.randint(1,10)
    d = random.randint(1,10)
    x = (d - b) / (a - c)
    equation = f"{a}x + {b} = {c}x + {d}"
    return equation, x

@api_view(['GET'])
def Equation_m(request):
    equation_str, correct_answer = generate_equation_1()
    equation = problems(equation=equation_str, correct_answer_fl=correct_answer)
    equation.save()
    serializer =Equation_m_Serializer(equation)
    return Response(serializer.data)

################## משוואה כיתה ז קל
def generate_equation_2():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    result = a * random.randint(1, 10) + b
    x = (result - b) / a
    equation = f"{a}x + {b} = {result}"
    return a, b, result, x, equation

class Equation_e(APIView):
    def get(self, request):
        a, b, result, x, equation_str = generate_equation_2()
        equation = problems.objects.create( correct_answer_fl=x, equation=equation_str)
        serializer = Equation_e_Serializer(equation)
        return Response(serializer.data)
########################פיתגורס
def generate_question():
    option = random.randint(0, 2)  
    if option == 0:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = round((a**2 + b**2)**0.5, 2)
        return a, b, c, "c"
    elif option == 1:
        a = random.randint(1, 20)
        c = random.randint(a + 1, 30)
        b = round((c**2 - a**2)**0.5, 2)
        return a, b, c, "b"
    else:
        b = random.randint(1, 20)
        c = random.randint(b + 1, 30)
        a = round((c**2 - b**2)**0.5, 2)
        return a, b, c, "a"

@api_view(['GET'])
def Pythagoras_eh(request):
    a, b, c, option = generate_question()
    question = problems.objects.create(a_fl=a, b_fl=b, c_fl=c, option=option)
    serializer = Pythagoras_h_Serializer(question)
    return Response(serializer.data, status=status.HTTP_200_OK)

######## פיתגורס קל
def generate_question1():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = round((a**2 + b**2)**0.5, 2)
    return a, b, c

class Pythagoras_e(APIView):
    def get(self, request):
        a, b, c = generate_question1()
        question = problems.objects.create(a=a, b=b, c_fl=c)  # Store c in the database
        serializer = Pythagoras_e_Serializer(question)
        return Response(serializer.data)


################### מציאת קו ישר כל הרמות
class line_equation(APIView):
    def get(self, request):
        x1 = random.randint(-10, 10)
        y1 = random.randint(-10, 10)
        x2 = random.randint(-10, 10)
        y2 = random.randint(-10, 10)

        if x2 != x1:
            slope = (y2 - y1) // (x2 - x1)
            y_intercept = y1 - slope * x1

            if slope == 0:
                equation = f"y={y_intercept}"
            elif y_intercept == 0:
                equation = f"y={slope}x"
            else:
                equation = f"y={slope}x+{y_intercept}"
        else:
            slope = 0 # Assign a value that makes sense for your application
            y_intercept = None
            equation = f"x={x1}"

        line = problems(
            point1_x=x1,
            point1_y=y1,
            point2_x=x2,
            point2_y=y2,
            slope=slope,
            y_intercept=y_intercept,
            equation=equation
        )

        line.save()

        # Use serializer to serialize the line object or manually create a response dictionary
        serializer = line_equation_Serializer(line)
        return Response(serializer.data)


################### חיתוך של 2 ישירם
class Meeting_Point_2_functions(APIView):
    def get(self, request):
        x, y = random.randint(-10, 10), random.randint(-10, 10)
        m1, m2 = random.randint(-5, 5), random.randint(-5, 5)
        while m1 == m2:
            m2 = random.randint(-5, 5)
        c1 = y - m1 * x
        c2 = y - m2 * x

        line1_equation = f"y = {m1}x + {c1}"
        line2_equation = f"y = {m2}x + {c2}"
        intersection_point = f"({x}, {y})"

        line = problems(
            line1_equation=line1_equation,
            line2_equation=line2_equation,
            intersection_point=intersection_point
        )

        serializer = Meeting_Point_2_functions_Serializer(line)
        line.save()

        return Response(serializer.data)
##################### חיתוך עם הצירים
def generate_linear_equation():
    m = random.randint(-10, 10)  # random slope
    c = random.randint(-10, 10)  # random y-intercept
    return f"y = {m}x + {c}", m, c

def solve_linear_equation(m,c):
    y_when_x_is_zero = round(c,2)  # y-intercept
    if m != 0:
        x_when_y_is_zero = round(-c / m, 2)
    else:
        x_when_y_is_zero = None
    return y_when_x_is_zero, x_when_y_is_zero

class Cutting_points_with_hinges(APIView):

    def get(self, request, *args, **kwargs):
        equation_string, m, c = generate_linear_equation()
        correct_y, correct_x = solve_linear_equation(m, c)

        equation = problems.objects.create(equation=equation_string, y_when_x_zero=correct_y, x_when_y_zero=correct_x)
        serializer = Cutting_points_with_hinges_Serializer(equation)

        return Response(serializer.data)
#############################שטח משולש בינוני וקשה

def calculate_area(base, height):
    return round(1/2 * abs(base) * abs(height), 2)

def generate_line():
    slope = random.randint(-10, 10)
    y_intercept = random.randint(-10, 10)
    return slope, y_intercept

def find_intersection(line1, line2):
    slope1, y_intercept1 = line1
    slope2, y_intercept2 = line2
    x_intersection = round((y_intercept2 - y_intercept1) / (slope1 - slope2), 2)
    y_intersection = round(slope1 * x_intersection + y_intercept1, 2)
    return x_intersection, y_intersection

class Triangle_hm(APIView):
    def get(self, request):
        line1 = generate_line()
        line2 = generate_line()

        x_intersection, y_intersection = find_intersection(line1, line2)

        base = round(abs(x_intersection), 2)
        height = round(abs(y_intersection), 2)

        area = calculate_area(base, height)

        line1_equation = f"y = {line1[0]}x +{line1[1]}"
        line2_equation = f"y = {line2[0]}x +{line2[1]}"

        triangle = problems(
            area=area,
            height=height,
            base=base,
            line1_equation=line1_equation,
            line2_equation=line2_equation,
            y_intersection=y_intersection,
            x_intersection=x_intersection
        )
        triangle.save()

        serializer = Triangle_hm_Serializer(triangle)

        return Response(serializer.data)
################ שטח משולש קל
def calculate_area_1(x, y):
    return abs(x) * abs(y) / 2  # Use float division

def generate_line_1():
    slope = random.randint(-10, 10)
    y_intercept = random.randint(-10, 10)
    while slope == 0 or y_intercept == 0 or slope % 2 != 0 or y_intercept % 2 != 0:
        slope = random.randint(-10, 10)
        y_intercept = random.randint(-10, 10)

    x_intercept = -y_intercept / slope  # Use float division
    return slope, y_intercept, x_intercept

def format_number(value):
    value_str = str(value)
    if '.' in value_str:
        value_str = value_str.rstrip('0').rstrip('.')
    return value_str

def ensure_positive(value):
    return abs(value)



@api_view(['GET'])
def Triangle_e(request):
    slope, y_intercept, x_intercept = generate_line_1()
    base = ensure_positive(x_intercept)  # Ensure the base is positive
    height = ensure_positive(y_intercept)  # Ensure the height is positive
    area = calculate_area_1(base, height)

    line_equation = f"y = {slope}x + {y_intercept if y_intercept >= 0 else '- ' + str(abs(y_intercept))}"
    line = problems.objects.create(
        line_equation=line_equation,
        x_intersection=x_intercept,
        y_intersection=y_intercept,
        height=height,
        base=base,
        area=area
    )

    serializer = Triangle_e_Serializer(line)
    response_data = serializer.data

    # Format the values
    for key in ['y_intersection', 'x_intersection', 'area', 'height', 'base']:
        response_data[key] = format_number(response_data[key])

    return Response(response_data)
#################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_solved_problems(request):
    user = request.user
    solved_problems = problems.objects.filter(solved_by=user)
    serializer = ProblemsSerializer(solved_problems, many=True)
    return Response(serializer.data)



#########################333
def problem_solver(request, problem_name):
    functions = {
        'test': Law_of_Extended_Division_h,
        'test_1': Law_of_Extended_Division_e.as_view(), # Here, using as_view() for the class-based view
        'test_2': Equation_System_h.as_view(), # Here, using as_view() for the class-based view
        'test_3': Equation_System_m.as_view(),
        'test_4': Equation_System_e,
        'test_5': Equation_h,
        'test_6': Equation_m,
        'test_7': Equation_e.as_view(),
        'test_8': Pythagoras_eh,
        'test_9': line_equation.as_view(),
        'test_10':Meeting_Point_2_functions.as_view(),
        'test_11':Cutting_points_with_hinges.as_view(),
        'test_12':Triangle_hm.as_view(),
        'test_13':Triangle_e,
        'test_14':Pythagoras_e.as_view()

    




    }

    view_func = functions.get(problem_name)

    if view_func:
        return view_func(request)
    else:
        return HttpResponse('Problem not found', status=404)
    
class RetrieveSolvedExercisesView(generics.ListAPIView):
    serializer_class = SolvedExerciseSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            # If the user is not authenticated, return an empty queryset
            return SolvedExercise.objects.none()
        else:
            return SolvedExercise.objects.filter(user=user)
