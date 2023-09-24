import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    
    angka_rahasia = random.randint(1, 100)
    kesempatan = 0
    
    while True:
        try:
            tebakan = int(input("Tebak angka (1-100): "))
            kesempatan += 1
            
            if tebakan < 1 or tebakan > 100:
                print("Masukkan angka antara 1 dan 100.")
                continue
            
            if tebakan < angka_rahasia:
                print("Angka terlalu kecil. Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Angka terlalu besar. Coba lagi.")
            else:
                print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {kesempatan} kesempatan.")
                break
        
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
