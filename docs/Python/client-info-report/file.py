import config

def create_report(file_name, report_string):
    report = open(file_name + '.csv', 'a')
    report.write(report_string)
    report.close
