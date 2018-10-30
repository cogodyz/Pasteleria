from django.test import TestCase
from apps.rescate.models import perrito


class ContactoModelTest(TestCase):

    def test_user_creation(self):
        perrito( nombrePerro='prueba user',razaP = "pruebaspadre" , descripcion = "pruebasmadre").save()

        perritos = perrito.objects.all()
        self.assertEquals(perrito.nombrePerro, nombrePerro="prueba user")

  
