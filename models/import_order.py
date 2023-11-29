import uuid
import datetime
import models.base_model as base
import models.product as pd
class ImportOrder(base.Indexable, base.Printable):


  def __init__(self, product_list : list, import_date=None) -> None:
    base.Indexable.__init__(self)
    for product in product_list:
      if not isinstance(product, pd.OrderProduct):
        raise ValueError ("Product phai co kieu OrderProduct")
    #type OrderProduct
    self.__product_list = product_list
    #type datetime
    self.__import_date = import_date 

  def add_product(self, products):
    for product in products:
      if not isinstance(product, pd.OrderProduct):
        raise ValueError ("Product phai co kieu OrderProduct")
      self.__product_list.append(product)


  def get_product_list(self):
    return self.__product_list
  def get_import_date(self):
    return self.__import_date
  
  def set_import_date(self,date):
    if not isinstance(date, datetime.datetime):
      raise ValueError ("Ngay nhap phai co kieu datetime")
    self.__import_date = date

  def json(self):
    return {
      "id" : self.get_id(),
      "import_date" : self.get_import_date(),
      "products" : self.get_products(),
    }

  


