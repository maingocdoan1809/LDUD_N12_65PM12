import re
from datetime import datetime
from models import product

manager = product.ManageProduct

def display_menu():
  print("----------------------------------------------------------------------------------------------------------")
  print("-                                          Moi lua chon:                                                 -")
  print("----------------------------------------------------------------------------------------------------------")
  print("- 1. Them moi hang hoa                           |    7. Top hang hoa tong tien nhap cao nhat            -")
  print("- 2. Danh sach hang hoa                          |    8. Hien thi danh sach hang can nhap                -")
  print("- 3. Tim kiem hang hoa theo ten                  |    9. Nhap hang                                       -")
  print("- 4. Sua thong tin san pham                      |    10. Xoa hang                                       -")
  print("- 5. Sap xep theo tong tien nhap hang            |    11. Thoat chuong trinh                             -")
  print("- 6. Danh sach hang hoa sap het han su dung      |                                                       -")
  print("----------------------------------------------------------------------------------------------------------")

while True:
  display_menu()
  choice = input("Lua chon: ")
  match choice:
    case "1":

      # Them hang hoa
      
      try:

        # Nhap ten #
        
        name = input("Ten:")
        while True:
          if name is None:  
            name = input("Nhap lai ten: ")
          else:
            break

        # Nhap gia ban #

        price_out = int(input("Gia ban hang: "))
        while True:
          if price_out is not isinstance(price_out, int) or price_out < 0:
            price_out = int(input("Nhap lai gia ban hang: "))
          else:
            break

        # Nhap gia nhap #

        price_in = input("Gia nhap: ")
        while True:
          if price_in is not isinstance(price_in, int) or price_in < 0:
            price_in = int(input("Nhap lai gia nhap hang: "))
          else:
            break

        # Nhap so luong ton kho #

        nbr_product = int(input("Nhap so luong ton kho: "))
        while True:
          if nbr_product is not isinstance(nbr_product,int) or nbr_product < 0:
            nbr_product = int(input("Nhap lai so luong ton kho: "))
          else:
            break

        # Nhap ngay het han #

        exp = input("Nhap ngay het han (dd-MM-yyyy): ")
        while True:

          # K dung pattern, nhap lai

          if not re.match('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}',exp):
            exp = input("Nhap lai ngay het han (dd-MM-yyyy)")
          else:
            exp_date = datetime.strptime(exp,'%d-%m-%Y')
            break

        # Nhap ngay san xuat #

        mfg = datetime.now()
        while True:

          # K dung pattern, nhap lai

          if not re.match('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}',mfg):
            mfg = input("Nhap lai ngay het han (dd-MM-yyyy)")
          else:
            mfg_date = datetime.strptime(mfg,'%d-%m-%Y')
            break

        # Them hang hoa #

        pd = product.Product(name,price_out,price_in,nbr_product,exp,mfg)
        if manager.add_product(pd):
          print("Them thanh cong")
        else:
          print("Them that bai")
      except Exception:
        print("An error occurred! ")

    case "2":

      # Danh sach hang hoa

      try: 
        x =  manager.get_products()
        print(x)
      except Exception:
        print("An error occurred! ")
    case "3":

      # Tim kiem hang hoa theo ten

      try:
        name = input("Ten:")
        while True:
          if name is None:  
            name = input("Nhap lai ten: ")
          else:
            break     
        tim_kiem_theo_ten = manager.search_by_name(name)
        print(tim_kiem_theo_ten)   
      except Exception:
        print("An error occurred! ")

    case "4":

      # Sua thong tin hang hoa theo id

      try:
        id = input("Nhap ma san pham: ")
        manager.edit_product(id)
      except Exception:
        print("An error occurred! ")

    case "5":

      # Sap xep hang hoa theo tong tien nhap hang

      try:
        sap_xep = input("Tang hay giam: ")
        while True:
          if not re.match('[Tt]ang',sap_xep) or re.match('[Gg]iam',sap_xep):
            sap_xep = input("Nhap lai: ")
          else:
            break

          if re.match('[Tt]ang',sap_xep):
            reverse = True         
          elif re.match('[Gg]iam',sap_xep):
            reverse = False      
                  
          list = manager.sort_by_price_in(reverse)
          print(list)
      except Exception:
        print("An error occurred! ")

    case "6":

      # Danh sach hang hoa sap het han su dung
      # Co ham se them vao sau

      pass

    case "7":

      # Top 5 hang hoa co gia nhap cao nhat, thap nhat

      try:
        manager.show_top5_high_low_pricein()
      except Exception:
        print("An error occurred! ")

    case "8":

      # Hien thi danh sach hang can nhap 
      # Co ham se them sau 

      pass

    case "9":

      # Nhap hang 
      # Co ham se them sau 

      pass
    case "10":

      # Xoa hang hoa

      try:
        id = input("Nhap ma hang can xoa: ")
        manager.del_product(id)
      except Exception:
        print("An error occurred! ")

    case "11":

      # Thoat chuong trinh

      print("Da thoat chuong trinh")
      break

    case default:
      choice  = input("Hay lua chon lai: ")

x = [
  {"id" : 1, "name" : "103"},
  {"id" : 2, "name" : "103"},
  {"id" : 4, "name" : "103"},
  {"id" : 3, "name" : "103"},
]
