import hashlib

def criptografia(senha):
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes)
    return senha_hash.hexdigest()
