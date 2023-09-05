from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from psycopg2 import errors as pg_errors


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, (IntegrityError, pg_errors.UniqueViolation)):
        return Response(
            {"error": "Duplicate key value violates unique constraint."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if response is not None:
        return Response({"error": response.data}, status=response.status_code)

    return Response(
        {"error": "Internal Server Error: Something went wrong."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
