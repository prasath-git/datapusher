from django.db import models

class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

# from django.db import models
import uuid
class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=255, default=uuid.uuid4, editable=False)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.account_name

class Destination(models.Model):
    account = models.ForeignKey(Account, related_name="destinations", on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10, choices=[("GET", "GET"), ("POST", "POST"), ("PUT", "PUT")])
    headers = models.JSONField()

    def __str__(self):
        return f"{self.account.account_name} - {self.url}"
