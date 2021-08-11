from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import PointsForm
from ast import literal_eval as make_tuple
import math
from django.contrib import messages

# Rendering the templates from the views controller.

def index(request):
    form = PointsForm()
    if request.method == 'POST':
        user_points = request.POST['user_points']

        result = calculateClosestPoints(user_points)
        request.POST = request.POST.copy()
        for closest_pair in result:
            request.POST['closest_pair'] = closest_pair
        form = PointsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Points successfully stored. Closest pair is : ' + str(closest_pair))

    context = {'points_form': form}
    return render(request, 'app/index.html', context)

def calculateClosestPoints(user_points):
    #Shortest distance in pairs c^2 = a^2 + b^2
    tuple_points = make_tuple(user_points)
    print('userEntry:', tuple_points)
    lc =[]
    lc_close_close_pair = []

    for point in tuple_points:
        if point in lc:
            # print('context:', lc_close_close_pair)
            print('Finished!')
            break

        x1, y1 = point  
        # print('Point1:', point)
        lc.append(point)
 
        for pnt in tuple_points:

            if point != pnt:
                x2,y2 = pnt
                # print('Point2:', pnt)
                result = distance(x1,y1,x2,y2)

                points_pair = '('+ str(x1) +','+ str(y1) +')' + ',' + '(' + str(x2) + ','+ str(y2) +')'
                # print('Pair', points_pair)
                lc.append(pnt)
                context = [result,points_pair]
                lc_close_close_pair.append(context)
                
                print('distance:', result)

    lc_close_close_pair.sort()
    for item in lc_close_close_pair:
        print(item)
    print(lc_close_close_pair[0])
    return lc_close_close_pair[0]

def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
                