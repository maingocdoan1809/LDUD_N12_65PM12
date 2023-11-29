import re
from datetime import datetime
import models.product as product


def check_positive_integer(num):
  num = int(num)
  if num < 0:
    raise ValueError(f'{num} la mot so am')
  return num


def display_menu():
  print("----------------------------------------------------------------------------------------------------------")
  print("-                                                                                                        -")
  print("-                                          Moi lua chon:                                                 -")
  print("-                                                                                                        -")
  print("----------------------------------------------------------------------------------------------------------")
  print("-                                                |                                                       -")
  print("- 1. Them moi hang hoa                           |    7. Top hang hoa tong tien nhap cao nhat, thap nhat            -")
  print("- 2. Danh sach hang hoa                          |    8. Hien thi danh sach hang can nhap                -")
  print("- 3. Tim kiem hang hoa theo ten                  |    9. Nhap hang                                       -")
  print("- 4. Sua thong tin san pham                      |    10. Xoa hang                                       -")
  print("- 5. Sap xep theo tong tien nhap hang            |    11. Thoat chuong trinh                             -")
  print("- 6. Danh sach hang hoa sap het han su dung      |                                                       -")
  print("-                                                |                                                       -")
  print("----------------------------------------------------------------------------------------------------------")

manager = product.ManageProduct()

while True:
  # Hien thi menu #
  display_menu()
  
  # Nhap lua chon #
  while True:
    try:
        choice = int(input("Lua chon: "))
        if choice <= 0 or choice > 11:
            raise ValueError("Vui long chon cac chuc nang tu 1 -> 11.")
        break
    
    except ValueError:
        print("Vui long chon cac chuc nang tu 1 -> 11.")
  
  # Xu ly lua chon #
  match choice:
    
    case 1:

      # Them hang hoa
      try:

        # Nhap ten #
        name = product.get_user_input("Nhap ten: ", parse_to=str, error_message="Loi, xin moi nhap lai ten.")

        # Nhap gia ban #
        price_out = product.get_user_input("Nhap gia ban: ", parse_to=check_positive_integer, error_message="Gia ban khong hop le, xin moi nhap lai.")

        # Nhap gia nhap #
        price_in = product.get_user_input("Nhap gia nhap: ", parse_to=check_positive_integer, error_message="Gia nhap khong hop le, xin moi nhap lai.")

        # Nhap so luong ton kho #
        nbr_product = product.get_user_input("Nhap so luong ton kho: ", parse_to=check_positive_integer, error_message="So luong khong hop le, xin moi nhap lai.")


        # Nhap ngay san xuat #
        mfg = product.get_user_input("Nhap ngay san xuat (dd/mm/yyyy): ", parse_to=product.date, error_message= "Ngay san xuat khong hop le, xin moi nhap lai.")

        # Nhap ngay het han #
        while True:
          exp = product.get_user_input("Nhap ngay het han (dd/MM/yyyy): ", parse_to=product.date, error_message="Ngay het han khong hop le, xin moi nhap lai.")
          if exp < mfg:
            print("Error: Ngay het han phai lon hon ngay san xuat.")
          else:
            break

        
        # Them hang hoa #
        pd = product.Product(name,price_out,price_in,nbr_product,exp=exp,mfg=mfg)
        #print(pd._name)

        manager.add_product(pd)

        print("Them thanh cong.")

      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 2:

      # Danh sach hang hoa
      try:
        print("Day la danh sach hang hoa: ") 
        x = manager.get_products()
      except Exception as e:
        print(e)

    case 3:

      # Tim kiem hang hoa theo ten
      try:
        name = input("Ten:")
        while True:
          if name is None:  
            name = input("Nhap lai ten: ")
          else:
            break     
        tim_kiem_theo_ten = manager.search_by_name(name)
        if not tim_kiem_theo_ten or len(tim_kiem_theo_ten) == 0:
          print("Khong co san pham nao duoc tim thay")
        else:
          print("Da tim thay:")
          for i in tim_kiem_theo_ten:
            print(i) 
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")
     
    # Sua thong tin hang hoa theo id
    case 4:
      try:        
        id = input("Nhap ma hang hoa: ")        
        
        manager.edit_product(id)
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")
    
    # Sap xep hang hoa theo tong tien nhap hang
    case 5:
      try:
        sap_xep = input("Tang hay giam: ")
        while True:
          if sap_xep.lower() in ["tang", 'giam']:
            if sap_xep.lower() == 'tang':
              reverse = False
              break         
            else:
              reverse = True
              break
          else:
            sap_xep = input("Nhap lai: ")
        
        list_x = manager.sort_sum_price_in(reverse)
        if not list_x or len(list_x) == 0:
          print("Khong co san pham nao.")
        else:
          print("Sau khi sap xep: ")
          for product_name, total_price in list_x.items():
            print(product_name, ": ", total_price)
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")
      
    # Danh sach hang hoa sap het han su dung
    case 6:
      exp_products = manager.set_new_price_out()
      if len(exp_products)==0:
        print("khong co hang hoa")
      else: 
        print("Cac hang hoa sap het han su dung")
        for product in exp_products:
          date_about_to_exp = product.get_exp() - product.get_mfg()
          print(f"Tên: {product.get_name()}, Giá bán mới: {product.get_price_out()}, Còn {date_about_to_exp}")

    # Top 5 hang hoa co gia nhap cao nhat, thap nhat
    case 7:
      try:
        result =  manager.show_top5_high_low_pricein()
        
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    #đang để tạm là hàm in hoá đơn
    case 8:
      # Hien thi danh sach hang can nhap 
      # Co ham se them sau 
      try:
        x = manager.need_import_later()
        if len(x) == 0:
          print("Chua du du lieu don nhap hang thong ke")
          pass
        print("Day la danh sach cac ID hang hoa can nhap: ") 
        for i in x:
          print(i)
      except Exception as e:
        print(e)

    case 9:
      # Nhap hang 
      product_list = []
      import_date = None
      while True:
        import_date = input("Nhap ngay nhap hang (dd/mm/yy): ")
        try:
            # Chuyển đổi ngày từ chuỗi nhập vào
          datetime_object = datetime.strptime(import_date, "%d/%m/%Y")
          break
        except ValueError:
          print("Ngay nhap khong hop le. Vui long nhap lai theo dinh dang dd/mm/yy.")

      while True:
      # create an empty list for the products
      # ask the user to enter the number of products
        product_name = input("Nhap ten hang (nhap 'exit' de ket thuc): ")
        if product_name.lower() == 'exit':
          break

        while True:
          try:
            price = int(input("Nhap gia: "))
            if price < 0:
              raise ValueError("Gia phai la so nguyen duong.")
            break
          except ValueError:
            print("Gia nhap khong hop le. Vui long nhap lai.")
            
        while True:
          try:
            nbr_product_in = int(input("Nhap so luong: "))
            if nbr_product_in < 0:
              raise ValueError("So luong phai la so nguyen duong.")
            break
          except ValueError:
              print("So luong nhap khong hop le. Vui long nhap lai.")
        thanhtien = price * nbr_product_in
        tongtien = thanhtien
          # create a dictionary for the product
        product = [product_name, price, nbr_product_in, thanhtien, tongtien]
        # add the product to the list of products
        product_list.append(product)
      if len(product_list) > 0:
        manager.add_import_order(import_date, product_list)
        print("Nhap hang thanh cong.")
      else:
        print("Da huy do khong co hang hoa trong hoa don")

    case 10:

      # Xoa hang hoa
      try:
        id = input("Nhap ma hang: ")
        try:
          manager.del_product(id)
          print("Da xoa thanh cong")
        except Exception as err:
          print(err)
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")
    case 11:

      # Thoat chuong trinh
      print("Da thoat chuong trinh")
      break

# x = [
#   {"id" : 1, "name" : "103"},
#   {"id" : 2, "name" : "103"},
#   {"id" : 4, "name" : "103"},
#   {"id" : 3, "name" : "103"},
# ]
# print(x)

