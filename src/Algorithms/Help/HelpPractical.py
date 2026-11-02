from base64 import b64decode, b64encode


class LibrariesHelp:
    RS = '\x1e'

    @staticmethod
    def to_bytes(text, enc):
        if text.startswith(('b"', "b'")):
            return text[2:-1].replace('\\n', '\n').encode('utf-8')
        elif enc == 'UTF-8':
            return text.encode('utf-8')
        elif enc == 'UTF-16':
            return text.encode('utf-16')
        elif enc == 'ASCII':
            return text.encode('ascii')
        elif enc == 'Base64':
            return b64decode(text)
        elif enc == 'Hex':
            return bytes.fromhex(text)

    @staticmethod
    def from_bytes(data, enc):
        if enc == 'UTF-8':
            return data.decode('utf-8')
        elif enc == 'UTF-16':
            return data.decode('utf-16')
        elif enc == 'ASCII':
            return data.decode('ascii')
        elif enc == 'Base64':
            return b64encode(data).decode('ascii')
        elif enc == 'Hex':
            return data.hex()