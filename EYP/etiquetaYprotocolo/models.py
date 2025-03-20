from django.db import models

# Clase Padre: Contiene la información general de la empresa
class Company(models.Model):
    name = models.CharField(max_length=200)  # Nombre de la empresa
    nit = models.BigIntegerField(unique=True)  # NIT de la empresa
    address = models.CharField(max_length=255)  # Dirección de la empresa
    telephone = models.CharField(max_length=20)  # Teléfono de la empresa

    def __str__(self):
        return f"{self.name} - NIT: {self.nit}"

# Clase Hija de Company: Relacionada con la empresa a través de una clave foránea
class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Relación con la empresa (Padre)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=400000)  # Costo del servicio

    def __str__(self):
        return f"Servicio de {self.company.name} - ${self.cost}"

# Clase Nieta de Company: Relacionada con Service
class Protocol(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='protocol_list')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Clase Nieta de Company: Relacionada con Service
class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='tag_list')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Clase para Solicitudes de Servicio
class ServiceRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    protocols = models.ManyToManyField(Protocol)
    tags = models.ManyToManyField(Tag)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Solicitud de {self.customer_name} - Total: ${self.total_cost}"

# Clase para Recibos
class Receipt(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recibo para {self.service_request.customer_name}"
