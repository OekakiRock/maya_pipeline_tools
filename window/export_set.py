import sys
import importlib
from ..utils import group as filedialog_group
from ..checker import group as check_group
from ..exporter import group as export_group
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    from PySide2 import QtWidgets, QtCore

class ToolWidget(MayaQWidgetBaseMixin, QtWidgets.QWidget):
    ##
    # @brief 生成時にグループボックスをセットできるウィンドウ
    # @note MayaQWidgetBaseMixin、Windowを手前によこす
    ##
    def __init__(self, parent=None):
        super().__init__(parent)

        # Maya上で単独のウィンドウとして表示するためのフラグ
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle("Maya Pipline Tool for Unity")
        self.resize(320, 320)

        main_layout = QtWidgets.QVBoxLayout(self)

        # 各グループボックスをメインレイアウトに追加
        self.__errorchecker = check_group.ErrorCheckWidgetGroup("Error Checker")
        self.__destpath = filedialog_group.FileDialogWidgetGroup("Output Path")
        self.__exporter = export_group.ExportWidgetGroup("Export")
        main_layout.addWidget(self.__errorchecker)
        main_layout.addWidget(self.__destpath)
        main_layout.addWidget(self.__exporter)

        # レイアウトの下部に上詰めのためのスペーサー（余白）を追加
        main_layout.addStretch()

        # ウィジェット全体のメインレイアウトとして設定
        self.setLayout(main_layout)

    ## TODO: 死んだら子供も殺すようにした方がいいかも…？

def get_maya_window():
    ##
    # @brief Mayaウィンドウを取得
    ##
    app = QtWidgets.QApplication.instance()
    if app:
        for widget in app.topLevelWidgets():
            if widget.objectName() == "MayaWindow":
                return widget
    return None

# Mayaのスクリプトエディタ（Python）から実行する処理
def show_ui():
    importlib.reload(filedialog_group)
    importlib.reload(check_group)
    importlib.reload(export_group)

    global unity_pipeline_ui
    try:
        unity_pipeline_ui.close()
        unity_pipeline_ui.deleteLater()
    except NameError:
        pass

    unity_pipeline_ui = ToolWidget()
    unity_pipeline_ui.show()
