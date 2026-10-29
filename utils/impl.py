import maya.cmds as cmds

class SceneUtils:

    @staticmethod
    def find_parent(node):
        tempparent = cmds.listRelatives(node, p=True) or None
        if tempparent == None:
             return node
        return SceneUtils.find_parent(tempparent)

    @staticmethod
    def find_get_joint_root():
        result = SceneUtils.find_parent(cmds.ls(type="joint")[0])
        return result[0] if result else None

    @staticmethod
    def find_get_mesh_root():
        result = SceneUtils.find_parent(cmds.ls(type="mesh")[0])
        return result[0] if result else None

