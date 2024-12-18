import sys
sys.path.append(r"C:\Dev\py2")
import numpy as np
from model.features.format.base.FeatureBaseFormatter import FeatureBaseFormatter
from model.features.format.base.FeatureBaseFormatter import FormatType
#
# 無変換フォーマット
#
class DescConvFormatter(FeatureBaseFormatter):
    def __init__(self, name, options=None):
        super().__init__(name, FormatType.Desc, options)


    def doit(self):
        ret ={}
        ret[f'{self._prefix}'] = self._val
        return ret