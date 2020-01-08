# -*- coding: utf-8 -*-
import subprocess


class NoseExecute(object):

    def __init__(self):
        self.testcaselistfile = "testcases.txt"

    def load_and_run_testcase(self):
        f = open(self.testcaselistfile)
        testlist = [case for case in f.readlines() if not case.startswith("#")]
        f.close()
        for casename in testlist:
            subprocess.call("nosetests " + str(casename).replace("\n", ""))

if __name__ == "__main__":
    noserun = NoseExecute()
    noserun.load_and_run_testcase()
