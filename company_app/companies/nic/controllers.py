from .repository import NICRepository
from .utils import download_pdf_from_url

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