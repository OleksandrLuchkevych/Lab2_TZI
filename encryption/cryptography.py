def encrypt(key: str, plain: str, alpha: str) -> str:
    alpha_len = len(alpha)
    
    fit_key = (key * (len(plain) // len(key))) + key[:len(plain) % len(key)]
    
    fit_key_indexes = [alpha.index(ch) + 1 for ch in fit_key]
    plain_indexes = [alpha.index(ch) + 1 for ch in plain]
    
    cipher_indexes = [
        (fit_key_indexes[i] + plain_indexes[i]) % alpha_len
        for i in range(len(plain))]
    
    cipher_text = ''.join([alpha[(cipher_indexes[i] - 1)] for i in range(len(plain))])

    return cipher_text
