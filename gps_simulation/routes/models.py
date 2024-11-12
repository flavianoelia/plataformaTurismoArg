from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="city_images", null=True, blank=True)
    poblacion = models.TextField(null=True)

    
class TouristPlace(models.Model):# Nueva clase
    city = models.ForeignKey(City, related_name='lugares_turisticos', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="tourist_place_images", null=True, blank=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    start_city = models.ForeignKey(
        City, related_name="route_start", on_delete=models.CASCADE
    )
    end_city = models.ForeignKey(
        City, related_name="route_end", on_delete=models.CASCADE
    )
    distance = models.FloatField()

    def save (self, *args, **kwargs): #para hacer automáticamente la ruta inversa
        super().save(*args, **kwargs) #llama al método save() original para guardar la ruta

        #Verifica si la ruta inversa ya existe si no la creamos
        if not Route.objects.filter( start_city=self.end_city, end_city=self.start_city).exists():
            #Crea la ruta inversa automáticamente con la misma distancia
            Route.objects.create(start_city=self.end_city, end_city=self.start_city, distance=self.distance)


    def __str__(self):
        return f"{self.start_city} -> {self.end_city} ({self.distance} km)"
