from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, PKCS1v15, MGF1, PSS
from cryptography.hazmat.primitives.hashes import SHA256, SHA384, SHA512
from cryptography.hazmat.primitives.serialization import (load_pem_private_key, load_pem_public_key, Encoding,
                                                          PrivateFormat, PublicFormat, NoEncryption)

from src.Algorithms.Help.HelpPractical import LibrariesHelp


class RsaLibrary:
    @staticmethod
    def encrypt(mes="", enc="", dec="", pbk="", prk="", pad="", hash_alg="", mgfhash_alg="",
                sch="", hash_algs="", mgfhash_algs="", salt="", sign=False, lbl=None, password=None):
        validator = RsaLibraryHelp.validate(text=mes, enc=enc, dec=dec, key=pbk, sign_key=prk, pad=pad,
                                            hash_alg=hash_alg, mgfhash_alg=mgfhash_alg, sch=sch, hash_algs=hash_algs,
                                            mgfhash_algs=mgfhash_algs, salt=salt, sign=sign, mode='encrypt')
        if not validator[0]:
            return None, validator[1]

        public = load_pem_public_key(LibrariesHelp.to_bytes(pbk, enc))

        if pad == "OAEP":
            cip = public.encrypt(
                LibrariesHelp.to_bytes(mes, enc),
                OAEP(
                    mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_alg)),
                    algorithm=RsaLibraryHelp.choose_hash(hash_alg),
                    label=LibrariesHelp.to_bytes(lbl, enc)
                )
            )
        elif pad == "PKCS1v15":
            cip = public.encrypt(
                LibrariesHelp.to_bytes(mes, enc),
                PKCS1v15()
            )

        signature = None

        if sign:
            private = load_pem_private_key(LibrariesHelp.to_bytes(prk, enc), password=password)
            if sch == "RSA-PSS":
                signature = private.sign(
                    LibrariesHelp.to_bytes(mes, enc),
                    PSS(
                        mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_algs)),
                        salt_length=RsaLibraryHelp.choose_salt(salt)
                    ),
                    RsaLibraryHelp.choose_hash(hash_algs)
                )
            elif sch == "PKCS1v15":
                signature = private.sign(
                    LibrariesHelp.to_bytes(mes, enc),
                    PKCS1v15(),
                    RsaLibraryHelp.choose_hash(hash_algs)
                )

        rs = LibrariesHelp.RS
        add = (f'{enc}{rs}{dec}{rs}{pad}{rs}{hash_alg}{rs}{mgfhash_alg}{rs}{sch}{rs}{hash_algs}{rs}'
               f'{mgfhash_algs}{rs}{salt}{rs}')
        add = f'{len(add)}{rs}' + add

        cip = LibrariesHelp.from_bytes(cip, dec)
        cip = add + cip

        if signature:
            signature = LibrariesHelp.from_bytes(signature, dec)
        return cip, signature

    @staticmethod
    def decrypt(cip="", signature="", prk="", pbk="", sign=False, lbl=None, password=None):
        rs = LibrariesHelp.RS
        if len(cip.split(rs)[1:-1]) != int(cip.split(rs)[0]):
            return None, 'System parameters were edited.'
        enc, dec, pad, hash_alg, mgfhash_alg, sch, hash_algs, mgfhash_algs, salt, cip = cip.split(rs)

        validator = RsaLibraryHelp.validate(text=cip, enc=enc, dec=dec, key=pbk, sign_key=prk, pad=pad, hash_alg=hash_alg,
                                            mgfhash_alg=mgfhash_alg, sch=sch, hash_algs=hash_algs,
                                            mgfhash_algs=mgfhash_algs, salt=salt, sign=sign, mode='decrypt')
        if not validator[0]:
            return None, validator[1]

        private = load_pem_private_key(LibrariesHelp.to_bytes(prk, dec), password=password)

        if pad == "OAEP":
            mes = private.decrypt(
                LibrariesHelp.to_bytes(cip, dec),
                OAEP(
                    mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_alg)),
                    algorithm=RsaLibraryHelp.choose_hash(hash_alg),
                    label=LibrariesHelp.to_bytes(lbl, dec)
                )
            )
        elif pad == "PKCS1v15":
            mes = private.decrypt(
                LibrariesHelp.to_bytes(cip, dec),
                PKCS1v15()
            )

        sign_verify = None
        if sign:
            public = load_pem_public_key(LibrariesHelp.to_bytes(pbk, dec))
            try:
                if sch == 'RSA-PSS':
                    public.verify(
                        LibrariesHelp.to_bytes(signature, dec),
                        mes,
                        PSS(
                            mgf=MGF1(algorithm=RsaLibraryHelp.choose_hash(mgfhash_algs)),
                            salt_length=RsaLibraryHelp.choose_salt(salt),
                        ),
                        RsaLibraryHelp.choose_hash(hash_algs)
                    )
                elif sch == 'PKCS1v15':
                    public.verify(
                        LibrariesHelp.to_bytes(signature, dec),
                        mes,
                        PKCS1v15(),
                        RsaLibraryHelp.choose_hash(hash_algs)
                    )
                sign_verify = True
            except InvalidSignature:
                return "The message or the signature has been edited.", False

        mes = LibrariesHelp.from_bytes(mes, enc)
        return mes, sign_verify

    @staticmethod
    def generate(size):
        private_key = generate_private_key(
            public_exponent=65537,
            key_size=size
        )
        public_key = private_key.public_key()
        private_key = private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption()
        )
        public_key = public_key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo,
        )
        return private_key, public_key


class RsaLibraryHelp:
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
    def validate(text="", enc="", dec="", key="", sign_key="", pad="", hash_alg="", mgfhash_alg="",
                sch="", hash_algs="", mgfhash_algs="", salt="", sign=False, mode=''):
        if not text:
            return False, 'The Message is empty.'
        if enc not in ('UTF-8', 'UTF-16', 'ASCII', 'Base64', 'Hex'):
            return False, 'The Input Encoding is invalid.'
        if dec not in ('Base64', 'Hex'):
            return False, 'The Output Encoding is invalid.'
        if not key:
            if mode == 'encrypt':
                return False, 'The Public Key is empty.'
            elif mode == 'decrypt':
                return False, 'The Private Key is empty.'
        if pad not in ('OAEP', 'PKCS1v15'):
            return False, 'The Padding Type is invalid.'
        if hash_alg not in ('SHA-256', 'SHA-384', 'SHA-512'):
            return False, 'The Hash Algorithm is invalid.'
        if mgfhash_alg not in ('SHA-256', 'SHA-384', 'SHA-512'):
            return False, 'The MgfHash Algorithm is invalid.'
        if sign:
            if not sign_key:
                if mode == 'encrypt':
                    return False, 'The Private Key is empty.'
                elif mode == 'decrypt':
                    return False, 'The Public Key is empty.'
            if sch not in ('RSA-PSS', 'PKCS1v15'):
                return False, 'The Signature Padding Type is invalid.'
            if hash_algs not in ('SHA-256', 'SHA-384', 'SHA-512'):
                return False, 'The Signature Hash Algorithm is invalid.'
            if mgfhash_algs not in ('SHA-256', 'SHA-384', 'SHA-512'):
                return False, 'The Signature MgfHash Algorithm is invalid.'
            if salt not in ('Maximum', 'Digest length'):
                return False, 'The Salt Length is invalid.'

        return True, None