from PyQt6.QtWidgets import QMainWindow

from src.Visual.Art import Ui_MainWindow


class Sluier(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._setup()
        self.connection()

    def _setup(self):
        self.ersa_buttons = {
            0: [self.rbtn_ersah1, self.chbx_ersal1],
            1: [self.rbtn_ersah2, self.chbx_ersal2],
            2: [self.rbtn_ersah3, self.chbx_ersal3],
            3: [self.rbtn_ersah4, self.chbx_ersal4],
            4: [self.rbtn_ersah5, self.chbx_ersal5],
            5: [self.rbtn_ersah6, self.chbx_ersal6],
            6: [self.rbtn_ersah7, self.chbx_ersal7],
            7: [self.rbtn_ersah8, self.chbx_ersal8],
            8: [self.rbtn_ersah9, self.chbx_ersal9]
        }
        self.eaes_buttons = {
            0: [self.rbtn_eaesh1, self.chbx_eaesl1],
            1: [self.rbtn_eaesh2, self.chbx_eaesl2],
            2: [self.rbtn_eaesh3, self.chbx_eaesl3],
            3: [self.rbtn_eaesh4, self.chbx_eaesl4],
            4: [self.rbtn_eaesh5, self.chbx_eaesl5],
            5: [self.rbtn_eaesh6, self.chbx_eaesl6],
            6: [self.rbtn_eaesh7, self.chbx_eaesl7],
            7: [self.rbtn_eaesh8, self.chbx_eaesl8],
            8: [self.rbtn_eaesh9, self.chbx_eaesl9],
            9: [self.rbtn_eaesh10, self.chbx_eaesl10]
        }
        self.eecc_buttons = {
            0: [self.rbtn_eecch1, self.chbx_eeccl1],
            1: [self.rbtn_eecch2, self.chbx_eeccl2],
            2: [self.rbtn_eecch3, self.chbx_eeccl3],
            3: [self.rbtn_eecch4, self.chbx_eeccl4],
            4: [self.rbtn_eecch5, self.chbx_eeccl5]
        }
        self.eecdh_buttons = {
            0: [self.rbtn_eecdhh1, self.chbx_eecdhl1],
            1: [self.rbtn_eecdhh2, self.chbx_eecdhl1],
            2: [self.rbtn_eecdhh3, self.chbx_eecdhl1],
            3: [self.rbtn_eecdhh4, self.chbx_eecdhl1]
        }

    def connection(self):
        # Main tab
        self.btn_mn_pr.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_pr))
        self.btn_mn_edu.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_edu))
        self.btn_mn_st.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_set))
        self.btn_mn_ab.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_about))
        self.btn_mn_hp.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_help))

        # Practical tab
        self.btn_pr_back.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_mn))
        self.btn_pr_rsa.clicked.connect(lambda: self.tw_pr.setCurrentWidget(self.tab_prsa))
        self.btn_pr_aes.clicked.connect(lambda: self.tw_pr.setCurrentWidget(self.tab_paes))
        self.btn_pr_bd.clicked.connect(lambda: self.tw_pr.setCurrentWidget(self.tab_pbd))
        self.btn_pr_ecc.clicked.connect(lambda: self.tw_pr.setCurrentWidget(self.tab_pecc))
        self.btn_pr_set.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_set))
        self.btn_pr_hp.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_help))

        self.cmbx_prsa_opr.currentIndexChanged.connect(lambda: self.operation(self.stw_prsa))
        self.cmbx_paes_opr.currentIndexChanged.connect(lambda: self.operation(self.stw_paes))
        self.cmbx_pbd_opr.currentIndexChanged.connect(lambda: self.operation(self.stw_pbd))
        # RSA
        # Encryption
        self.btn_prsaenc_genk.clicked.connect(lambda: self.generatekeys('RSA'))
        self.btn_prsaenc_rec.clicked.connect(lambda: self.prmodes('RSA', 'Recommended'))
        self.btn_prsaenc_adv.clicked.connect(lambda: self.prmodes('RSA', 'Advanced'))

        self.cmbx_prsaenc_pad.currentIndexChanged.connect(lambda: self.hidesettings(self.cmbx_prsaenc_pad, 'RSA', False))
        self.cmbx_prsaencs_sch.currentIndexChanged.connect(lambda: self.hidesettings(self.cmbx_prsaencs_sch, 'RSA', True))

        self.cmbx_prsaenc_pbk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_prsaenc_pbk, self.cmbx_prsaenc_pbk,
                                                                                 'RSA', 'enc'))
        self.cmbx_prsaenc_prk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_prsaenc_prk, self.cmbx_prsaenc_prk,
                                                                                 'RSA', 'enc', signature=True))

        self.btn_prsaenc_enc.clicked.connect(lambda: self.encryption('RSA'))
        self.btn_prsaenc_addkdep.clicked.connect(lambda: self.addkeysdepository('RSA'))
        # Decryption
        self.cmbx_prsadec_prk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_prsadec_prk, self.cmbx_prsadec_prk,
                                                                                 'RSA', 'dec'))
        self.cmbx_prsadec_pbk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_prsadec_pbk, self.cmbx_prsadec_pbk,
                                                                                 'RSA', 'dec', signature=True))

        self.btn_prsadec_dec.clicked.connect(lambda: self.decryption('RSA'))
        self.btn_prsadec_addkdep.clicked.connect(lambda: self.addkeysdepository('RSA'))

        self.lbl_prsadec_signval.setEnabled(False)
        # AES
        # Encryption
        self.cmbx_paesenc_k.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_paesenc_k, self.cmbx_paesenc_k,
                                                                               'AES', 'enc'))
        self.btn_paesenc_enc.clicked.connect(lambda: self.encryption('AES'))
        self.btn_paesenc_addkdep.clicked.connect(lambda: self.addkeysdepository('AES'))

        self.stw_paesenc_k.setEnabled(False)
        # Decryption
        self.cmbx_paesdec_k.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_paesdec_k, self.cmbx_paesdec_k,
                                                                               'AES', 'dec'))
        self.btn_paesdec_dec.clicked.connect(lambda: self.decryption('AES'))
        self.btn_paesdec_addkdep.clicked.connect(lambda: self.addkeysdepository('AES'))
        self.lbl_paesdec_tagver.setEnabled(False)
        # BigData
        # Encryption
        self.btn_pbdenc_genk.clicked.connect(lambda: self.generatekeys('BD'))
        self.btn_pbdenc_rec.clicked.connect(lambda: self.prmodes('BD', 'Recommended'))
        self.btn_pbdenc_adv.clicked.connect(lambda: self.prmodes('BD', 'Advanced'))

        self.btn_pbdenc_sf.clicked.connect(lambda: self.selectfile())

        self.cmbx_pbdenc_pad.currentIndexChanged.connect(lambda: self.hidesettings(self.cmbx_pbdenc_pad, 'BD', False))
        self.cmbx_pbdencs_sch.currentIndexChanged.connect(lambda: self.hidesettings(self.cmbx_pbdencs_sch, 'BD', True))

        self.cmbx_pbdenc_pbk.currentIndexChanged.connect(
            lambda: self.enterkeys(self.stw_pbdenc_pbk, self.cmbx_pbdenc_pbk, 'BD', 'enc'))
        self.cmbx_pbdenc_prk.currentIndexChanged.connect(
            lambda: self.enterkeys(self.stw_pbdenc_prk, self.cmbx_pbdenc_prk, 'BD', 'enc', signature=True))

        self.btn_pbdenc_enc.clicked.connect(lambda: self.encryption('BD'))
        self.btn_pbdenc_addkdep.clicked.connect(lambda: self.addkeysdepository('BD'))
        # Decryption
        self.cmbx_pbddec_prk.currentIndexChanged.connect(
            lambda: self.enterkeys(self.stw_pbddec_prk, self.cmbx_pbddec_prk, 'BD', 'dec'))
        self.cmbx_pbddec_pbk.currentIndexChanged.connect(
            lambda: self.enterkeys(self.stw_pbddec_pbk, self.cmbx_pbddec_pbk, 'BD', 'dec', signature=True))

        self.btn_pbddec_dec.clicked.connect(lambda: self.decryption('BD'))
        self.btn_pbddec_addkdep.clicked.connect(lambda: self.addkeysdepository('BD'))

        self.lbl_pbddec_signval.setEnabled(False)
        # ECC
        self.btn_peccg_genk.clicked.connect(lambda: self.generatekeys('ECC'))
        self.btn_peccg_addkdep.clicked.connect(lambda: self.addkeysdepository('ECC'))

        self.cmbx_peccex_prk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_peccex_prk, self.cmbx_peccex_prk,
                                                                                'ECC', 'prk'))
        self.cmbx_peccex_pbk.currentIndexChanged.connect(lambda: self.enterkeys(self.stw_peccex_pbk, self.cmbx_peccex_pbk,
                                                                                'ECC', 'pbk'))
        self.btn_peccex_dshk.clicked.connect(lambda: self.decryption('ECC'))
        self.btn_peccex_addkdep.clicked.connect(lambda: self.addkeysdepository('ECC', eccexchange=True))

        # Education tab
        self.btn_emn_rsa.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_ersa))
        self.btn_emn_aes.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eaes))
        self.btn_emn_ecc.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eecc))
        self.btn_emn_ecdh.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eecdh))
        self.btn_emn_pr.clicked.connect(lambda: self.tw_mn.setCurrentWidget(self.tab_pr))
        # All-buttons
        self.btn_ersah_all.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_emn))
        self.btn_eaesh_all.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_emn))
        self.btn_eecch_all.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_emn))
        self.btn_eecdhh_all.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_emn))
        # Back/Further buttons
        self.btn_ersab_fr.clicked.connect(lambda: self.backfurther(self.stw_ersa, self.ersa_buttons, 'further'))
        self.btn_ersab_bk.clicked.connect(lambda: self.backfurther(self.stw_ersa, self.ersa_buttons, 'back'))
        self.btn_eaesb_fr.clicked.connect(lambda: self.backfurther(self.stw_eaes, self.eaes_buttons, 'further'))
        self.btn_eaesb_bk.clicked.connect(lambda: self.backfurther(self.stw_eaes, self.eaes_buttons, 'back'))
        self.btn_eeccb_fr.clicked.connect(lambda: self.backfurther(self.stw_eecc, self.eecc_buttons, 'further'))
        self.btn_eeccb_bk.clicked.connect(lambda: self.backfurther(self.stw_eecc, self.eecc_buttons, 'back'))
        self.btn_eecdhb_fr.clicked.connect(lambda: self.backfurther(self.stw_eecdh, self.eecdh_buttons, 'further'))
        self.btn_eecdhb_bk.clicked.connect(lambda: self.backfurther(self.stw_eecdh, self.eecdh_buttons, 'back'))
        # Radio buttons
        self.rbtn_ersah1.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 0))
        self.rbtn_ersah2.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 1))
        self.rbtn_ersah3.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 2))
        self.rbtn_ersah4.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 3))
        self.rbtn_ersah5.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 4))
        self.rbtn_ersah6.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 5))
        self.rbtn_ersah7.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 6))
        self.rbtn_ersah8.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 7))
        self.rbtn_ersah9.clicked.connect(lambda: self.radiobuttons(self.stw_ersa, self.ersa_buttons, 8))

        self.rbtn_eaesh1.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 0))
        self.rbtn_eaesh2.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 1))
        self.rbtn_eaesh3.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 2))
        self.rbtn_eaesh4.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 3))
        self.rbtn_eaesh5.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 4))
        self.rbtn_eaesh6.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 5))
        self.rbtn_eaesh7.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 6))
        self.rbtn_eaesh8.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 7))
        self.rbtn_eaesh9.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 8))
        self.rbtn_eaesh10.clicked.connect(lambda: self.radiobuttons(self.stw_eaes, self.eaes_buttons, 9))

        self.rbtn_eecch1.clicked.connect(lambda: self.radiobuttons(self.stw_eecc, self.eecc_buttons, 0))
        self.rbtn_eecch2.clicked.connect(lambda: self.radiobuttons(self.stw_eecc, self.eecc_buttons, 1))
        self.rbtn_eecch3.clicked.connect(lambda: self.radiobuttons(self.stw_eecc, self.eecc_buttons, 2))
        self.rbtn_eecch4.clicked.connect(lambda: self.radiobuttons(self.stw_eecc, self.eecc_buttons, 3))
        self.rbtn_eecch5.clicked.connect(lambda: self.radiobuttons(self.stw_eecc, self.eecc_buttons, 4))

        self.rbtn_eecdhh1.clicked.connect(lambda: self.radiobuttons(self.stw_eecdh, self.eecdh_buttons, 0))
        self.rbtn_eecdhh2.clicked.connect(lambda: self.radiobuttons(self.stw_eecdh, self.eecdh_buttons, 1))
        self.rbtn_eecdhh3.clicked.connect(lambda: self.radiobuttons(self.stw_eecdh, self.eecdh_buttons, 2))
        self.rbtn_eecdhh4.clicked.connect(lambda: self.radiobuttons(self.stw_eecdh, self.eecdh_buttons, 3))

        self.rbtn_ersah1.setChecked(True)
        self.rbtn_eaesh1.setChecked(True)
        self.rbtn_eecch1.setChecked(True)
        self.rbtn_eecdhh1.setChecked(True)
        # To explore buttons
        self.btn_eeccmn5_ecdh.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eecdh))
        self.btn_eecdhmn1_ecc.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eecc))
        self.btn_eecdhmn4_aes.clicked.connect(lambda: self.stw_edu.setCurrentWidget(self.pg_eaes))

    def operation(self, container):
        if container.currentIndex() == 0:
            container.setCurrentIndex(1)
        else:
            container.setCurrentIndex(0)

    def prmodes(self, alg, mode):
        if alg == 'RSA':
            if mode == 'Recommended':
                self.cmbx_prsaenc_inenc.setCurrentText('UTF-8')
                self.cmbx_prsaenc_outfm.setCurrentText('Base64')
                self.cmbx_prsaenc_pad.setCurrentText('OAEP')
                self.cmbx_prsaenc_pad.setEnabled(False)
                self.cmbx_prsaenc_hash.setCurrentText('SHA-256')
                self.cmbx_prsaenc_hash.setEnabled(False)
                self.cmbx_prsaenc_mgfhash.setCurrentText('SHA-256')
                self.cmbx_prsaenc_mgfhash.setEnabled(False)
                self.lbl_prsaenc_lbl.setEnabled(False)
                self.lne_prsaenc_lbl.setEnabled(False)
                self.cmbx_prsaencs_sch.setCurrentText('RSA-PSS')
                self.cmbx_prsaencs_sch.setEnabled(False)
                self.cmbx_prsaencs_hash.setCurrentText('SHA-256')
                self.cmbx_prsaencs_hash.setEnabled(False)
                self.cmbx_prsaencs_mgfhash.setCurrentText('SHA-256')
                self.cmbx_prsaencs_mgfhash.setEnabled(False)
                self.cmbx_prsaencs_sl.setCurrentText('Maximum')
                self.cmbx_prsaencs_sl.setEnabled(False)
            else:
                self.cmbx_prsaenc_inenc.setCurrentText('UTF-8')
                self.cmbx_prsaenc_outfm.setCurrentText('Base64')
                self.cmbx_prsaenc_pad.setCurrentText('OAEP')
                self.cmbx_prsaenc_pad.setEnabled(True)
                self.cmbx_prsaenc_hash.setCurrentText('SHA-256')
                self.cmbx_prsaenc_hash.setEnabled(True)
                self.cmbx_prsaenc_mgfhash.setCurrentText('SHA-256')
                self.cmbx_prsaenc_mgfhash.setEnabled(True)
                self.lbl_prsaenc_lbl.setEnabled(True)
                self.lne_prsaenc_lbl.setEnabled(True)
                self.cmbx_prsaencs_sch.setCurrentText('RSA-PSS')
                self.cmbx_prsaencs_sch.setEnabled(True)
                self.cmbx_prsaencs_hash.setCurrentText('SHA-256')
                self.cmbx_prsaencs_hash.setEnabled(True)
                self.cmbx_prsaencs_mgfhash.setCurrentText('SHA-256')
                self.cmbx_prsaencs_mgfhash.setEnabled(True)
                self.cmbx_prsaencs_sl.setCurrentText('Maximum')
                self.cmbx_prsaencs_sl.setEnabled(True)
        elif alg == 'BD':
            if mode == 'Recommended':
                self.cmbx_pbdenc_inenc.setCurrentText('UTF-8')
                self.cmbx_pbdenc_outfm.setCurrentText('Base64')
                self.cmbx_pbdenc_pad.setCurrentText('OAEP')
                self.cmbx_pbdenc_pad.setEnabled(False)
                self.cmbx_pbdenc_hash.setCurrentText('SHA-256')
                self.cmbx_pbdenc_hash.setEnabled(False)
                self.cmbx_pbdenc_mgfhash.setCurrentText('SHA-256')
                self.cmbx_pbdenc_mgfhash.setEnabled(False)
                self.cmbx_pbdencs_sch.setCurrentText('RSA-PSS')
                self.cmbx_pbdencs_sch.setEnabled(False)
                self.cmbx_pbdencs_hash.setCurrentText('SHA-256')
                self.cmbx_pbdencs_hash.setEnabled(False)
                self.cmbx_pbdencs_mgfhash.setCurrentText('SHA-256')
                self.cmbx_pbdencs_mgfhash.setEnabled(False)
                self.cmbx_pbdencs_sl.setCurrentText('Maximum')
                self.cmbx_pbdencs_sl.setEnabled(False)
            else:
                self.cmbx_pbdenc_inenc.setCurrentText('UTF-8')
                self.cmbx_pbdenc_outfm.setCurrentText('Base64')
                self.cmbx_pbdenc_pad.setCurrentText('OAEP')
                self.cmbx_pbdenc_pad.setEnabled(True)
                self.cmbx_pbdenc_hash.setCurrentText('SHA-256')
                self.cmbx_pbdenc_hash.setEnabled(True)
                self.cmbx_pbdenc_mgfhash.setCurrentText('SHA-256')
                self.cmbx_pbdenc_mgfhash.setEnabled(True)
                self.cmbx_pbdencs_sch.setCurrentText('RSA-PSS')
                self.cmbx_pbdencs_sch.setEnabled(True)
                self.cmbx_pbdencs_hash.setCurrentText('SHA-256')
                self.cmbx_pbdencs_hash.setEnabled(True)
                self.cmbx_pbdencs_mgfhash.setCurrentText('SHA-256')
                self.cmbx_pbdencs_mgfhash.setEnabled(True)
                self.cmbx_pbdencs_sl.setCurrentText('Maximum')
                self.cmbx_pbdencs_sl.setEnabled(True)

    def hidesettings(self, cmbxs, alg, signature):
        if alg == 'RSA':
            if cmbxs.currentText() == 'PKCS1v15':
                if signature:
                    self.lbl_prsaencs_hash.setEnabled(False)
                    self.cmbx_prsaencs_hash.setEnabled(False)
                    self.lbl_prsaencs_mgfhash.setEnabled(False)
                    self.cmbx_prsaencs_mgfhash.setEnabled(False)
                    self.lbl_prsaencs_sl.setEnabled(False)
                    self.cmbx_prsaencs_sl.setEnabled(False)
                    self.lbl_prsaencs_mgf.setEnabled(False)
                else:
                    self.lbl_prsaenc_hash.setEnabled(False)
                    self.cmbx_prsaenc_hash.setEnabled(False)
                    self.lbl_prsaenc_mgfhash.setEnabled(False)
                    self.cmbx_prsaenc_mgfhash.setEnabled(False)
                    self.lbl_prsaenc_lbl.setEnabled(False)
                    self.lne_prsaenc_lbl.setEnabled(False)
                    self.lbl_prsaenc_mgf.setEnabled(False)
            else:
                if signature:
                    self.lbl_prsaencs_hash.setEnabled(True)
                    self.cmbx_prsaencs_hash.setEnabled(True)
                    self.lbl_prsaencs_mgfhash.setEnabled(True)
                    self.cmbx_prsaencs_mgfhash.setEnabled(True)
                    self.lbl_prsaencs_sl.setEnabled(True)
                    self.cmbx_prsaencs_sl.setEnabled(True)
                    self.lbl_prsaencs_mgf.setEnabled(True)
                else:
                    self.lbl_prsaenc_hash.setEnabled(True)
                    self.cmbx_prsaenc_hash.setEnabled(True)
                    self.lbl_prsaenc_mgfhash.setEnabled(True)
                    self.cmbx_prsaenc_mgfhash.setEnabled(True)
                    self.lbl_prsaenc_lbl.setEnabled(True)
                    self.lne_prsaenc_lbl.setEnabled(True)
                    self.lbl_prsaenc_mgf.setEnabled(True)
        elif alg == 'BD':
            if cmbxs.currentText() == 'PKCS1v15':
                if signature:
                    self.lbl_pbdencs_hash.setEnabled(False)
                    self.cmbx_pbdencs_hash.setEnabled(False)
                    self.lbl_pbdencs_mgfhash.setEnabled(False)
                    self.cmbx_pbdencs_mgfhash.setEnabled(False)
                    self.lbl_pbdencs_sl.setEnabled(False)
                    self.cmbx_pbdencs_sl.setEnabled(False)
                    self.lbl_pbdencs_mgf.setEnabled(False)
                else:
                    self.lbl_pbdenc_hash.setEnabled(False)
                    self.cmbx_pbdenc_hash.setEnabled(False)
                    self.lbl_pbdenc_mgfhash.setEnabled(False)
                    self.cmbx_pbdenc_mgfhash.setEnabled(False)
                    self.lbl_pbdenc_mgf.setEnabled(False)
            else:
                if signature:
                    self.lbl_pbdencs_hash.setEnabled(True)
                    self.cmbx_pbdencs_hash.setEnabled(True)
                    self.lbl_pbdencs_mgfhash.setEnabled(True)
                    self.cmbx_pbdencs_mgfhash.setEnabled(True)
                    self.lbl_pbdencs_sl.setEnabled(True)
                    self.cmbx_pbdencs_sl.setEnabled(True)
                    self.lbl_pbdencs_mgf.setEnabled(True)
                else:
                    self.lbl_pbdenc_hash.setEnabled(True)
                    self.cmbx_pbdenc_hash.setEnabled(True)
                    self.lbl_pbdenc_mgfhash.setEnabled(True)
                    self.cmbx_pbdenc_mgfhash.setEnabled(True)
                    self.lbl_pbdenc_mgf.setEnabled(True)

    def enterkeys(self, container, cmbxs, alg, encdec, signature=False):
        if alg == 'RSA':
            container.setEnabled(True)
            if encdec == 'enc':
                if cmbxs.currentText() == 'Depository':
                    if signature:
                        container.setCurrentWidget(self.pg_prsaencs_dep)
                    else:
                        container.setCurrentWidget(self.pg_prsaenc_dep)
                elif cmbxs.currentText() == 'Enter':
                    if signature:
                        container.setCurrentWidget(self.pg_prsaencs_ent)
                    else:
                        container.setCurrentWidget(self.pg_prsaenc_ent)
                elif cmbxs.currentText() == 'Generate':
                    container.setEnabled(False)
            else:
                if cmbxs.currentText() == 'Depository':
                    if signature:
                        container.setCurrentWidget(self.pg_prsadecs_dep)
                    else:
                        container.setCurrentWidget(self.pg_prsadec_dep)
                elif cmbxs.currentText() == 'Enter':
                    if signature:
                        container.setCurrentWidget(self.pg_prsadecs_ent)
                    else:
                        container.setCurrentWidget(self.pg_prsadec_ent)
        elif alg == 'AES':
            container.setEnabled(True)
            if encdec == 'enc':
                if cmbxs.currentText() == 'Depository':
                    container.setCurrentWidget(self.pg_paesenc_dep)
                elif cmbxs.currentText() == 'Enter':
                    container.setCurrentWidget(self.pg_paesenc_oth)
                elif cmbxs.currentText() == 'Generate':
                    container.setEnabled(False)
                elif cmbxs.currentText() == 'ECC-key':
                    container.setCurrentWidget(self.pg_paesenc_oth)
            else:
                if cmbxs.currentText() == 'Depository':
                    container.setCurrentWidget(self.pg_paesdec_dep)
                elif cmbxs.currentText() == 'Enter':
                    container.setCurrentWidget(self.pg_paesdec_ent)
        elif alg == 'BD':
            container.setEnabled(True)
            if encdec == 'enc':
                if cmbxs.currentText() == 'Depository':
                    if signature:
                        container.setCurrentWidget(self.pg_pbdencs_dep)
                    else:
                        container.setCurrentWidget(self.pg_pbdenc_dep)
                elif cmbxs.currentText() == 'Enter':
                    if signature:
                        container.setCurrentWidget(self.pg_pbdencs_ent)
                    else:
                        container.setCurrentWidget(self.pg_pbdenc_ent)
                elif cmbxs.currentText() == 'Generate':
                    container.setEnabled(False)
            else:
                if cmbxs.currentText() == 'Depository':
                    if signature:
                        container.setCurrentWidget(self.pg_pbddecs_dep)
                    else:
                        container.setCurrentWidget(self.pg_pbddec_dep)
                elif cmbxs.currentText() == 'Enter':
                    if signature:
                        container.setCurrentWidget(self.pg_pbddecs_ent)
                    else:
                        container.setCurrentWidget(self.pg_pbddec_ent)
        elif alg == 'ECC':
            if encdec == 'prk':
                if cmbxs.currentText() == 'Depository':
                    container.setCurrentWidget(self.pg_peccex_dep)
                elif cmbxs.currentText() == 'Enter':
                    container.setCurrentWidget(self.pg_peccex_ent)
            else:
                if cmbxs.currentText() == 'Depository':
                    container.setCurrentWidget(self.pg_peccex_pbkdep)
                elif cmbxs.currentText() == 'Enter':
                    container.setCurrentWidget(self.pg_peccex_pbkent)

    def encryption(self, alg):
        if alg == 'RSA':
            pass
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

    def backfurther(self, container, btns, method):
        if method == 'further':
            if container.currentIndex() + 1 < container.count():
                container.setCurrentIndex(container.currentIndex() + 1)
                btns[container.currentIndex()][0].setChecked(True)
                btns[container.currentIndex() - 1][1].setChecked(True)
            else:
                container.setCurrentIndex(0)
                for btn in btns.values():
                    btn[0].setChecked(False)
                    btn[1].setChecked(False)
                btns[container.currentIndex()][0].setChecked(True)
        else:
            if container.currentIndex() > 0:
                container.setCurrentIndex(container.currentIndex() - 1)
                btns[container.currentIndex() + 1][0].setChecked(False)
                btns[container.currentIndex()][1].setChecked(False)
            else:
                container.setCurrentIndex(container.count() - 1)
                for btn in btns.values():
                    btn[0].setChecked(True)
                    btn[1].setChecked(True)
                btns[container.currentIndex()][1].setChecked(False)

    def radiobuttons(self, container, btns, num):
        container.setCurrentIndex(num)
        for key, btn in btns.items():
            if key <= container.currentIndex():
                btn[0].setChecked(True)
                btn[1].setChecked(True)
            else:
                btn[0].setChecked(False)
                btn[1].setChecked(False)
        btns[container.currentIndex()][1].setChecked(False)
