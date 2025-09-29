from django.core.management.base import BaseCommand
import csv
from cat.models import Breed, Cat

class Command(BaseCommand):
    help = 'Load cats from CSV'

    def handle(self, *args, **kwargs):
        with open('cats.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                print(row)
                name, breed_name, weight = row
                breed, created = Breed.objects.get_or_create(name=breed_name)
                Cat.objects.create(nickname=name, breed=breed, weight=float(weight))

        self.stdout.write(self.style.SUCCESS('Cats loaded successfully!'))

'''
- Reads cats.csv
- Skips header row
- Creates Breed objects if missing
- Creates Cat objects linked to Breed

'''