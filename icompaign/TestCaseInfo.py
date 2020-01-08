class TestCaseInfo(object):
    def __init__(self, caseid="", name="", owner="", result="Failed", starttime="", endtime="", errorinfo=""):
        self.caseid = caseid
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.errorinfo = errorinfo
