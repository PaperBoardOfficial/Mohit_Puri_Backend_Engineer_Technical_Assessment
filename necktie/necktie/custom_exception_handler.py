import traceback
from django.utils.timezone import now
from rest_framework.views import exception_handler

from django.conf import settings

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            'status_code': response.status_code,
            'error_type': type(exc).__name__,
            'error_message': str(exc),
            'timestamp': now().isoformat(),
            'request_method': context['request'].method,
            'request_path': context['request'].path,
        }

        if settings.DEBUG:
            response.data['traceback'] = traceback.format_exc()

        response.data['suggested_action'] = "Please check the request data and try again."

    return response