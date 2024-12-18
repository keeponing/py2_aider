import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
from model.features.format.base.FeatureBaseFormatter import FeatureBaseFormatter
from model.features.format.base.FeatureBaseFormatter import FormatType
from sklearn.preprocessing import LabelEncoder
from collections import OrderedDict

# ワンホットフォーマット
#
class LabelConvFormatter(FeatureBaseFormatter):
    _le = LabelEncoder()
    _is_reshape = True
    def __init__(self, prefix, options, is_reshape=True):
        self._is_reshape = is_reshape
        options2 = None
        if(self._is_reshape==True):
            try:
                options2 = np.array(options).reshape(-1, 1).astype('int32')
            except :
                options2 = np.array(options)
            finally:
                options = options2
        super().__init__(prefix, FormatType.LabelE, options)

    def doit(self):
        target_val = self._val

        if(self._is_reshape==True):
            
            try:
                target_val2 = np.array(target_val).reshape(-1, 1).astype('int32')
            except :
                target_val2 = np.array(target_val).reshape(-1, 1)
            finally:
                target_val3 = target_val2
        self._le.fit(self._options)
        val = self._le.transform(target_val3)
        ret = OrderedDict()
        ret[f'{self._prefix}'] = val[0].astype('int32')
        return ret