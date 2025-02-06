from src.core.models.base import *


class Region(BaseModel):
    """ viloyatlar uchun model """
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "regions"
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, related_name="districts", null=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "districts"
        ordering = ("region",)

    def __str__(self):
        return str(self.name)


class FileManager(BaseModel):
    """ Uploaded images """
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    class Meta:
        db_table = "images"
        ordering = ("-id",)
