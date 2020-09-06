from django.test import TestCase
from api.models import (
    Workshop,
    Profile,
    Registration,
    Cart)
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        # creating a user object to assign it to the instructor user field when testing creating an instructor
        self.user1 = User.objects.create(
            username='someone1@test.com',
            password='abc12312q'
        )

    def test_create_workshop(self):
        Workshop.objects.create(
            name='test',
            description='test test',
            image='https://i.pinimg.com/originals/7f/54/1d/7f541d48692e19c7a492d7243b72302f.jpg',
            price='200',
        )

    def test_create_profile(self):
        Profile.objects.update(
            user_id=1,
            first_name="user",
            middle_name="test",
            last_name="family",
            gender="male",
            nationality="something",
            mobile_number="+96599913245",
            secondary_contact_number="+96599913241",
            civil_id_number="123456789123",
            governorate="Ahmadi",
            area="somewhere",
            education_level="College University Graduate",
            major="thing",
            age="22",
        )
