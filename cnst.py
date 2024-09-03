import gdsfactory as gf
import os

def run_cnst(cnst_path: str, 
             cnst_jar_path: str,
             javafx_sdk_path: str,
             gds_filename: str):

    javafx_sdk_path=javafx_sdk_path
    javafx_modules_path='javafx.controls,javafx.fxml'
    gds_filename=gds_filename

    cnst_run_comm = 'java --module-path ' + javafx_sdk_path + ' --add-modules ' + \
    javafx_modules_path + ' -jar ' + cnst_jar_path + ' cnstscripting '

    os.system(cnst_run_comm + cnst_path + ' ' + gds_filename)

if __name__ == "__main__":
    print("cnst.py has been invoked")