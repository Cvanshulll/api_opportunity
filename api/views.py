from .serializers import OpportunitySerializer
from rest_framework.generics import ListAPIView
from .models import Opportunity
# Create your views here.

class OpportunityListView(ListAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


