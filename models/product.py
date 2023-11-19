import uuid
import datetime
import base_model as base
class Product(base.BaseProduct, base.Expirable, base.Importable, base.Exportable, base.Printable):
  
  @staticmethod
  def _generate_id():
    return uuid.uuid4().hex

  def __init__(self, name, 
               price_out=None, 
               price_in=None,
               nbr_products=None,
               exp=None, mfg=None ) -> None:
    base.BaseProduct.__init__(self,name=name)
    base.Expirable.__init__(self,exp=exp,mfg=mfg)
    base.Importable.__init__(self,price_in=price_in, nbr_products=nbr_products)
    base.Exportable.__init__(self,price_out=price_out)

  def json(self):
    product = self
    return {
        "id" : product.get_id(),
        "name" : product.get_name(),
        "price_in": product.get_price_in(),
        "price_out": product.get_price_out(),
        "exp": product.get_exp(),
        "mfg": product.get_mfg(),
        "nbr_products": product.get_nbr_products(),
      }


class OrderProduct(base.BaseProduct, base.Importable):
  def __init__(self, 
               name, 
               price_in=None,
               nbr_products=None, 
               total_price=None, 
               final_price=None):
    base.BaseProduct.__init__(self,name=name)
    base.Importable.__init__(self,price_in=price_in, nbr_products=nbr_products)

    if total_price is not None and total_price < 0:
      raise ValueError("Total price must be greater than zero.")
    if final_price is not None and final_price < 0:
      raise ValueError("Final price must be greater than zero.")
    self._total_price = total_price
    self._final_price = final_price


  def get_total_price(self):
    return self._total_price
  def get_final_price(self):
    return self._final_price
  
  def set_total_price(self, total_price):
    if total_price is not None and total_price < 0:
      raise ValueError("Total price must be greater than zero.")
    self._total_price = total_price
    
  def set_final_price(self, final_price):
    if final_price is not None and final_price < 0:
      raise ValueError("Final price must be greater than zero.")
    self._final_price = final_price
    
  
  

    


class ManageProduct:
  def __init__(self):
    self.__products = []
    self.__import_orders = []

  def add_product(self, product):
    if not isinstance(product, Product):
      raise ValueError("Param must be a type of Product")
    self.__products.append(product)

  def get_products(self):
    products = []
    for product in self.__products:
      products.append(product.json())
    return products
  
  def search_by_name(self, name : str):
    products = []
    for product in self.__products:
      if product.get_name() and name in product.get_name().lower():
         products.append(product.json())
    return products
  
  def sum_price_in(self):
    return sum(product.get_price_in() * product.get_nbr_products for product in self.__products)
  
  def search_import_orders(self, month : int, year : int):
    if month <= 0 or month > 12:
      raise ValueError('Month must be between 1 and 12')
    if year <= 0:
      raise ValueError('Year must be a positive integer')
    found_orders = []
    for order in self.__import_orders:
      import_date = order.get_import_date()
      _year = import_date.year
      _month = import_date.month
      if _year == year and _month == month and isinstance(order, base.Printable):
        found_orders.append(order.json())

    return found_orders
  
  def sort_by_price_in(self, reverse=False):
    sorted_orders = sorted(self.__import_orders, 
                           lambda x, y: (x.get_price_in() * x.get_nbr_products) > (y.get_price_in() * y.get_nbr_products)
                           ,reverse=reverse)


p = Product(name="Hellp", price_in=10214, price_out=1324, 
             nbr_products=102, mfg=datetime.datetime.now(), 
             exp=datetime.datetime.now())
manager = ManageProduct()

manager.add_product(p)
print(manager.get_products()) 