from .repository import NICRepository
from .utils import download_pdf_from_url
from typing import Any
from company_app.common.request_handler import RequestHandler
import requests
from .utils import *

class NICController:

    @staticmethod
    def get_policies():
        return list(NICRepository.get_all())

    @staticmethod
    def create_policy(data: dict):
        policy = NICRepository.create_single(data)
        return {"id": policy.id}

    @staticmethod
    def bulk_insert(data_list: list):
        return NICRepository.bulk_insert(data_list)

    @staticmethod
    def download_pdf(policy_number: str):
        policy = NICRepository.get_all().filter(policy_number=policy_number).first()
        if not policy or not policy["pdf_url"]:
            return {"error": "PDF not found"}
        return download_pdf_from_url(policy["pdf_url"])

    @staticmethod
    def login(data: dict):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"status": False, "message": "Username and password are required"}
        login_url = "https://niconline.co.in/ubportal/SelectUserType.do"

        session = requests.Session()

        payload = {
            "userId": username,
            "password": password,
            "next": "LOGIN"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0"
        }

        try:
            response = session.post(
                login_url,
                data=payload,
                headers=headers,
                timeout=20
            )
            save_txt_file("response.txt", response.text)
            # Check success condition
            if "Change Password" in response.text:
                return {
                    "status": False,
                    "message": "Invalid credentials"
                }

            return {
                "status": True,
                "message": "Login request sent successfully",
                "cookies": session.cookies.get_dict()
            }

        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }