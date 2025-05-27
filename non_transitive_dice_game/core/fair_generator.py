import secrets
import hmac
import hashlib

class FairRandomGenerator:
    def __init__(self, size):
        self.size = size
        self.secret_key = secrets.token_bytes(32)
        self.number = self.secure_random_int(size)

    def secure_random_int(self, n):
        return secrets.randbelow(n)

    def commit(self):
        msg = str(self.number).encode()
        digest = hmac.new(self.secret_key, msg, hashlib.sha3_256).hexdigest()
        return self.number, digest

    def reveal(self, user_input):
        result = (self.number + user_input) % self.size
        print(f"My number is {self.number} (KEY={self.secret_key.hex()}).")
        print(f"The fair number generation result is {self.number} + {user_input} = {result} (mod {self.size})")
        return {"value": result}