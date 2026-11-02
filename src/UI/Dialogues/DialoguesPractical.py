from PyQt6.QtWidgets import QMessageBox


class MessageDialogue:
    @staticmethod
    def show_warning(text=''):
        QMessageBox.warning(None, 'Warning', text)

    @staticmethod
    def show_critical(text=''):
        QMessageBox.critical(None, 'Important', text)