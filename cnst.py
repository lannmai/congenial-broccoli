import gdsfactory as gf
import os

def run_cnst(cnstpath: str, 
             cnst_jar_path: str,
             javafx_sdk_path: str,
             gds_filename: str):

    javafx_sdk_path=javafx_sdk_path
    javafx_modules_path="javafx.controls,javafx.fxml"
    gds_filename=gds_filename

    cnst_run_comm='java --module-path ' + javafx_sdk_path + ' --add-modules ' + \
    javafx_modules_path + ' -jar ' + cnst_jar_path + ' cnstscripting '

    os.system(cnst_run_comm + cnstpath + ' ' + gds_filename)

def remove_gds_cnst(gdspath: str,
                    cnstpath: str):
    
    os.remove(gdspath)
    os.remove(cnstpath)

# TODO
def remap_layers(component: gf.Component):
    return 0

if __name__ == "__main__":
    print("cnst.py has been invoked")