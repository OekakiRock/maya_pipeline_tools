from . import impl
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    from PySide2 import QtWidgets, QtCore


class ErrorCheckerResult(MayaQWidgetBaseMixin, QtWidgets.QWidget):
    def __init__(self, parent=None, in_checkers=[]):
        super().__init__(parent)

        self.__checkers = in_checkers
        self.setWindowFlags(QtCore.Qt.Window)

        # 全体を配置するメインのレイアウト
        main_layout = QtWidgets.QVBoxLayout(self)

        # 左でカテゴリ選択、右でエラー毎の選択
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self)
        
        # 左側: チェッカー項目のリスト
        self.category_list = QtWidgets.QListWidget(self)
        self.category_list.addItems([elem.get_discliption() for elem in self.__checkers])
        splitter.addWidget(self.category_list)
        
        # 右側: 検出されたイシューの一覧テーブル
        self.issue_table = QtWidgets.QTableWidget(self)
        self.issue_table.setColumnCount(3)
        self.issue_table.setHorizontalHeaderLabels(["Object Name", "Issue Type", "Description"])
        splitter.addWidget(self.issue_table)
        
        # 左右の初期幅の比率を設定（例: 左30%、右70%）
        splitter.setSizes([150, 350])
        
        # メインレイアウトにスプリッターを追加
        main_layout.addWidget(splitter)
        
        # --------------------------------------------------
        # 2. 選択変更時の連動（シグナルとスロット）
        # --------------------------------------------------
        self.category_list.currentItemChanged.connect(self.on_category_changed)

    def on_category_changed(self, current, previous):
        ##
        # @brief 左側の項目がクリックされたときの処理
        ##
        if not current:
            return
        self.issue_table.clearContents()
        current.issue_table
        #self.issue_table.
