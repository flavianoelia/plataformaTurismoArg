from django.test import TestCase
from .models import City, Route
from .utils import get_shortest_path  # Ajusta la ruta según la ubicación del código

class ShortestPathTest(TestCase):
    def setUp(self):
        # Creamos las ciudades necesarias para el test
        self.cordoba = City.objects.create(name="Córdoba")
        self.carlos_paz = City.objects.create(name="Carlos Paz")
        self.jesus_maria = City.objects.create(name="Jesús María")

        # Creamos rutas entre las ciudades con distancias definidas
        Route.objects.create(start_city=self.cordoba, end_city=self.carlos_paz, distance=35.0)
        Route.objects.create(start_city=self.cordoba, end_city=self.jesus_maria, distance=50.0)
        Route.objects.create(start_city=self.carlos_paz, end_city=self.jesus_maria, distance=40.0)

    def test_shortest_path(self):
        # Calcula el camino más corto de Córdoba a Jesús María
        path, distance = get_shortest_path(self.cordoba, self.jesus_maria)
        
        # Comprobamos si el camino más corto es el esperado
        expected_path = [self.cordoba.id, self.carlos_paz.id, self.jesus_maria.id]  # IDs del camino previsto
        expected_distance = 50.0  # Distancia prevista de Córdoba -> Carlos Paz -> Jesús María
        
        # Extraemos los IDs de las ciudades del camino retornado
        path_ids = [city.id for city in path]
        
        # Comprobaciones
        self.assertEqual(path_ids, expected_path, "El camino más corto no es el esperado.")
        self.assertEqual(distance, expected_distance, "La distancia calculada no es la esperada.")
