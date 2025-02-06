import django_filters

import src.core.models as models


class StadionFilterSet(django_filters.FilterSet):
    region = django_filters.NumberFilter(field_name="region_id")
    district = django_filters.NumberFilter(field_name="district_id")

    class Meta:
        model = models.Stadion
        fields = ("region", "district",)
