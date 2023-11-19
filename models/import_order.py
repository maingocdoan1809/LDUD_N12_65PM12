import uuid
import datetime
import base_model as base
import product as pd
class ImportOrder(base.Indexable, base.Printable):


  def __init__(self, product_list : list, import_date=None) -> None:
    base.Indexable.__init__(self)
    if import_date is not None and not isinstance(import_date, datetime.datetime):
      raise ValueError ("Import date must be a datetime object")
    
    for product in product_list:
      if not isinstance(product, pd.Product):
        raise ValueError ("Product in production must be of type Product")
    for product in product_list:
      if not isinstance(product, pd.Product):
        raise ValueError ("Product in production must be of type Product")

    self.__product_list = product_list
    self.__import_date = import_date 

  def add_product(self, products):
    for product in products:
      if not isinstance(product, pd.Product):
        raise ValueError ("Product in products must be of type Product")
      self.__product_list.append(product)


  def get_product_list(self):
    return self.__product_list
  def get_import_date(self):
    return self.__import_date
  
  def set_import_date(self,date):
    if not isinstance(date, datetime.datetime):
      raise ValueError ("Import date must be a datetime")
    self.__import_date = date

  def json(self):
    return {
      "id" : self.get_id(),
      "import_date" : self.get_import_date(),
      "products" : self.get_products(),
    }

  


