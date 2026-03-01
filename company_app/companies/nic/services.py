import requests

class NICService:

    BASE_URL = "https://niconline.co.in"

    @staticmethod
    def fetch_policies(token: str):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{NICService.BASE_URL}/api/policies",
            headers=headers
        )
        return response.json()