import uuid
import datetime
import base_model as base
import product as pd
class ImportOrder(base.Indexable):


  def __init__(self, product_list : list, import_date=None) -> None:
    base.Indexable.__init__(self)
    if import_date is not None and not isinstance(import_date, datetime.datetime):
      raise ValueError ("Import date must be a datetime object")
    
    for product in product_list:
      if not isinstance(product, pd.Product):
        raise ValueError ("Product in production must be of type Product")

    self.__product_list = product_list
    self.__import_date = import_date 

  
i = ImportOrder([])


