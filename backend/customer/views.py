from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView


from lead.models import Lead
from team.models import Team

from .models import Customer, Note
from .serializers import CustomerSeraializer, NoteSerializer

class CustomerPagination(PageNumberPagination):
    page_size = 2


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSeraializer
    queryset = Customer.objects.all()
    pagination_class = CustomerPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person')


    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team = team)
    

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team = team,created_by = self.request.user)



class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        customer_id = self.request.GET.get('customer_id')

        return self.queryset.filter(team=team).filter(customer_id=customer_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        customer_id = self.request.data['customer_id']

        serializer.save(team=team, created_by=self.request.user, customer_id=customer_id)


@api_view(['POST'])
def convert_lead_to_customer(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404
    
    customer = Customer.objects.create(team=team, name=lead.company, contact_person=lead.contact_person, email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)
    lead.delete()
    return Response()

@api_view(['POST'])
def delete_customer(request, customer_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    customer = team.customers.filter(pk=customer_id)
    customer.delete()

    return Response({'message': 'The customer was deleted'})