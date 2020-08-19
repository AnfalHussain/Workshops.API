from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
import uuid

from .models import (
    Workshop,
    Profile,
    Registration,
    Cart)
from .serializers import (WorkshopListSerializer, UserCreateSerializer, ProfileUpdateSerializer, RegistrationSerializer
                          )


class WorkshopListView(ListAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopListSerializer


class RegistrationItems(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # generating a random reference_number
        random_reference_number = str(uuid.uuid4())[0:8]
        total = 0
        workshops = request.data['carts']

        for workshop in workshops:
            total += Workshop.objects.get(id=workshop['id']).price

        registration_order = Registration.objects.create(
            reference_number=rand_reference_number, customer=request.user, total=total, payment_status="SUCCESSFUL")

        for workshop in workshops:
            Cart.objects.create(
                workshop_id=workshop['id'],
                registration=registration_order
            )
            return Response(self.serializer_class(registration).data, status=HTTP_200_OK)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
