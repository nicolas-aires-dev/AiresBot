from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .knowledge import answer_question


@api_view(["POST"])
def chat(request):
    message = request.data.get("message", "")
    if not isinstance(message, str) or not message.strip():
        return Response(
            {"error": "Envie uma mensagem não vazia no campo 'message'."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if len(message) > 1000:
        return Response(
            {"error": "A mensagem deve ter até 1000 caracteres."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response({"answer": answer_question(message)})
