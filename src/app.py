import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Path to store the encryption key
KEY_FILE = "key.txt"
ENCRYPTED_FOLDER = "encrypted_files"

# Ensure the encrypted folder exists
if not os.path.exists(ENCRYPTED_FOLDER):
    os.makedirs(ENCRYPTED_FOLDER)

def generate_key():
    """Generate and save a key if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)

def load_key():
    """Load the encryption key from the file."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Please generate it first.")
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_file(file_path):
    """Encrypt a file and save it in the encrypted folder."""
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)
        encrypted_file_path = os.path.join(ENCRYPTED_FOLDER, os.path.basename(file_path) + ".enc")

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        messagebox.showinfo("Success", f"File encrypted and saved to {encrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encrypt file: {str(e)}")

def decrypt_file(file_path, key):
    """Decrypt a file and save it."""
    try:
        fernet = Fernet(key)

        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = fernet.decrypt(encrypted)
        decrypted_file_path = filedialog.asksaveasfilename(title="Save Decrypted File")

        if decrypted_file_path:
            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)

            messagebox.showinfo("Success", f"File decrypted and saved to {decrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decrypt file: {str(e)}")

def upload_file():
    """Handle file upload and encryption."""
    file_path = filedialog.askopenfilename(title="Select a File to Encrypt")
    if file_path:
        encrypt_file(file_path)

def decrypt_prompt():
    """Prompt user to select a file and enter the key for decryption."""
    file_path = filedialog.askopenfilename(title="Select an Encrypted File")
    if file_path:
        key = tk.simpledialog.askstring("Enter Key", "Enter the encryption key:", show='*')
        if key:
            decrypt_file(file_path, key.encode())

# GUI Setup
root = tk.Tk()
root.title("Secure AppLock")
root.geometry("400x200")

# Generate key if not exists
generate_key()

# Buttons
upload_button = tk.Button(root, text="Upload and Encrypt File", command=upload_file, width=30)
upload_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_prompt, width=30)
decrypt_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=30)
exit_button.pack(pady=10)

root.mainloop()
