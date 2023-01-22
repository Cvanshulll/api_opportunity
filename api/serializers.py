from rest_framework import serializers
from .models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('opportunity_id', 'name', 'role', 'batch', 'job_id', 'job_link', 'location', 'end_date', 'description', 'stipend', 'added_date', 'active')