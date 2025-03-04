import os
import time
import pydicom
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Función para cifrar con AES-256-GCM
def encrypt_aes_gcm(data, key):
    iv = get_random_bytes(12)  # Nonce de 12 bytes
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext, iv, tag

# Función para descifrar con AES-256-GCM
def decrypt_aes_gcm(ciphertext, key, iv, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

# Cargar archivos DICOM desde la misma carpeta del script (introduce los archivos manualmente)
dicom_files = [
]

# Generar clave para AES-256-GCM (256 bits / 32 bytes)
key = get_random_bytes(32)

def main():
    for filename in dicom_files:
        if os.path.exists(filename):
            dicom_data = pydicom.dcmread(filename).PixelData
            print(f"Procesando: {filename}")
            
            # Cifrar
            ciphertext, iv, tag = encrypt_aes_gcm(dicom_data, key)
            print("Cifrado completado.")
            
            # Descifrar
            decrypted_data = decrypt_aes_gcm(ciphertext, key, iv, tag)
            print("Descifrado completado.")
            
            # Verificar integridad
            if dicom_data == decrypted_data:
                print("Integridad verificada: Los datos coinciden.\n")
            else:
                print("Error: Los datos descifrados no coinciden.\n")
        else:
            print(f"Warning: {filename} no existe.")

if __name__ == "__main__":
    main()
