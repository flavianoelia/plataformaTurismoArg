from django.test import TestCase

# Create your tests here.
from .models import City, Route
from .utils import get_shortest_path  # Ajusta el import según mi estructura de proyecto

class DijkstraAlgorithmTest(TestCase):
    def setUp(self):
        # Crea las ciudades
        self.cba = City.objects.create(name="CBA")  # Córdoba
        self.rp = City.objects.create(name="RP")    # Río Primero
        self.rs = City.objects.create(name="RS")    # Río Segundo
        self.co = City.objects.create(name="CO")    # Cosquín
        self.jm = City.objects.create(name="JM")    # Jesús María
        self.ct = City.objects.create(name="CT")    # Carlos Paz
        self.cc = City.objects.create(name="CC")    # Colonia Caroya
        self.vgb = City.objects.create(name="VGB")  # Villa General Belgrano
        self.cp = City.objects.create(name="CP")    # Carlos Paz

        # Crea las rutas con las distancias dadas
        Route.objects.create(start_city=self.cba, end_city=self.rp, distance=68.0)
        Route.objects.create(start_city=self.cba, end_city=self.rs, distance=46.6)
        Route.objects.create(start_city=self.cba, end_city=self.co, distance=55.6)
        Route.objects.create(start_city=self.cba, end_city=self.jm, distance=56.5)
        Route.objects.create(start_city=self.cba, end_city=self.ct, distance=36.5)
        Route.objects.create(start_city=self.cba, end_city=self.cc, distance=54.5)
        Route.objects.create(start_city=self.cba, end_city=self.vgb, distance=85.8)
        Route.objects.create(start_city=self.cba, end_city=self.cp, distance=40.9)

        # Agrega rutas directas adicionales entre otras ciudades
        Route.objects.create(start_city=self.jm, end_city=self.cc, distance=6.0)
        Route.objects.create(start_city=self.vgb, end_city=self.cp, distance=65.0)
        Route.objects.create(start_city=self.co, end_city=self.cp, distance=23.0)
        Route.objects.create(start_city=self.rs, end_city=self.rp, distance=30.0)

    def test_direct_route(self):
        """Prueba una ruta directa donde no se necesita pasar por Córdoba."""
        path, distance = get_shortest_path(self.jm, self.cc)
        expected_path = [self.jm, self.cc]
        expected_distance = 6.0

        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)

    def test_indirect_route_via_cordoba(self):
        """Prueba una ruta donde el camino más corto pasa por Córdoba."""
        path, distance = get_shortest_path(self.jm, self.cp)
        expected_path = [self.jm, self.cba, self.cp]
        expected_distance = 97.4  # 56.5 (JM a CBA) + 40.9 (CBA a CP)

        self.assertEqual(path, expected_path)
        self.assertAlmostEqual(distance, expected_distance, places=1)

    def test_shortest_path_avoiding_cordoba(self):
        """Prueba que el algoritmo elija la ruta más corta sin pasar por Córdoba si hay una ruta directa."""
        path, distance = get_shortest_path(self.rs, self.rp)
        expected_path = [self.rs, self.rp]
        expected_distance = 30.0

        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)

    def test_path_with_multiple_stops(self):
        """Prueba una ruta más compleja que pasa por múltiples ciudades."""
        path, distance = get_shortest_path(self.jm, self.vgb)
        # Ruta esperada: JM -> CBA -> VGB
        expected_path = [self.jm, self.cba, self.vgb]
        expected_distance = 142.3  # 56.5 (JM a CBA) + 85.8 (CBA a VGB)

        self.assertEqual(path, expected_path)
        self.assertAlmostEqual(distance, expected_distance, places=1)

