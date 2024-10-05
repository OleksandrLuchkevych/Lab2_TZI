def decrypt(key: str, cipher: str, alpha: str) -> str:
    alpha_len = len(alpha)
    
    fit_key = key * (len(cipher) // len(key)) + key[:len(cipher) % len(key)]
    
    fit_key_indexes = [alpha.index(ch) + 1 for ch in fit_key]
    cipher_indexes = [alpha.index(ch) + 1 for ch in cipher]
    
    plain_indexes = [
        (cipher_indexes[i] - fit_key_indexes[i]) % alpha_len
        for i in range(len(cipher))]
    
    plain_text = ''.join([alpha[(plain_indexes[i] - 1)] for i in range(len(cipher))])

    return plain_text