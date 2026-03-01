from django.db import transaction
from .models import NICPolicy

class NICRepository:

    @staticmethod
    def get_all():
        return NICPolicy.objects.all().values()

    @staticmethod
    def create_single(data: dict):
        return NICPolicy.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def bulk_insert(data_list: list):
        objs = [NICPolicy(**item) for item in data_list]
        NICPolicy.objects.bulk_create(objs, ignore_conflicts=True)
        return len(objs)