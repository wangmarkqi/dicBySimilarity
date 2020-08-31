Python dictionary, but the keys are recognized by text similarity ratio!
======================================================
### Description:
Python dictionary, but the keys are recognized by text similarity ratio.

## Dependencies:
Python-Levenshtein must be pre-installed and python3 is required.  
If you have difficulty on installing Levenshtein, go to [Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/) for wheel package,download whl file and pip install file name.

## Install:    
pip install dicBySimilarity

### Tutorial:
**Usage is simple:**
- step1: tell converter where your data is: 
`from dicBySimilarity import SimiDic`    
`sdic=SimiDic(threshold=0.90)`  
Threshold  is the ration above which you want the SimiDic return value by key, otherwise will return None`
- step2: use sdic as normal python dictionary object. If the text similarity between sdic key1 when write into sdic and sdic key2 when read out data is above threshold value, the sdic return value, else return None.     
`sdic[key1]=value #write into key and value`   
`value,ratio=sdic[key2] #read data from sdic when similarity between key1 and key2 above threshold else None,return value and ratio`   

