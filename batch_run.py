import glob
import os
import papermill as pm

ROOT_DIR = os.path.abspath(os.curdir)
# path = ROOT_DIR + '\\..\\..\\Datasets\\processed\\classification_10d'
# print(path)

# csvfiles = glob.glob(path + "/*.csv")


# for i, file in enumerate(csvfiles):
#     pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":i, "my_seed":64})
#     pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":i, "my_seed":32})
#     pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":i, "my_seed":13})
#
path_reg = ROOT_DIR + '\\..\\..\\Datasets\\processed\\regression_10d'
print(path_reg)

csvfiles_reg = glob.glob(path_reg + "/*.csv")


for j, file_reg in enumerate(csvfiles_reg):
    pm.execute_notebook('mlpModelMix.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":64})
    pm.execute_notebook('mlpModelMix.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":32})
    pm.execute_notebook('mlpModelMix.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":13})
