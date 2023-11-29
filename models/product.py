import uuid
import datetime
import models.base_model as base
import models.import_order as ipo
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
      raise ValueError("Tong gia tien phai lon hon 0")
    self._total_price = total_price
    
  def set_final_price(self, final_price):
    if final_price is not None and final_price < 0:
      raise ValueError("Tien hang thuc te phai lon hon 0.")
    self._final_price = final_price
    
  
  
def date(str_like_date):
  return datetime.datetime.strptime(str_like_date, '%d/%m/%Y')

def get_user_input(message, parse_to=int, error_message="Khong hop le, xin thu lai"):
  while True:
    try:
      data = parse_to(input(message))
      return data
    except Exception as err:
      if (error_message):
        print(error_message)
      else:
        print(err)

def _compute_total_price_in(order):
  total = 0
  for p in order.get_product_list():
    total += p.get_final_price()
  return total
class ManageProduct:
  def __init__(self):
    # type Product
    self.__products = []
    # type ImportOrder
    self.__import_orders = []

  def add_product(self, product):
    if not isinstance(product, Product):
      raise ValueError("Ban phai truyen tham so la mot Product")
    self.__products.append(product)

  def get_products(self):
    products = []
    for product in self.__products:
      products.append(product.json())
    for product in products:
      print("Ma hang: ",product["id"])
      print("Ten hang: ",product["name"])
      print("Gia ban: ", product["price_out"])
      print("Gia nhap: ",product["price_in"])
      print("Ton kho: ",product["nbr_products"])
      print("Ngay san xuat: ",product["mfg"])
      print("Ngay het han: ",product["exp"])
      print("\n")
    return products
    
  def search_by_name(self, name : str):
    products = []
    for product in self.__products:
      if product.get_name() and name.lower() in product.get_name().lower():
         products.append(product.json())
    return products
  
  def sum_price_in_of_each_product(self):

    _sum = {}

    for i in self.__import_orders:
      
      for j in i.get_product_list():
        x = _sum.get(j.get_id(), 0)
        _sum[j.get_id()] = x + j.get_final_price()
    
    data = []
    for key, value in _sum.items():
      data.append({
        "id": key,
        "total" : value
      })

    
    return data
  

  def sum_nbr_of_sold_product_of_each_product(self):
    _sum = {}

    for i in self.__import_orders:
      for j in i.get_product_list():
        x = _sum.get(j.get_id(), 0)
        _sum[j.get_id()] = x + j.get_nbr_products()
    
    data = []
    for key, value in _sum.items():
      data.append({
        "id": key,
        "total" : value
      })

    
    return data

  def search_import_orders(self, month : int, year : int):
    if month <= 0 or month > 12:
      raise ValueError('Thang phai nam trong khoang tu 1 - 12')
    if year <= 0:
      raise ValueError('Nam phai la mot so duong')
    found_orders = []
    for order in self.__import_orders:
      import_date = order.get_import_date()
      _year = import_date.year
      _month = import_date.month
      if _year == year and _month == month and isinstance(order, base.Printable):
        found_orders.append(order.json())

    return found_orders
  
  def sort_sum_price_in(self, reverse=False):
    data = self.sum_price_in_of_each_product()
    sorted_data = sorted(data, key=lambda x: x["total"], reverse=reverse)    
    return sorted_data


  #7
  def show_top5_high_low_pricein(self):
    product_list = self.sort_sum_price_in()
    if len(product_list)==0:
      print("Chưa có hóa đơn nào.")
    else:
      high_product = product_list[:5]
      low_product = product_list[-5:]
      print ("top 5 hang hoa co tong nhap cao nhat va thap nhat: ")
      for item in high_product:
        product_name, total_price = item
        print(f"Tên sản phẩm: {product_name}, Tổng giá: {total_price}")
      print("\n")
      for item in low_product:
        product_name, total_price = item
        print(f"Tên sản phẩm: {product_name}, Tổng giá: {total_price}")
    return product_list
  #8: DONE
  def set_new_price_out(self):
    exp_product=[]
    for product in self.__products:
      date_about_to_exp = product.get_exp() - product.get_mfg()
      if (date_about_to_exp.days < 14):
        new_price_out = product.get_price_out()*0.45
        product._price_out = new_price_out
        exp_product.append(product)
      elif (14 < date_about_to_exp.days <= 31):
        new_price_out = product.get_price_out()*0.8
        product._price_out = new_price_out
        exp_product.append(product)
      else:
        print("Cac hang hoa van con han su dung")
    return exp_product
  
  #9:
  def need_import_later(self):
    # lay 10 hang hoa ton kho it nhat:
    least_remain = []

    for i in self.__products:
      least_remain.append({
        "id": i.get_id(),
        "remain" : i.get_nbr_products()
      })

    least_remain = sorted(least_remain, key=lambda x: x["remain"])

   
    # top 10 hang hoa con it nhat kho:

    least_remain = least_remain[:10]

    # tim top 15 hang ban chay nhat

    total_sold = self.sum_nbr_of_sold_product_of_each_product()

    total_sold = sorted(total_sold, key=lambda x : x["total"], reverse=True)

    num =  len(total_sold)

    start = num - 15

    total_sold = total_sold[start if start >=0 else 0:num]
   
    
    need_to_import_ids = []

    for p in least_remain:
      for top in total_sold:
        if p["id"] == top["id"]:
          need_to_import_ids.append(p["id"]) 
    
    need_to_import = []

    for product in self.__products:
      if product.get_id() in need_to_import_ids:
        need_to_import.append(product.json())

    return need_to_import

  #10: DONE
  def edit_product(self, id:str):

    product = None

    for p in self.__products:
      if p.get_id() == id:
        product = p
        break

    if product is None:
      raise ValueError("Ma hang hoa khong ton tai")

    new_name = get_user_input("Nhap ten moi: ", parse_to=str)
    new_price_in = get_user_input("Nhap gia moi: ", parse_to=int, error_message="Gia tien khong le, ban phai nhap mot so.")
    new_price_out = get_user_input("Nhap gia xuat moi: ", parse_to=int, error_message="Gia xuat khong hop le, ban phai nhap mot so.")
    new_nbr_products = get_user_input("Nhap so san pham moi: ", parse_to=int, error_message="Khong hop le, ban phai nhap mot so")
    exp = get_user_input("Enter expiration day (dd/MM/yyyy): ", parse_to=date, error_message="Khong hop le, ngay thang phai co dang dd/MM/yyyy")

    mfg = get_user_input("Nhap ngay san xuat (dd/MM/yyyy): ", parse_to=date, error_message="Khong hop le, ngay thang phai co dang dd/MM/yyyy")
    product._name = new_name 
    product._price_out = new_price_in
    product._price_in = new_price_out
    product._nbr_products = new_nbr_products
    product._exp = exp
    product._mfg = mfg 
    return product      

  #11
  def del_product(self, id:str):
    product = None

    for p in self.__products:
      if p.get_id() == id:
        product = p
        break
    if product is None:
      raise ValueError("Ma san pham khong ton tai.")
    else:
      self.__products.remove(product)
  #12
  def add_import_order(self, import_date, product_list):
    self.__import_orders.append(ipo.ImportOrder(product_list=product_list, import_date=import_date))
  
  def print_invoices(self):
    for invoice in self.__import_orders:
      print("\nNgay nhap hang:", invoice[0])
      print("----Danh sach don hang---------")
      for item in invoice[1]:
        print("Ten hang:", item[0])
        print("Gia nhap:", item[1])
        print("So luong nhap:", item[2])
        print("Thanh tien:", item[3])
        print("Tong tien:", item[4])
        print("\n")
      print("-----------------------------")



# p = Product(name="Hellp", price_in=10214, price_out=1324, 
#              nbr_products=102, mfg=datetime.datetime.now(), 
#              exp=datetime.datetime.now())
# manager = ManageProduct()

# manager.add_product(p)
# print(manager.get_products()) 

