import json
from typing import Dict, Any


class RequestHandler:

    @staticmethod
    def get_get_data(request) -> Dict[str, Any]:
        try:
            data = {}

            for key in request.GET:
                values = request.GET.getlist(key)
                data[key] = values[0] if len(values) == 1 else values

            return data

        except Exception:
            return {}

    @staticmethod
    def get_post_data(request) -> Dict[str, Any]:
        try:
            content_type = request.content_type or ""

            # JSON Request
            if "application/json" in content_type:
                if not request.body:
                    return {}

                return json.loads(request.body)

            # Form-data or x-www-form-urlencoded
            if request.POST:
                data = {}

                for key in request.POST:
                    values = request.POST.getlist(key)
                    data[key] = values[0] if len(values) == 1 else values

                return data

            return {}

        except json.JSONDecodeError:
            return {}

        except Exception:
            return {}