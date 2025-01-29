from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import os


def get_info(request):
    """
    Returns informations in JSON format
    """

    email_address = os.environ.get('EMAIL_ADDRESS', "hetty8004@gmail.com")

    github_url = "https://github.com/samuelhetty/HNG-Python-Backend"

    current_datetime = datetime.now().isoformat() + "Z"

    data = {
        "email": email_address,
        "datetime": current_datetime,
        "github_url": github_url
    }
    return JsonResponse(data)
