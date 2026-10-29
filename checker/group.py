from . import impl
from . import resultwin
import importlib
#importlib.reload(impl)
#importlib.reload(resultwin)

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    from PySide2 import QtWidgets, QtCore

class ErrorCheckWidgetGroup(QtWidgets.QGroupBox):
    ##
    # @brief エラーチェッカー起動グループボックス
    ##
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        main_layout = QtWidgets.QVBoxLayout()
        self.runcheck = QtWidgets.QPushButton("Check Scene")
        self.runcheck.clicked.connect(self.run_check)
        main_layout.addWidget(self.runcheck)
        self.setLayout(main_layout)

        # エラチェのリザルト
        self.__unity_errorchecker_ui = None
        self.__initialize_checkers()

    def __initialize_checkers(self):
        self.__checkers = [
            impl.Check_Freezed(),
            impl.Check_DeletedHistory(),
            impl.Check_BackFace(),
            impl.Check_NodeNames(),
            impl.Check_BasePose(),
        ]

    def run_check(self):
        for elem in self.__checkers:
            elem.check()
        if self.__unity_errorchecker_ui:
            try:
                self.__unity_errorchecker_ui.close()
                self.__unity_errorchecker_ui.deleteLater()
            except NameError:
                pass
        self.__unity_errorchecker_ui = resultwin.ErrorCheckerResult(self, self.__checkers)
        self.__unity_errorchecker_ui.show()



