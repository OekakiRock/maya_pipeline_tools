import maya.cmds as cmds
import maya.mel as mel

def export_model(nodes, path):
    ##
    # @brief 環境依存の事故を起こさないため、基本的に一つのプロジェクトでは設定は一律。
    ##
    mel.eval("FBXExportAnimationOnly -v 0")
    mel.eval("FBXExportApplyConstantKeyReducer -v 0")
    mel.eval("FBXExportAxisConversionMethod convertAnimation")
    mel.eval("FBXExportBakeComplexAnimation -v false")
    mel.eval("FBXExportBakeComplexEnd -v 200")
    mel.eval("FBXExportBakeComplexStart -v 1")
    mel.eval("FBXExportBakeComplexStep -v 1")
    mel.eval("FBXExportBakeResampleAnimation -v 0")
    mel.eval("FBXExportCacheFile -v 0")
    mel.eval("FBXExportCameras -v 1")
    mel.eval("FBXExportColladaFrameRate 24.0")
    mel.eval("FBXExportColladaSingleMatrix true")
    mel.eval("FBXExportColladaTriangulate true")
    mel.eval("FBXExportConstraints -v 0")
    mel.eval("FBXExportConvertUnitString -v 1.0")
    mel.eval("FBXExportEmbeddedTextures -v 0")
    mel.eval("FBXExportFileVersion FBX202000")
    mel.eval("FBXExportGenerateLog -v 1")
    mel.eval("FBXExportHardEdges -v 0")
    mel.eval("FBXExportInAscii -v 0")
    mel.eval("FBXExportInputConnections -v 1")
    mel.eval("FBXExportInstances -v 0")
    mel.eval("FBXExportLights -v 1")
    mel.eval("FBXExportQuaternion -v resample")
    try:
        cmds.select(nodes)
        cmds.file(path, force=True, options="v=0;", type="FBX export", exportSelected=True)
        cmds.select(clear=True)
        return True
    except Exception as e:
        print(e)    
    return False