# Todo List Application

def display_tasks(tasks):
    """Menampilkan daftar tugas."""
    if len(tasks) == 0:
        print("Tidak ada tugas.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Menambahkan tugas baru."""
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print(f"Tugas '{task}' berhasil ditambahkan.")

def remove_task(tasks):
    """Menghapus tugas berdasarkan nomor yang dipilih."""
    try:
        task_number = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Tugas '{removed_task}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def main():
    """Fungsi utama untuk menjalankan aplikasi To-Do List."""
    tasks = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Tampilkan Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid, coba lagi.")
if __name__ == "__main__":
    main()