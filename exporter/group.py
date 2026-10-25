from . import impl
try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

class ExportWidgetGroup(QtWidgets.QGroupBox):
    ##
    # @brief 要素C: 何も connect しない PushButton
    ##
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        main_layout = QtWidgets.QVBoxLayout(self)
        self.checkbox_1 = QtWidgets.QCheckBox("Export Animation", self)
        self.checkbox_2 = QtWidgets.QCheckBox("Embed Textures", self)
        self.checkbox_3 = QtWidgets.QCheckBox("Optimize Geometry", self)

        # デフォルトのチェック状態を設定（必要に応じて変更可能）
        self.checkbox_1.setChecked(False)
        self.checkbox_1.setChecked(False)
        self.checkbox_1.setChecked(False)

        main_layout.addWidget(self.checkbox_1)
        main_layout.addWidget(self.checkbox_2)
        main_layout.addWidget(self.checkbox_3)

        self.action_btn = QtWidgets.QPushButton("Execute Export", self)
        main_layout.addWidget(self.action_btn)

        self.setLayout(main_layout)
