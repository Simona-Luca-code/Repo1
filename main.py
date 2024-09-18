from product.product import Product
from product.productsRepository import ProductsRepository

product_repository1 = ProductsRepository()
product_repository1.create({"name" : "orhidee", "price" : 60,"quantity" : 3})
product_repository1.create({"name" : "crin", "price" : 15,"quantity" : 2})
product_repository1.create({"name" : "trandafir", "price" : 50,"quantity" : 10})

product_repository1.read(1)
product_repository1.read(3)
product_repository1.read(10)
product_repository1.update(3,{"name": "bujor","price": 10, "quantity" : 5} )
product_repository1.read(3)
product_repository1.delete(2)
product_repository1.read(2)

#product_repository1.update(3,{"nume": "bujor","pret": 10, "quantity" : 5} )

"""
modificare fisier git
"""



