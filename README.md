# applock
A Python File Encryption System Used to encrypt

# Secure AppLock

Welcome to **Secure AppLock**, a simple and secure application to encrypt and decrypt your files. This guide will help you understand how to use the application on both Windows and Linux systems.

---

## What Does Secure AppLock Do?
- **Encrypt Files**: Protect your files by encrypting them. Encrypted files are stored securely and can only be accessed with a unique key.
- **Decrypt Files**: Access your encrypted files by entering the correct key.
- **Key Management**: A unique key is generated once and saved securely. This key is required to decrypt your files.

---

## Getting Started

### Prerequisites
1. **Python**: Make sure Python is installed on your system.
   - On Windows, download Python from [python.org](https://www.python.org/downloads/).
   - On Linux, install Python using your package manager (e.g., `sudo apt-get install python3`).
2. **Install Required Libraries**:
   - Open a terminal or command prompt and run:
     ```
     pip install -r requirements.txt
     ```

---

## How to Use Secure AppLock

### Step 1: Launch the Application
- **Windows**: Double-click the `app.py` file or run the following command in the terminal:
  ```
  python src/app.py
  ```
- **Linux**: Open a terminal, navigate to the project folder, and run:
  ```
  python3 src/app.py
  ```

### Step 2: Encrypt a File
1. Click the **"Upload and Encrypt File"** button.
2. Select the file you want to encrypt.
3. The file will be encrypted and saved in the `encrypted_files` folder.
4. A success message will show the location of the encrypted file.

### Step 3: Decrypt a File
1. Click the **"Decrypt File"** button.
2. Select the encrypted file (with `.enc` extension).
3. Enter the encryption key when prompted.
4. Choose where to save the decrypted file.
5. A success message will confirm the file has been decrypted.

---

## Key Management
- The encryption key is generated automatically the first time you run the application.
- The key is saved in a file named `key.txt` in the application folder.
- **Do not delete or lose this file!** Without the key, you cannot decrypt your files.

---

## Creating an Executable (Optional)
If you want to create a standalone `.exe` file for Windows:
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Run the following command:
   ```
   pyinstaller --onefile --windowed src/app.py
   ```
3. The `.exe` file will be in the `dist` folder.

For Linux, you can use the same steps, but the output will be a Linux executable.

---

## Troubleshooting
- **Missing Key File**: If `key.txt` is missing, delete the `encrypted_files` folder and restart the application to generate a new key. Note that previously encrypted files cannot be decrypted without the original key.
- **Dependencies Not Installed**: Ensure you have installed the required libraries using `pip install -r requirements.txt`.
- **Permission Issues**: On Linux, ensure you have the necessary permissions to read/write files in the application folder.

---

## Support
If you encounter any issues, feel free to reach out to the developer team at **Dolphin-Co-Solution**.

Enjoy using Secure AppLock to keep your files safe!
