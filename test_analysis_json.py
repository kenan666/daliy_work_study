# test analysis json file 

import json
import pandas as pd

with open("./test_file1/test_read_json2.json",'r') as json_date:
    load_dict = json.load(json_date)
    
    load_dict = load_dict['mainData'] #拆第一层花括号
    data_raw = pd.DataFrame(columns=load_dict.keys())
    data_raw = data_raw.append(load_dict,ignore_index=True)

data_raw