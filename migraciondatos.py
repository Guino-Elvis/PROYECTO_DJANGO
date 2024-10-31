import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyectoweb.settings")
django.setup()

from crm.models.categoria import Categoria
from crm.models.producto import Producto


fake = Faker()


def migraciondatos(num_categories=5, num_productos=10):

    for _ in range(num_categories):
        cat = Categoria(
            name=fake.word().capitalize(),
            tag=fake.word(),
            estado=fake.random_element(elements=("activo", "inactivo")),
        )
        cat.save()

    categories = Categoria.objects.all()
    for _ in range(num_productos):
        prod = Producto(
            name=fake.word().capitalize(),
            descrip=fake.sentence(nb_words=6),
            estado=fake.random_element(elements=("activo", "disponible")),
            categoria=fake.random_element(elements=categories),
        )
        prod.save()

    print("Categorías:")
    for cat in Categoria.objects.all():
        print(cat)

    print("\nProductos:")
    for prod in Producto.objects.all():
        print(prod)


if __name__ == "__main__":
    migraciondatos()
