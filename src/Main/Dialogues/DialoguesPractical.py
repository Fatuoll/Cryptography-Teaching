from PyQt6.QtWidgets import QMessageBox


class MessageDialogue:
    @staticmethod
    def show_critical(text=''):
        QMessageBox.warning(None, 'Warning', text)