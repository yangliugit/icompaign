# -*- coding: utf-8_*
import os
from lxml import html
import lxml.etree as mytree


class TestReport(object):

    def __init__(self):
        self.testreport = r"F:\icompaign\docs\testresult.html"

    def create_html_file(self):
        if os.path.exists(self.testreport) is False:
            f = open(self.testreport, "w")
            message = '''
            <html>
            <head>
                <title>Automation Test Result</title>
                <style>
                    table {
                            border-collapse: collapse;
                            padding: 15px;
                            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                            }
                    th{
                        background-color: green;
                        color: white;
                        border: 1px solid #ddd;
                        padding-bottom: 15px;
                        padding-top: 15px;
                    }
                    tr{
                        border: 1px solid #008000;
                        padding-bottom: 8px;
                        padding-top: 8px;
                        text-align: left;
                    }
                    td{
                        border: 1px solid #008000;
                    }
                </style>
            </head>
            <body>
                <h1>Automation Test Result</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th>Result</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>ErrorMessage</th>
                   </tr>
                </table>
            </body>
            </html>
            '''
            f.write(message)
            f.close()

    def write_html(self, testcaseinfo):

        self.create_html_file()

        f = open(self.testreport)
        htmlcontent = f.read()
        f.close()
        tree = html.fromstring(htmlcontent)
        table_elem = tree.find(".//table")
        if testcaseinfo.result == "faild":
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td bgcolor=\"#FF0000\">{3}</td><td>{4}</td>" \
                         "<td>{5}</td><td>{6}</td>" \
                         "</tr>".format(testcaseinfo.caseid, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result,
                                        testcaseinfo.starttime, testcaseinfo.endtime
                                        , testcaseinfo.errorinfo)
        else:
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td>" \
                         "</tr>".format(testcaseinfo.caseid, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result,
                                        testcaseinfo.starttime, testcaseinfo.endtime
                                        , testcaseinfo.errorinfo)

        table_elem.append(mytree.HTML(str(mytablerow)))

        f = open(self.testreport, "w")
        new_content = repr(html.tostring(tree, method="html", with_tail=False))
        new_content = new_content.replace(r"\n", "").replace(r"\t", "").replace('b\'', "").replace("'", "").replace("\\", "")
        new_content = new_content[:len(new_content)-1]
        f.write(new_content)
        f.close()
