
from enum import Enum
from abc import ABC, abstractmethod

#
# ChatTypeタイプ
#
class FormatType(Enum):
    Desc = 0 # description
    NoConv = 1  # そのまま
    ToInt = 2   # 整数変換
    ToFloat = 3 # フロート変換
    OnehotE = 4  # ワンホットエンコーディング
    LabelE = 5 # ラベルエンコーディング

    
#
#   特徴量フォーマットクラス
#    
class FeatureBaseFormatter(ABC):
    _prefix = ""
    _format_type = FormatType.NoConv
    _options = None
    _val = None
    
    def __init__(self, prefix, format_type, options):
        self._prefix = prefix
        self._format_type = format_type
        self._options = options
    @property
    def val(self):
        return self._val
    
    @val.setter
    def val(self, val):
        self._val = val
    
    def clear_val(self):
        self._val = None
            
    @abstractmethod
    def doit(self):
        pass
    
    
