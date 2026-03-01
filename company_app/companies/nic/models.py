from django.db import models

class NICPolicy(models.Model):
    policy_number = models.CharField(max_length=255, unique=True)
    insured_name = models.CharField(max_length=255)
    premium_amount = models.DecimalField(max_digits=15, decimal_places=2)
    pdf_url = models.TextField(null=True)
    pdf_local_path = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nic_policy"