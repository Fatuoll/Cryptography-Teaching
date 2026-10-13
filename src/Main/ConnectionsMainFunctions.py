from src.RSA.RsaPractical import RsaLibrary

from src.Main.Dialogues.DialoguesPractical import MessageDialogue


class SluierMainFunctionsMixin:
    def encryption(self, alg):
        if alg == 'RSA':
            cip, signature = RsaLibrary.encrypt(mes=self.pte_prsaenc_mes.toPlainText(),
                                                enc=self.cmbx_prsaenc_inenc.currentText(),
                                                pbk=None,
                                                prk=None,
                                                pad=self.cmbx_prsaenc_pad.currentText(),
                                                hash_alg=self.cmbx_prsaenc_hash.currentText(),
                                                mgfhash_alg=self.cmbx_prsaenc_mgfhash.currentText(),
                                                sch=self.cmbx_prsaencs_sch.currentText(),
                                                hash_algs=self.cmbx_prsaencs_hash.currentText(),
                                                mgfhash_algs=self.cmbx_prsaencs_mgfhash.currentText(),
                                                salt=self.cmbx_prsaencs_sl.currentText(),
                                                sign=self.chbx_prsaenc_addsign.isChecked(),
                                                lbl=self.lne_prsaenc_lbl.text()
                                                )
            if not cip:
                MessageDialogue.show_critical(text=signature)
            else:
                self.pte_prsaenc_cip.setPlainText(cip)
                if signature:
                    self.pte_prsaenc_sign.setPlainText(signature)
        elif alg == 'AES':
            pass
        elif alg == 'BD':
            pass

    def decryption(self, alg):
        if alg == 'RSA':
            pass
        elif alg == 'AES':
            pass
        elif alg == 'BD':
            pass
        elif alg == 'ECC':
            pass

    def addkeysdepository(self, alg, eccexchange=False):
        if alg == 'RSA':
            pass
        elif alg == 'AES':
            pass
        elif alg == 'BD':
            pass
        elif alg == 'ECC':
            if not eccexchange:
                pass
            else:
                pass

    def generatekeys(self, alg):
        if alg == 'RSA':
            pass
        elif alg == 'BD':
            pass
        elif alg == 'ECC':
            pass

    def selectfile(self):
        pass