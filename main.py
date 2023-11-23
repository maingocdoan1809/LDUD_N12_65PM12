import re
from datetime import datetime
import models.product as product

def display_menu():
  print("----------------------------------------------------------------------------------------------------------")
  print("-                                                                                                        -")
  print("-                                          Moi lua chon:                                                 -")
  print("-                                                                                                        -")
  print("----------------------------------------------------------------------------------------------------------")
  print("-                                                |                                                       -")
  print("- 1. Them moi hang hoa                           |    7. Top hang hoa tong tien nhap cao nhat            -")
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
  choice = int(input("Lua chon: "))
  while choice is None or (not isinstance(choice, int) or choice <= 0 or choice >= 12):
      choice = int(input("Hay chon lai: "))
  
  # Xu ly lua chon #
  match choice:
    
    case 1:

      # Them hang hoa
      try:

        # Nhap ten #
        name = input("Ten: ")
        while True:
          if name is None:  
            name = input("Nhap lai ten: ")
          else:
            break

        # Nhap gia ban #
        price_out = int(input("Gia ban hang: "))
        while True:
          if price_out is None:
            price_out = int(input("Nhap lai gia ban hang: "))
          elif price_out is not None and ( not isinstance(price_out, int) or price_out < 0 ):
            price_out = int(input("Nhap lai gia ban hang: "))
          else:
            break

        # Nhap gia nhap #
        price_in = int(input("Gia nhap hang: "))
        while True:
          if price_in is None:
            price_in = int(input("Nhap lai gia nhap hang: "))
          elif price_in is not None and ( not isinstance(price_in, int) or price_in < 0 ):
            price_in = int(input("Nhap lai gia nhap hang: "))
          else:
            break

        # Nhap so luong ton kho #
        nbr_product = int(input("Nhap so luong ton kho: "))
        while True:
          if nbr_product is not None and (not isinstance(nbr_product, int) or nbr_product < 0 ):
            nbr_product = int(input("Nhap lai so luong ton kho: "))
          else:
            break

        # Nhap ngay het han #
        exp = input("Nhap ngay het han (dd/MM/yyyy): ")
        while True:

          # K dung pattern, nhap lai
          if re.match(r'(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}',exp):
            exp_date = datetime.strptime(exp,'%d/%m/%Y')
            break            
          else:
            exp = input("Nhap lai ngay het han (dd/MM/yyyy): ")

        # Nhap ngay san xuat #
        mfg = input("Nhap ngay san xuat (dd/mm/yyyy): ")
        while True:

          # K dung pattern, nhap lai
          if re.match(r'(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}',mfg):
            mfg_date = datetime.strptime(mfg,'%d/%m/%Y')
            break
          else:
            mfg = input("Nhap lai ngay san xuat (dd/MM/yyyy): ")

        # Them hang hoa #
        pd = product.Product(name,price_out,price_in,nbr_product,exp_date,mfg_date)
        #print(pd._name)

        manager.add_product(pd)

      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 2:

      # Danh sach hang hoa
      try:
        print("Day la danh sach hang hoa: ") 
        x = manager.get_products()
        print(x)
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
        print(tim_kiem_theo_ten) 
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 4:

      # Sua thong tin hang hoa theo id
      try:        
        id = input("Nhap ma hang hoa: ")        
        manager.edit_product(id)
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 5:

      # Sap xep hang hoa theo tong tien nhap hang
      try:
        sap_xep = input("Tang hay giam: ")
        while True:
          if re.match('[Tt]ang',sap_xep) or re.match('[Gg]iam',sap_xep):
            if re.match('[Tt]ang',sap_xep):
              reverse = True
              break         
            elif re.match('[Gg]iam',sap_xep):
              reverse = False
              break              
          else:
            sap_xep = input("Nhap lai: ")
        
          list = manager.sort_by_price_in(reverse)
          print(list)
      
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 6:

      # Danh sach hang hoa sap het han su dung
      # Co ham se them vao sau
      pass

    case 7:

      # Top 5 hang hoa co gia nhap cao nhat, thap nhat
      try:
        manager.show_top5_high_low_pricein()
      except Exception as e:
        print("------------------------------")
        print("Error:",e)
        print("------------------------------")

    case 8:

      # Hien thi danh sach hang can nhap 
      # Co ham se them sau 
      pass

    case 9:

      # Nhap hang 
      # Co ham se them sau 
      pass
    
    case 10:

      # Xoa hang hoa
      try:
        id = input("Nhap ma hang: ")
        manager.del_product(id)
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
