from rest_framework.views import APIView
from rest_framework.response import Response

class User(APIView):
    def get(self, request):
        return Response({"hoge": "hoge"}, status=200)
