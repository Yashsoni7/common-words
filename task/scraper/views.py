from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import scrape
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .serializers import common_words_serializer
from .models import common_word


@api_view(['POST'])
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data['url']
        words = common_word.objects.filter(url=url)
        if words:
            serializer = common_words_serializer(words,many=True)
            return Response(serializer.data)
        else:
            freq = scrape.find_freq_words(url)
            res = []
            for i in freq:
                val = {'word':i[0],'freq':i[1],'url':url}
                res.append(val)
                serializer = common_words_serializer(data=val)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors)
            print(res)
            return Response(res)

