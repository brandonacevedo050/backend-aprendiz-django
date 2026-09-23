import importlib
import os
from unittest.mock import patch

from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient

from aprendiz.models import Aprendiz


class AprendizSettingsTests(SimpleTestCase):
    def test_sqlite_configuration_is_supported_for_tests(self):
        with patch.dict(os.environ, {"DB_ENGINE": "sqlite3"}, clear=False):
            import config.settings.base as base_settings

            importlib.reload(base_settings)

            self.assertEqual(
                base_settings.DATABASES["default"]["ENGINE"],
                "django.db.backends.sqlite3",
            )


class AprendizApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("aprendiz-list-create")

    def _make_payload(self, email="ana@example.com"):
        return {
            "nombre": "Ana",
            "apellido": "García",
            "cedula": "10101010",
            "tipo_id": "CC",
            "email": email,
            "telefono": "3000000000",
            "direccion": "Calle 10",
            "genero": "F",
            "ficha": "2024A",
            "jornada": "Diurna",
        }

    def test_create_and_list_aprendiz(self):
        payload = self._make_payload()

        create_response = self.client.post(self.url, payload, format="json")
        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(Aprendiz.objects.count(), 1)

        list_response = self.client.get(self.url)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["email"], payload["email"])

    def test_update_and_delete_aprendiz(self):
        created = self.client.post(self.url, self._make_payload(), format="json")
        aprendiz_id = created.data["id"]
        detail_url = reverse("aprendiz-detail", args=[aprendiz_id])

        update_payload = self._make_payload(email="ana_nueva@example.com")
        update_response = self.client.put(detail_url, update_payload, format="json")
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.data["email"], "ana_nueva@example.com")

        delete_response = self.client.delete(detail_url)
        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(Aprendiz.objects.filter(id=aprendiz_id).exists())
