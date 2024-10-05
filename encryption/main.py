from cryptography import encrypt

def main():

    alpha = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_0123456789'
    key = 'ВЕРБАН'
    plain_text = 'ОРРААВПМА_300_Т'

    cipher_text = encrypt(key, plain_text, alpha)

    print("Key:", key)
    print("Plain text:", plain_text)
    print("Cipher text:", cipher_text)

main()
