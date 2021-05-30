import glob
import os
import time
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
# path_reg = ROOT_DIR + '\\..\\..\\Datasets\\processed\\regression_10d'
# print(path_reg)
#
# csvfiles_reg = glob.glob(path_reg + "/*.csv")
#
#
# for j, file_reg in enumerate(csvfiles_reg):
#     pm.execute_notebook('mlpModelRegression.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":64})
#     pm.execute_notebook('mlpModelRegression.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":32})
#     pm.execute_notebook('mlpModelRegression.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":13})

# path_lstm = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm'
#
# csvfiles_lstm = glob.glob(path_lstm + "/*.csv")
#
# for k, file_lstm in enumerate(csvfiles_lstm):
#     print(file_lstm)
#     stock_name = (os.path.basename(file_lstm)).split('_')[0]
#     print(os.path.basename(file_lstm))
#     pm.execute_notebook('lstmModelClassKeras.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "tuner_package":stock_name})
#     pm.execute_notebook('lstmModelClassKeras.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":26118, "tuner_package":stock_name})
#     pm.execute_notebook('lstmModelClassKeras.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":35352, "tuner_package":stock_name})
#     time.sleep(20)

## NEW NEW NEW
# path_lstm = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm'
#
# csvfiles_lstm = glob.glob(path_lstm + "/*.csv")
#
# for k, file_lstm in enumerate(csvfiles_lstm):
#     if (k != 0):
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":150})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":120})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":180})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":210})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":70, "no_epochs":150})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":70, "no_epochs":120})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":70, "no_epochs":180})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":70, "no_epochs":210})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":130, "no_epochs":150})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":130, "no_epochs":120})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":130, "no_epochs":180})
#         pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":130, "no_epochs":210})
#         time.sleep(20)

path_class = ROOT_DIR + '\\..\\..\\Datasets\\processed\\classification_10d'
path_reg = ROOT_DIR + '\\..\\..\\Datasets\\processed\\regression_10d'
csvfiles_class = glob.glob(path_class + "/*.csv")
csvfiles_reg = glob.glob(path_reg + "/*.csv")

for k, file_class in enumerate(csvfiles_class):
    ##pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":150, "shuffle_bool":False})
    ##pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":150, "shuffle_bool":True})
    # pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "activation":'sigmoid'})
    pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "activation":'softmax'})
    time.sleep(2)

# for j, file_reg in enumerate(csvfiles_reg):
#     pm.execute_notebook('mlpModelRegression.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":41291})
#     time.sleep(10)
