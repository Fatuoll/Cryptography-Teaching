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
        # Back/Further buttons and RadioButtons
        self.btn_ersab_fr.clicked.connect(lambda: self.backfurther(self.stw_ersa, 'further', self.ersa_buttons))
        self.btn_ersab_bk.clicked.connect(lambda: self.backfurther(self.stw_ersa, 'back', self.ersa_buttons))
        self.btn_eaesb_fr.clicked.connect(lambda: self.backfurther(self.stw_eaes, 'further', self.eaes_buttons))
        self.btn_eaesb_bk.clicked.connect(lambda: self.backfurther(self.stw_eaes, 'back', self.eaes_buttons))
        self.btn_eeccb_fr.clicked.connect(lambda: self.backfurther(self.stw_eecc, 'further', self.eecc_buttons))
        self.btn_eeccb_bk.clicked.connect(lambda: self.backfurther(self.stw_eecc, 'back', self.eecc_buttons))
        self.btn_eecdhb_fr.clicked.connect(lambda: self.backfurther(self.stw_eecdh, 'further', self.eecdh_buttons))
        self.btn_eecdhb_bk.clicked.connect(lambda: self.backfurther(self.stw_eecdh, 'back', self.eecdh_buttons))

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

    def backfurther(self, container, method, btns):
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
