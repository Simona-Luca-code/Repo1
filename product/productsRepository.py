from repositoryInterface import RepositoryInterface
from product.product import Product


class ProductsRepository(RepositoryInterface):

     def __init__(self):
         self.products = []

     def create(self, data):
         product_id = len(self.products) + 1
         new_product = Product(product_id,data["name"],data["price"],data["quantity"])
         self.products.append(new_product)


     def read(self, entry_id):
         for product in self.products:
             if product.product_id == entry_id:
                 print("Produsul a fost gasit, mai jos gasim detaliile produsului: " )
                 print(f"Numele produsului este: {product.name}")
                 print(f"Pretul este:{product.price} ")
                 print(f"Cantitatea de produse este: {product.quantity}")
                 break
         else:
           print(f"The product with id {entry_id} is not available.")

     def update(self, entry_id, new_data):
        for product in self.products:
            if product.product_id == entry_id:
               # product.product_id = new_data["entry_id"]
                product.name = new_data["name"]
                product.price = new_data["price"]
                product.quantity = new_data["quantity"]
                print("Produsul a fost actualizat")
                break
        else:
            print("Produsul nu a fost gasit!")

     def delete(self, entry_id):
         for product in self.products:
             if product.product_id == entry_id:
                 self.products.remove(product)
                 print("Produsul a fost sters")
                 break
         else:
             print("Produsul nu a fost gasit!")