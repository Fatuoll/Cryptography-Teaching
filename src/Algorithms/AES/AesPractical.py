from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from os import urandom

from src.Algorithms.Help.HelpPractical import LibrariesHelp


class AesLibrary:
    @staticmethod
    def encrypt(key="", ktype="", mes="", aad="", enc="", dec="", isaad=False):
        # TODO


        aes = AESGCM(LibrariesHelp.to_bytes(key, enc))
        nonce = urandom(12)

        if isaad:
            cip = aes.encrypt(nonce, LibrariesHelp.to_bytes(mes, enc), LibrariesHelp.to_bytes(aad, enc))
        else:
            cip = aes.encrypt(nonce, LibrariesHelp.to_bytes(mes, enc), None)

        rs = LibrariesHelp.RS
        add = f'{rs}{enc}{rs}{dec}{rs}{nonce}{rs}{aad}{rs}{str(isaad)}{rs}'
        add = f'{len(add)}{rs}' + add
        cip = LibrariesHelp.from_bytes(cip, dec)
        cip = add + cip

        return cip

    @staticmethod
    def decrypt(key="", cip=""):
        rs = LibrariesHelp.RS
        enc, dec, nonce, aad, isaad, cip = cip.split(rs)
        if len(cip.split(rs)[1:-1]) != int(cip.split(rs)[0]):
            return None, 'System parameters were edited.'
        isaad = True if isaad == 'True' else False

        AesLibraryHelp.validate(mes=cip, enc=enc, dec=dec, aad=aad, isaad=isaad)

        aes = AESGCM(LibrariesHelp.to_bytes(key, dec))

        try:
            if isaad:
                mes = aes.decrypt(LibrariesHelp.to_bytes(nonce, dec), LibrariesHelp.to_bytes(cip, dec),
                                  LibrariesHelp.to_bytes(aad, dec))
            else:
                mes = aes.decrypt(LibrariesHelp.to_bytes(nonce, dec), LibrariesHelp.to_bytes(cip, dec), None)
        except InvalidTag:
            return "The message is corrupted or modified.", False

        LibrariesHelp.from_bytes(mes, enc)
        return mes, True


class AesLibraryHelp:
    @staticmethod
    def validate(mes="", enc="", dec="", aad="", isaad=False):
        if not mes:
            return False, "The message is empty."
        if isaad and not aad:
            return False, "The AAD is empty."
        if enc not in ('UTF-8', 'UTF-16', 'ASCII', 'Base64', 'Hex'):
            return False, "The Input Encoding is invalid."
        if dec not in ('Base64', 'Hex'):
            return False, "The Output Encoding is invalid."
        return True, None

    @staticmethod
    def prepare(key, ktype, enc=''):
        if ktype == 'key':
            return LibrariesHelp.to_bytes(key, enc)
        elif ktype == 'generate':
            pass
        elif ktype == 'password':
            pass
        elif ktype == 'enter':
            pass
        elif ktype == 'ecc':
            pass