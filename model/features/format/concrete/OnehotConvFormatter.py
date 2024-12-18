import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
from model.features.format.base.FeatureBaseFormatter import FeatureBaseFormatter
from model.features.format.base.FeatureBaseFormatter import FormatType
from sklearn.preprocessing import OneHotEncoder
from collections import OrderedDict

# ワンホットフォーマット
#
class OnehotConvFormatter(FeatureBaseFormatter):
    _oe = OneHotEncoder( sparse_output= False, handle_unknown='ignore')
    _is_reshape = True
    def __init__(self, prefix, options, is_reshape=True):
        self._is_reshape = is_reshape
        if(self._is_reshape==True):
            options = np.array(options).reshape(-1, 1).astype('int32')
        super().__init__(prefix, FormatType.OnehotE, options)

    def doit(self):
        target_val = self._val

        if(self._is_reshape==True):
            target_val = np.array(target_val).reshape(-1, 1).astype('int32')
        self._oe.fit(self._options)
        trans = self._oe.transform(target_val)
        ret = OrderedDict()
        onehot = trans.astype('int32')
        arr = onehot[0]
        for index, val in enumerate(arr):
            ret[f'{self._prefix}_{index}'] = val.astype('int32')
        # if(1 < len(ret)):
        #     ret.popitem(last=False)
   
        return ret