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

def add_new_product():
  name = input("Ten:")
  price_out = input("Gia ban: ")
  price_in = input("Gia nhap: ")
  nbr_product = input("Ton kho: ")
  exp = datetime.now()
  mfg = datetime.now()

  p = product.Product(name,price_out,price_in,nbr_product,exp,mfg)
  manager.add_product()

while True:
  display_menu()
  choice = input("Lua chon: ")
  match choice:
    case "1":
      # Them hang hoa
      try: 
        add_new_product()
      except Exception:
        print("An error occurred! ")
    case "2":
      # Danh sach hang hoa
      try: 
        manager.get_products()
      except Exception:
        print("An error occurred! ")
    case "3":
      # Tim kiem hang hoa theo ten
      try:
        name = input("Nhap ten: ")
        manager.search_by_name(name)
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
        manager.sort_by_price_in()
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
