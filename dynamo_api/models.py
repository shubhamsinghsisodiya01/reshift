from django.db import models
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class PowerConsumption(Model):
    class Meta:
        table_name = 'power_consumption'
        # Specifies the region
        region = 'us-east-1'
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        # host = 'arn:aws:dynamodb:us-east-1:186355660035:table/power_consumption'
        # Specifies the write capacity
        write_capacity_units = 5
        # Specifies the read capacity
        read_capacity_units = 5
    date_time = UnicodeAttribute(hash_key=True)
    power = UnicodeAttribute(range_key=True)


class PowerConsumptionTest(Model):
    class Meta:
        table_name = 'power_consumption_test'
        # Specifies the region
        region = 'us-east-1'
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        # host = 'arn:aws:dynamodb:us-east-1:186355660035:table/power_consumption'
        # Specifies the write capacity
        write_capacity_units = 5
        # Specifies the read capacity
        read_capacity_units = 5
    date_time = UnicodeAttribute(hash_key=True)
    power = UnicodeAttribute(range_key=True)