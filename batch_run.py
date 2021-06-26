import glob
import os
import time
import papermill as pm

ROOT_DIR = os.path.abspath(os.curdir)

## NEW NEW NEW
path_lstm_3d = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm'
path_lstm_5d = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm'
path_lstm_7d = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm'
path_lstm_trd = ROOT_DIR + '\\..\\..\\Datasets\\processed\\lstm\\trends\\5d'
path_class_trd = ROOT_DIR + '\\..\\..\\Datasets\\processed\\classification_10d\\3d\\trends'
path_class = ROOT_DIR + '\\..\\..\\Datasets\\processed\\classification_10d\\3d'

csvfiles_lstm_3d = glob.glob(path_lstm_3d + "/*.csv")
csvfiles_lstm_5d = glob.glob(path_lstm_5d + "/*.csv")
csvfiles_lstm_7d = glob.glob(path_lstm_7d + "/*.csv")
csvfiles_lstm_trd = glob.glob(path_lstm_trd + "/*.csv")
csvfiles_class_trd = glob.glob(path_class_trd + "/*.csv")
csvfiles_class = glob.glob(path_class + "/*.csv")

### LSTM Batch Run Scripts

# for a, file_lstm in enumerate(csvfiles_lstm_3d):
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":a, "my_seed":41291, "lstm_units":100, "no_epochs":120, "shuffle_bool":False, "trendpath":'//3d'})
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":a, "my_seed":41291, "lstm_units":100, "no_epochs":120, "shuffle_bool":False, "trendpath":'//3d'})
#     time.sleep(10)
# print(len(csvfiles_lstm_5d))
# print(len(csvfiles_lstm_trd))
#
# for b, file_lstm in enumerate(csvfiles_lstm_5d):
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":26118, "lstm_units":100, "no_epochs":180, "trendpath":'//5d'})
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":35352, "lstm_units":100, "no_epochs":180, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "dropout":0.4, "trendpath":'//7d'})
#
# #     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb',
# #                         parameters={"file_no": b, "my_seed": 41291, "lstm_units": 100, "no_epochs": 120,
# #                                     "shuffle_bool": True, "trendpath": '//5d'})
# #     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb',
# #                         parameters={"file_no": b, "my_seed": 41291, "lstm_units": 100, "no_epochs": 180,
# #                                     "shuffle_bool": True, "trendpath": '//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":120, "lstm_2_units":0, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":120, "lstm_2_units":50, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":120, "lstm_2_units":70, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":120, "lstm_2_units":100, "trendpath":'//5d'})
#     #
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":180, "lstm_2_units":0, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":180, "lstm_2_units":50, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":180, "lstm_2_units":70, "trendpath":'//5d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":b, "my_seed":41291, "lstm_units":100, "no_epochs":180, "lstm_2_units":100, "trendpath":'//5d'})
#     time.sleep(2)
#
#
#
# for d, file_lstm in enumerate(csvfiles_lstm_trd):
#     print(d)
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":d, "my_seed":26118, "lstm_units":100, "no_epochs":180, "lstm_2_units":0, "trendpath":'//trends//5d'})
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":d, "my_seed":35352, "lstm_units":100, "no_epochs":180, "lstm_2_units":0, "trendpath":'//trends//5d'})
#     time.sleep(2)

# for c, file_lstm in enumerate(csvfiles_lstm_7d):
# #     print(c)
# #     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb',
# #                         parameters={"file_no": c, "my_seed": 41291, "lstm_units": 70, "no_epochs": 120,
# #                                     "shuffle_bool": False, "trendpath": '//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb',
#     #                     parameters={"file_no": c, "my_seed": 41291, "lstm_units": 130, "no_epochs": 150,
#     #                                 "shuffle_bool": True, "trendpath": '//7d'})
#     pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "trendpath":'//7d'})    # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "dropout":0.4, "trendpath":'//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "dropout":0.6, "trendpath":'//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "lstm_2_units":0, "trendpath":'//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "lstm_2_units":50, "trendpath":'//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "lstm_2_units":70, "trendpath":'//7d'})
#     # pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":c, "my_seed":41291, "lstm_units":70, "no_epochs":120, "lstm_2_units":100, "trendpath":'//7d'})
#     time.sleep(5)

print(len(csvfiles_class))
print(len(csvfiles_class_trd))

for e, file_class_trd in enumerate(csvfiles_class_trd):
    print(e)
    pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":e, "my_seed":26118, "trendpath":'//trends'})
    pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":e, "my_seed":35352, "trendpath":'//trends'})
    time.sleep(2)

for f, file_class in enumerate(csvfiles_class):
    print(f)
    pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":f, "my_seed":26118, "trendpath":'//'})
    pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":f, "my_seed":35352, "trendpath":'//'})
    time.sleep(2)

### ANN Batch Run Scripts

# path_class = ROOT_DIR + '\\..\\..\\Datasets\\processed\\classification_10d'
# path_reg = ROOT_DIR + '\\..\\..\\Datasets\\processed\\regression_10d'
# csvfiles_class = glob.glob(path_class + "/*.csv")
# csvfiles_reg = glob.glob(path_reg + "/*.csv")
#
# for k, file_class in enumerate(csvfiles_class):
#     ##pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":150, "shuffle_bool":False})
#     ##pm.execute_notebook('lstmModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "lstm_units":100, "no_epochs":150, "shuffle_bool":True})
#     # pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "activation":'sigmoid'})
#     pm.execute_notebook('mlpModelClass.ipynb', 'out.ipynb', parameters = {"file_no":k, "my_seed":41291, "activation":'softmax'})
#     time.sleep(2)
#
# # for j, file_reg in enumerate(csvfiles_reg):
# #     pm.execute_notebook('mlpModelRegression.ipynb', 'out.ipynb', parameters = {"file_no":j, "my_seed":41291})
# #     time.sleep(10)
