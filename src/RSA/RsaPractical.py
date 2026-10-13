from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, PKCS1v15, MGF1, PSS
from cryptography.hazmat.primitives.hashes import SHA256, SHA384, SHA512
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

from base64 import b64decode, b64encode


class RsaLibrary:
    @staticmethod
    def encrypt(mes="", enc="", pbk="", prk="", pad="", hash_alg="", mgfhash_alg="",
                sch="", hash_algs="", mgfhash_algs="", salt="", sign=False, lbl=None, password=None):
        validator = RsaLibraryHelp.validate(text=mes, enc=enc, key=pbk, sign_key=prk, pad=pad, hash_alg=hash_alg,
                                            mgfhash_alg=mgfhash_alg, sch=sch, hash_algs=hash_algs,
                                            mgfhash_algs=mgfhash_algs, salt=salt, sign=sign, mode='encrypt')
        if not validator[0]:
            return None, validator[1]

        public = load_pem_public_key(RsaLibraryHelp.to_bytes(pbk, enc))

        if pad == "OAEP":
            cip = public.encrypt(
                RsaLibraryHelp.to_bytes(mes, enc),
                OAEP(
                    mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_alg)),
                    algorithm=RsaLibraryHelp.choose_hash(hash_alg),
                    label=lbl
                )
            )
        elif pad == "PKCS1v15":
            cip = public.encrypt(
                RsaLibraryHelp.to_bytes(mes, enc),
                PKCS1v15()
            )

        signature = None

        if sign:
            private = load_pem_private_key(RsaLibraryHelp.to_bytes(prk, enc), password=password)
            if sch == "RSA-PSS":
                signature = private.sign(
                    RsaLibraryHelp.to_bytes(mes, enc),
                    PSS(
                        mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_algs)),
                        salt_length=RsaLibraryHelp.choose_salt(salt)
                    ),
                    RsaLibraryHelp.choose_hash(hash_algs)
                )
            elif sch == "PKCS1v15":
                signature = private.sign(
                    RsaLibraryHelp.to_bytes(mes, enc),
                    PKCS1v15(),
                    RsaLibraryHelp.choose_hash(hash_algs)
                )

        cip = RsaLibraryHelp.from_bytes(cip, enc)
        if signature:
            signature = RsaLibraryHelp.from_bytes(signature, enc)
        return cip, signature

    @staticmethod
    def decrypt(cip="", signature="", enc="", prk="", pbk="", pad="", hash_alg="", mgfhash_alg="",
                sch="", hash_algs="", mgfhash_algs="", salt="", sign=False, lbl=None, password=None):
        validator = RsaLibraryHelp.validate(text=cip, enc=enc, key=pbk, sign_key=prk, pad=pad, hash_alg=hash_alg,
                                            mgfhash_alg=mgfhash_alg, sch=sch, hash_algs=hash_algs,
                                            mgfhash_algs=mgfhash_algs, salt=salt, sign=sign, mode='decrypt')
        if not validator[0]:
            return None, validator[1]

        private = load_pem_private_key(RsaLibraryHelp.to_bytes(prk, enc), password=password)

        if pad == "OAEP":
            mes = private.decrypt(
                RsaLibraryHelp.to_bytes(cip, enc),
                OAEP(
                    mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_alg)),
                    algorithm=RsaLibraryHelp.choose_hash(hash_alg),
                    label=lbl
                )
            )
        elif pad == "PKCS1v15":
            mes = private.decrypt(
                RsaLibraryHelp.to_bytes(cip, enc),
                PKCS1v15()
            )

        if sign:
            public = load_pem_public_key(RsaLibraryHelp.to_bytes(pbk, enc))
            try:
                if sch == 'RSA-PSS':
                    public.verify(
                        RsaLibraryHelp.to_bytes(signature, enc),
                        mes,
                        PSS(
                            mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_algs)),
                            salt_length=RsaLibraryHelp.choose_salt(salt),
                        ),
                        RsaLibraryHelp.choose_hash(hash_algs)
                    )
                elif sch == 'PKCS1v15':
                    public.verify(
                        RsaLibraryHelp.to_bytes(signature, enc),
                        mes,
                        PKCS1v15(),
                        RsaLibraryHelp.choose_hash(hash_algs)
                    )
            except InvalidSignature:
                return "The message or the signature has been edited!", False

        mes = RsaLibraryHelp.from_bytes(mes, enc)
        return mes, True

    @staticmethod
    def generate(size):
        private_key = generate_private_key(
            public_exponent=65537,
            key_size=size
        )
        public_key = private_key.public_key()
        return private_key, public_key


class RsaLibraryHelp:
    @staticmethod
    def to_bytes(text, enc):
        if enc == 'utf-8':
            return text.encode('utf-8')
        elif enc == 'utf-16':
            return text.encode('utf-16')
        elif enc == 'ASCII':
            return text.encode('ascii')
        elif enc == 'base64':
            return b64decode(text)
        elif enc == 'hex':
            return bytes.fromhex(text)

    @staticmethod
    def from_bytes(data, enc):
        if enc == 'utf-8':
            return data.decode('utf-8')
        elif enc == 'utf-16':
            return data.decode('utf-16')
        elif enc == 'ASCII':
            return data.decode('ascii')
        elif enc == 'base64':
            return b64encode(data).decode('ascii')
        elif enc == 'hex':
            return data.hex()

    @staticmethod
    def choose_hash(hash_algorithm):
        if hash_algorithm == 'SHA-256':
            return SHA256()
        elif hash_algorithm == 'SHA-384':
            return SHA384()
        elif hash_algorithm == 'SHA-512':
            return SHA512()

    @staticmethod
    def choose_salt(salt_length):
        if salt_length == 'Maximum':
            return PSS.MAX_LENGTH
        elif salt_length == 'Digest length':
            return PSS.DIGEST_LENGTH

    @staticmethod
    def validate(text="", enc="", key="", sign_key="", pad="", hash_alg="", mgfhash_alg="",
                sch="", hash_algs="", mgfhash_algs="", salt="", sign=False, mode=''):
        if not text:
            return [False, 'The Message is empty!']
        if enc not in ['utf-8', 'utf-16', 'ASCII', 'base64', 'hex']:
            return [False, 'The Encryption Type is invalid!']
        if not key:
            if mode == 'encrypt':
                return [False, 'The Public Key is empty!']
            elif mode == 'decrypt':
                return [False, 'The Private Key is empty!']
        if pad not in ['OAEP', 'PKCS1v15']:
            return [False, 'The Padding Type is invalid!']
        if hash_alg not in ['SHA256', 'SHA384', 'SHA512']:
            return [False, 'The Hash Algorithm is invalid!']
        if mgfhash_alg not in ['SHA256', 'SHA384', 'SHA512']:
            return [False, 'The MgfHash Algorithm is invalid!']
        if sign:
            if not sign_key:
                if mode == 'encrypt':
                    return [False, 'The Private Key is empty!']
                elif mode == 'decrypt':
                    return [False, 'The Public Key is empty!']
            if sch not in ['RSA-PSS', 'PKCS1v15']:
                return [False, 'The Signature Padding Type is invalid!']
            if hash_algs not in ['SHA256', 'SHA384', 'SHA512']:
                return [False, 'The Signature Hash Algorithm is invalid!']
            if mgfhash_algs not in ['SHA256', 'SHA384', 'SHA512']:
                return [False, 'The Signature MgfHash Algorithm is invalid!']
            if salt not in ['Maximum', 'Digest length']:
                return [False, 'The Salt Length is invalid!']

        return [True, None]