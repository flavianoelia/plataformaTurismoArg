from django.db import models # Importa el módulo `models` de Django, utilizado para definir modelos de datos

# Modelo que representa una ciudad.
class City(models.Model):
    # Campo que almacena el nombre de la ciudad, con una longitud máxima de 100 caracteres.
    name = models.CharField(max_length=100)
    # Campo que almacena una descripción opcional de la ciudad.
    description = models.TextField(null=True)
    # Campo que almacena una imagen opcional de la ciudad. Las imágenes se subirán a la carpeta "city_images".
    image = models.ImageField(upload_to="city_images", null=True, blank=True)
    # Campo que almacena la población de la ciudad como texto, siendo opcional.
    poblacion = models.TextField(null=True)

    # Método mágico que define cómo se representa una instancia del modelo como texto. Devuelve el nombre de la ciudad.
    def __str__(self):
        return self.name

# Modelo que representa un lugar turístico asociado a una ciudad.
class TouristPlace(models.Model):# Nueva clase
    # Relación de clave foránea con el modelo `City`. 
    # Cada lugar turístico pertenece a una ciudad específica. Si se elimina la ciudad, los lugares turísticos también se eliminarán.
    city = models.ForeignKey(City, related_name='lugares_turisticos', on_delete=models.CASCADE)
    # Campo que almacena el nombre del lugar turístico, con una longitud máxima de 100 caracteres.
    name = models.CharField(max_length=100)
    # Campo opcional que almacena una descripción del lugar turístico.
    description = models.TextField(blank=True, null=True)
    # Campo opcional que almacena una imagen del lugar turístico. Las imágenes se subirán a "tourist_place_images".
    image = models.ImageField(upload_to="tourist_place_images", null=True, blank=True)

    # Método mágico que define cómo se representa una instancia del modelo como texto. Devuelve el nombre del lugar turístico.
    def __str__(self):
        return self.name

# Modelo que representa una ruta entre dos ciudades.
class Route(models.Model):
    # Relación de clave foránea para la ciudad de inicio de la ruta.
    start_city = models.ForeignKey(
        City, related_name="route_start", on_delete=models.CASCADE
    )
    # Relación de clave foránea para la ciudad de destino de la ruta.
    end_city = models.ForeignKey(
        City, related_name="route_end", on_delete=models.CASCADE
    )
    # Campo que almacena la distancia de la ruta en kilómetros como un número flotante.
    distance = models.FloatField()

    # Sobrescribe el método `save` para agregar funcionalidad personalizada al guardar una instancia de Route.
    def save (self, *args, **kwargs): #para hacer automáticamente la ruta inversa
        # Llama al método `save` original para guardar la ruta actual.
        super().save(*args, **kwargs) #llama al método save() original para guardar la ruta

        #Verifica si la ruta inversa ya existe si no la creamos
        if not Route.objects.filter( start_city=self.end_city, end_city=self.start_city).exists():
            #Si no existe, crea la ruta inversa automáticamente con la misma distancia
            Route.objects.create(start_city=self.end_city, end_city=self.start_city, distance=self.distance)

# Método mágico que define cómo se representa una instancia del modelo como texto.
# Devuelve una representación en formato "Ciudad de inicio -> Ciudad de destino (distancia en km)".
    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"
