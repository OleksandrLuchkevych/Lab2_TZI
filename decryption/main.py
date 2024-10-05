from cryptography import decrypt

def main():
    alpha = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_0123456789'
    key = "ДМИТРО"
    cipher_text = "ЖРБУУЄ_СГЖОЧ2ВФА1"

    decrypted_message = decrypt(key, cipher_text, alpha)

    print("Key:", key)
    print("Cipher text:", cipher_text)
    print("Decrypted message:", decrypted_message)

main()
