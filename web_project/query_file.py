# query_file.py

from models import Product

def get_entries_by_age(age):
    """
    Gibt Einträge zurück, deren 'age' größer als der angegebene Wert ist.
    """
    return Product.objects.filter(age__gt=age)
