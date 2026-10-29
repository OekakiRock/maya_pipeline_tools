try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

class FileDialogWidgetGroup(QtWidgets.QGroupBox):
    ##
    # @brief (未使用：エクスポータに統合)
    ##
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        path_layout = QtWidgets.QHBoxLayout()
        
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setPlaceholderText("Select export path or asset name...")
        path_layout.addWidget(self.line_edit)

        self.browse_btn = QtWidgets.QPushButton("Browse...", self)
        path_layout.addWidget(self.browse_btn)

        # グループレイアウトに追加
        self.setLayout(path_layout)

    def get_filepath(self):
        return self.line_edit.text()
