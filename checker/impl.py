import maya.cmds as cmds
import weakref

class IssueBase:
    ##
    # @brief エラー詳細(エラーチェッカーのリザルトウィンドウ右側の項目)
    ##
    def __init__(self, msg="", node=""):
        self.__msg = msg
        self.__node = node
        self.__fixfunc = None
        self.__args = None

    def set_fixfinc(self, in_func, *args)
        self.__fixfunc = weakref.WeakMethod(fixfunc)
        self.__args = args

    def run_fix(self):
        temp_method = self.__fixfunc()
        if temp_method is not None:
            return temp_method(self.__args)
        return False

    def get_message(self):
        return self.__msg

    def get_node(self):
        return self.__node


class CheckerBase:
    ##
    # @brief エラーカテゴリ(エラーチェッカーのリザルトウィンドウ左側の項目)
    ##
    def __init__(self):
        self._issues = []

    def get_discliption(self):
        return "BaseClass for Checker"

    def is_warning(self):
        # Warningに落とす場合はオーバーライドする
        return False

    def check(self):
        pass

    def get_issues(self):
        return self._issues

    def auto_fix(self):
        print("naosu")


class Check_Freezed(CheckerBase):
    ##
    # @brief ルートノードに値が入ってないか。
    ##
    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "ルートノードに値が入ってないか"

    def check(self):
        
        IssueBase("なんでやねん", "mesh_root", self.auto_fix)
        self._issues.append()


class Check_DeletedHistory(CheckerBase):
    ##
    # @brief ヒストリ削除済みか
    ##
    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "ヒストリ削除済みか"

    def check(self):
        pass

class Check_Influence(CheckerBase):
    ##
    # @brief インフルエンス数が4を超えていないか
    ##

    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "インフルエンス数が4を超えていないか"

    def check(self):
        pass

class Check_BackFace(CheckerBase):
    ##
    # @brief 逆向き法線がないか。
    ##

    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "逆向き法線がないか"

    def check(self):
        pass

class Check_NodeNames(CheckerBase):
    ##
    # @brief 不正なノード名(デフォルト名、別階層の同名、ネムスペ)がまぎれていないか
    ##

    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "不正なノード名がまぎれていないか"

    def check(self):
        pass

class Check_BasePose(CheckerBase):
    ##
    # @brief ベースポーズが存在するか
    ##

    def __init__(self):
        super().__init__()

    def get_discliption(self):
        return "ベースポーズが存在するか"

    def check(self):
        pass


