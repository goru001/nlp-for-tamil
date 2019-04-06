from fastai.text import *
import sentencepiece as spm
from pathlib import Path

path = Path(__file__).parent.parent

class TamilTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        model_path = path/f'tamil_spm_8k.model'
        self.sp.Load(str(model_path))
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)