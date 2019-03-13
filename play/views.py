import json

from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from play.mock_data import MOCK_RESPONSE
from .models import Play


def graph(request):
    return render(request, 'graph/graph.html')


def mock_data(request):
    mock_data_dict = json.loads(MOCK_RESPONSE)
    return JsonResponse(mock_data_dict, safe=False)


def play_count_by_month(request):
    data = Play.objects.all() \
        .extra(
        select={
            'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')
        }
    ) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)
