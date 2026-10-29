import maya.cmds as cmds
import os
from . import impl
from ..utils import impl as utils_impl

try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

class ExportWidgetGroup(QtWidgets.QGroupBox):
    ##
    # @brief エクスポータ内包グループボックス
    ##
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        main_layout = QtWidgets.QVBoxLayout(self)

        ## エクスポートオプション ------------
        # 今後必要なら追加
        # self.checkbox_1 = QtWidgets.QCheckBox("Export Animation", self)
        # self.checkbox_2 = QtWidgets.QCheckBox("Embed Textures", self)
        # self.checkbox_3 = QtWidgets.QCheckBox("Optimize Geometry", self)

        # デフォルトのチェック状態を設定（必要に応じて変更可能）
        # self.checkbox_1.setChecked(False)
        # self.checkbox_2.setChecked(False)
        # self.checkbox_3.setChecked(False)

        # main_layout.addWidget(self.checkbox_1)
        # main_layout.addWidget(self.checkbox_2)
        # main_layout.addWidget(self.checkbox_3)
        # -----------------------------

        ## エクスポート先 ----------------
        path_layout = QtWidgets.QHBoxLayout()
        
        self.path_line_edit = QtWidgets.QLineEdit(self)
        self.path_line_edit.setPlaceholderText("Select export path ...")
        path_layout.addWidget(self.path_line_edit)

        self.browse_btn = QtWidgets.QPushButton("Browse...", self)
        self.browse_btn.clicked.connect(self.show_dialog)
        path_layout.addWidget(self.browse_btn)
        main_layout.addLayout(path_layout)

        ## 出力名
        name_layout = QtWidgets.QHBoxLayout()
        
        self.name_line_edit = QtWidgets.QLineEdit(self)
        self.name_line_edit.setPlaceholderText("asset name without extension...")
        name_layout.addWidget(self.name_line_edit)
        name_layout.addWidget(QtWidgets.QLabel(".fbx"))
        main_layout.addLayout(name_layout)

        self.action_btn = QtWidgets.QPushButton("Run Export", self)
        self.action_btn.clicked.connect(self.run_export)
        main_layout.addWidget(self.action_btn)
        # ----------------------------

        self.setLayout(main_layout)

    def show_dialog(self):
        path = cmds.fileDialog2(
            fileFilter="FBX (*.fbx);;All Files (*.*)",
            dialogStyle=2,
            fileMode=2) or [""]
        self.path_line_edit.setText(path[0].replace("\\", "/"))

    def run_export(self):
        # FIXME: モデル出力に問題あり
        jointroot = utils_impl.SceneUtils.find_get_joint_root()
        meshroot = utils_impl.SceneUtils.find_get_mesh_root()
        if (not cmds.objExists(jointroot)) or (not cmds.objExists(meshroot)):
            cmds.confirmDialog(title="Confirm", message="出力するモデルはキャラクターを想定しています。\n骨階層とメッシュのセットが必要です")
            return False

        temppath = self.path_line_edit.text()
        if not os.path.exists(temppath):
            cmds.confirmDialog(title="Confirm", message="出力先フォルダの存在を確認してください \n{}".format(temppath))
            return False

        if cmds.confirmDialog(title="Confirm", message="FBXを出力します。", button=("OK", "Cancel")) == "Cancel":
            return False

        path = "{}/{}.fbx".format(temppath, self.name_line_edit.text())
        impl.export_model([jointroot, meshroot], path)
        cmds.confirmDialog(title="Confirm", message="FBX出力を完了しました。")
        return True