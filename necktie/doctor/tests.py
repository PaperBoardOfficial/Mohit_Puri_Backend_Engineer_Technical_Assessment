from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Doctor, ConsultationDetail
from clinic.models import Clinic


class DoctorListCreateViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        downtown_clinic = Clinic.objects.create(district="Downtown")
        uptown_clinic = Clinic.objects.create(district="Uptown")
        consultation_detail_smith = ConsultationDetail.objects.create(
            consultation_fee=100
        )
        consultation_detail_jones = ConsultationDetail.objects.create(
            consultation_fee=150
        )
        Doctor.objects.create(
            name="Dr. Smith",
            speciality="Cardiology",
            clinic=downtown_clinic,
            consultation_detail=consultation_detail_smith,
            language="English",
        )
        Doctor.objects.create(
            name="Dr. Jones",
            speciality="Dermatology",
            clinic=uptown_clinic,
            consultation_detail=consultation_detail_jones,
            language="Spanish",
        )

    def test_list_doctors(self):
        url = reverse("doctor-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_doctors_by_speciality(self):
        url = reverse("doctor-list-create")
        response = self.client.get(url, {"speciality": "Cardiology"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["speciality"], "Cardiology")

    def test_filter_doctors_by_price_range(self):
        url = reverse("doctor-list-create")
        response = self.client.get(url, {"price_min": 100, "price_max": 120})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.data:
            self.assertTrue(
                100
                <= float(response.data[0]["consultation_detail"]["consultation_fee"])
                <= 120
            )
        else:
            self.fail("No doctors found within the specified price range")

    def test_filter_doctors_by_language(self):
        url = reverse("doctor-list-create")
        response = self.client.get(url, {"language": "English"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(doc["language"] == "English" for doc in response.data))

    def test_create_doctor(self):
        url = reverse("doctor-list-create")
        data = {
            "name": "Dr. New",
            "speciality": "General",
            "clinic": {
                "district": "Midtown",
                "name": "Clinic Name",
                "address": "123 Main St",
            },
            "consultation_detail": {"consultation_fee": 200},
            "language": "English",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 3)

    def test_filter_doctors_by_clinic_district(self):
        url = reverse("doctor-list-create")
        response = self.client.get(url, {"district": "Downtown"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            all(
                clinic["district"] == "Downtown"
                for doc in response.data
                for clinic in [doc["clinic"]]
            )
        )
