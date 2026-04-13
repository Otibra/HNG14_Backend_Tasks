from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import ClassifyName


def error_response(message, http_status):
    return Response(
        {"status": "error", "message": message},
        status=http_status
    )


@api_view(["GET"])
def gender_view(request):
    name = request.query_params.get("name")

    # ---------------- validation ----------------
    if not name:
        return error_response(
            "Missing or empty name parameter",
            status.HTTP_400_BAD_REQUEST
        )

    name = name.strip()

    try:
        # ---------------- external API ----------------
        data = requests.get(
            "https://api.genderize.io",
            params={"name": name},
            timeout=5
        ).json()

        gender = data.get("gender")
        probability = float(data.get("probability") or 0)
        count = int(data.get("count") or 0)

        # ---------------- edge case ----------------
        if gender is None or count == 0:
            return error_response(
                "No prediction available for the provided name",
                status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        is_confident = probability >= 0.7 and count >= 100

        # ---------------- DB write ----------------
        obj = ClassifyName.objects.create(
            name=name,
            gender=gender,
            probability=probability,
            sample_size=count,
            is_confident=is_confident
        )

        # ---------------- response ----------------
        return Response({
            "status": "success",
            "data": {
                "name": obj.name,
                "gender": obj.gender,
                "probability": obj.probability,
                "sample_size": obj.sample_size,
                "is_confident": obj.is_confident,
                "processed_at": obj.processed_at.isoformat() + "Z"
            }
        })

    except requests.RequestException:
        return error_response(
            "Upstream or server failure",
            status.HTTP_502_BAD_GATEWAY
        )

    except Exception:
        return error_response(
            "Internal server error",
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    