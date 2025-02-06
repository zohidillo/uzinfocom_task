import json

from django.core.management.base import BaseCommand

import src.core.models as models


class Command(BaseCommand):
    help = 'Install regions and districts'

    def handle(self, *args, **options):
        with open('src/resources/regions.json', 'r') as f:
            regions = json.load(f)
            for item in regions:
                if not models.Region.objects.filter(name=item.get('name')).exists():
                    models.Region.objects.create(name=item.get('name'))
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Region id: {item.get('id')}, name: {item.get('name')} created"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Region id: {item.get('id')}, name: {item.get('name')} already exists"
                        )
                    )
        with open('src/resources/districts.json', 'r') as f:
            districts = json.load(f)
            for i in districts:
                if not models.District.objects.filter(name=i.get("name")).exists():
                    models.District.objects.create(region_id=i.get("region_id"), name=i.get("name"))
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"District id: {i.get('id')}, name: {i.get('name')} created"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"District id: {i.get('id')}, name: {i.get('name')} already exists"
                        )
                    )
