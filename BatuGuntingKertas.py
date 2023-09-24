import random

def main():
    print("Selamat datang di Permainan Batu Gunting Batu Kertas!")
    
    while True:
        user_choice = input("Pilih batu, gunting, atau kertas (keluar untuk mengakhiri): ").lower()
        if user_choice == "keluar":
            break

        if user_choice not in ["batu", "gunting", "kertas"]:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            continue

        computer_choice = random.choice(["batu", "gunting", "kertas"])

        print(f"Anda memilih: {user_choice}")
        print(f"Komputer memilih: {computer_choice}")

        if user_choice == computer_choice:
            print("Hasilnya seri!")
        elif (
            (user_choice == "batu" and computer_choice == "gunting") or
            (user_choice == "gunting" and computer_choice == "kertas") or
            (user_choice == "kertas" and computer_choice == "batu")
        ):
            print("Anda menang!")
        else:
            print("Komputer menang!")

if __name__ == "__main__":
    main()
