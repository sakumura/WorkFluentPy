#! Python3
# text_cleaner.py - テキストの空白スペースや改行などを取り除く。

import re

def purge(text:str):
    """ 空白スペースと改行を取り除きます。 """
    text = re.sub(r'[\r\n\s　]+', '', text)
    return text.strip()

def purge_line(text:str):
    """ 改行を取り除きます。 """
    text = re.sub(r'[\r\n]+', '', text)
    return text.strip()

def em_space_purge(text:str):
    """ 文字列（text）内の全角空白スペースを取り除きます。 """
    return re.sub(r'[\u3000　]+', '', text)

def em_space_to_space(text:str):
    """ 文字列（text）内の全角空白スペースを半角空白スペースに置き換えます。 """
    return re.sub(r'[\u3000　]+', ' ', text)

def around_purge(text:str):
    """ 前後の空白スペースと改行を取り除きます。 """
    return text.strip()

def kabu(text:str):
    """ （株）を株式会社に、（有）を有限会社に変更します。 """
    text = text.replace('（株）', '株式会社')
    text = text.replace('(株)', '株式会社')
    text = text.replace('㈱', '株式会社')
    text = text.replace('（有）', '有限会社')
    text = text.replace('(有)', '有限会社')
    text = text.replace('㈲', '有限会社')
    return text

if __name__ == '__main__':
    # Testing
    text = 'ABCD-ABCD-ABCD\n'
    print(purge(text))  # Should return: 'ABCD-ABCD-ABCD'

    text = '  本日は \n  晴天なり  \n'
    print(around_purge(text))  # Should return: '本日は \n  晴天なり'
