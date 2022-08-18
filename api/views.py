import json
# from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_good_receive(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    
@csrf_exempt
def get_delivery_order(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    
@csrf_exempt
def get_stock_transfer(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    
@csrf_exempt
def get_receiving(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)