from sanic.views import HTTPMethodView
from sanic.response import text

class Jobs(HTTPMethodView):
    async def get(self, request):
        return text("Get Jobs")
