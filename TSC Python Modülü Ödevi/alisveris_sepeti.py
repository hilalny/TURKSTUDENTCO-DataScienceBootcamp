import os

class Market:
    def __init__(self, file_name="product.txt"):
        self.file_name = file_name
        # Dosyanın mevcut olup olmadığını kontrol edin, yoksa oluşturun
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                pass

    def __del__(self):
        # Program sonlandığında dosyayı kapatma işlemi
        print("Program sonlanıyor. Dosya kapatıldı.")

    def list_products(self):
        print("\n--- Ürün Listesi ---")
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("Ürün bulunamadı.")
                    return
                for i, line in enumerate(lines, start=1):
                    product_info = line.strip().split(",")
                    print(f"{i}) Ürün Adı: {product_info[0]}, Kategori: {product_info[1]}, Fiyat: {product_info[2]}, Stok: {product_info[3]}")
        except FileNotFoundError:
            print("Dosya bulunamadı.")

    def add_product(self):
        print("\n--- Ürün Ekle ---")
        name = input("Ürün Adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok Miktarı: ")
        new_product = f"{name},{category},{price},{stock}\n"
        try:
            with open(self.file_name, 'a') as file:
                file.write(new_product)
                print("Ürün başarıyla eklendi!")
        except Exception as e:
            print(f"Ürün eklenirken bir hata oluştu: {e}")

    def delete_product(self):
        print("\n--- Ürün Sil ---")
        self.list_products()
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
            if not lines:
                print("Silinecek ürün bulunamadı.")
                return

            product_number = int(input("Silmek istediğiniz ürün numarasını girin: "))
            if 1 <= product_number <= len(lines):
                del lines[product_number - 1]
                with open(self.file_name, 'w') as file:
                    file.writelines(lines)
                print("Ürün başarıyla silindi!")
            else:
                print("Geçersiz ürün numarası.")
        except ValueError:
            print("Lütfen geçerli bir numara girin.")
        except Exception as e:
            print(f"Ürün silinirken bir hata oluştu: {e}")


def main():
    market = Market()

    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        choice = input("Seçiminizi yapın (1-4): ")

        if choice == "1":
            market.list_products()
        elif choice == "2":
            market.add_product()
        elif choice == "3":
            market.delete_product()
        elif choice == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir seçim yapın.")

if __name__ == "__main__":
    main()
