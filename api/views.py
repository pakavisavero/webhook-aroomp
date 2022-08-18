import json
# from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# @require_http_methods(["POST", "GET"])
def get_webhook(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)