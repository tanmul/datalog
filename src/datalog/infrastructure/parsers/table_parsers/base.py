from tokenizers.base import Tokenizer

class BaseTableParser:

    def parse(sql : str, tokenizer : Tokenizer):
        tokens = tokenizer.tokenize(sql)