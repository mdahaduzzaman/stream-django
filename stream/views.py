from django.http import StreamingHttpResponse
import time
import json
from rest_framework.decorators import api_view

def generate_data():
    for i in range(50):
        data = json.dumps({"chunk": i})
        yield f"{data}\n"
        time.sleep(0.1)  # Simulate a delay

@api_view(['GET'])
def stream_data(request):
    response = StreamingHttpResponse(generate_data(), content_type='application/json')
    response['Cache-Control'] = 'no-cache'
    return response

from django.shortcuts import render
def home(request):
    return render(request, "stream.html")