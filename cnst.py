import gdsfactory as gf
import os
from layer_map import LAYER

def run_cnst(cnstpath: str, 
             cnst_jar_path: str,
             javafx_sdk_path: str,
             gds_filename: str):

    javafx_sdk_path=str(javafx_sdk_path)
    javafx_modules_path='javafx.controls,javafx.fxml'
    gds_filename=str(gds_filename)

    cnst_run_comm='java --module-path ' + javafx_sdk_path + ' --add-modules ' + \
    javafx_modules_path + ' -jar ' + cnst_jar_path + ' cnstscripting '

    os.system(cnst_run_comm + cnstpath + ' ' + gds_filename)

def remove_gds(gdspath: str, cnstpath: str):
    
    os.remove(gdspath)
    os.remove(gdspath + '.log')

def cnst_to_gf(cnstpath: str,
               cnst_jar_path: str,
               javafx_sdk_path: str,
               gds_filename: str):   

    run_cnst(cnstpath, cnst_jar_path, javafx_sdk_path, gds_filename)
     
    component = gf.import_gds('gds/' + str(gds_filename))
    
    remove_gds('gds/' + str(gds_filename), cnstpath)

    return component

if __name__ == "__main__":
    print("cnst.py has been invoked")