from src.core.models.base import *


class Stadion(BaseModel):
    """ Stadion lar ro'yhati uchun """
    name = models.CharField(max_length=255, verbose_name="Maydon nomi")
    region = models.ForeignKey("Region", on_delete=models.SET_NULL, related_name="stadiums", null=True)
    district = models.ForeignKey("District", on_delete=models.SET_NULL, related_name="stadiums", null=True)
    address = models.CharField(max_length=255, null=True)
    length = models.DecimalField(max_digits=20, decimal_places=2)
    width = models.DecimalField(max_digits=20, decimal_places=2)
    varata_height = models.DecimalField(max_digits=10, decimal_places=2)
    varata_width = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    description = models.TextField(verbose_name="Qo'chimcha malumot")

    class Meta:
        ordering = ("-id",)
        db_table = "stadiums"

    def __str__(self):
        return str(self.name)


class StadionContact(BaseModel):
    """ Stadion egalarining contactlari """
    stadion = models.ForeignKey("Stadion", on_delete=models.CASCADE, related_name="contacts")
    f_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ("-id",)
        db_table = "stadion_contacts"

    def __str__(self):
        return f"{self.f_name} {self.phone}"


class StadionImages(BaseModel):
    """ Stadion Rasmlari """
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey("FileManager", on_delete=models.CASCADE, related_name="stadiums_images")

    class Meta:
        ordering = ("-id",)
        db_table = "stadion_images"

    def __str__(self):
        return f"{self.stadion.name}'s image"
