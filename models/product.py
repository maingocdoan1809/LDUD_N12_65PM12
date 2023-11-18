import uuid
import datetime
import base_model as base
class Product(base.BaseProduct, base.Expirable, base.Importable, base.Exportable):
  
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

  
p = Product(name="Hello world",exp=datetime.datetime.now(), 
            mfg=datetime.datetime.now(), price_in=10, price_out=10,
            nbr_products=12)

class OrderProduct(base.BaseProduct, base.Importable):
  def __init__(self, name, 
               price_in=None,
               nbr_products=None, total_price=None, final_price=None):
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
    
  
  

    


