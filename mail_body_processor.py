#! Python3
# mail_body_processor.py - メールの本文を処理する。

import re
import text_cleaner

def process_mail_body(mail, column_num, special_sentence):
    SEPARATOR = '■'
    REPLACEMENT_REGEXS = [r'【', r'】']
    NAME_KEY = 'お名前'
    COMPANY_KEY = '貴社名'

    body = mail['body']

    # Replace and split the body
    for regex in REPLACEMENT_REGEXS + [special_sentence]:
        ro = re.compile(regex)
        body = ro.sub(SEPARATOR, body)
    body = body.split(SEPARATOR)

    # Create columns and dictionary
    body_dict = {}
    count = 0
    for i in range(len(body)):
        if body[i].replace('\n', '') == '':  # Skip empty strings
            continue
        if count % 2 == 0:
            body_dict[body[i]] = body[i+1]
        count += 1
        if count == column_num * 2:
            break

    # Text cleaning
    for k, v in body_dict.items():
        if NAME_KEY in k:
            v = text_cleaner.around_purge(text_cleaner.em_space_to_space(v))
        elif COMPANY_KEY in k:
            v = text_cleaner.kabu(text_cleaner.purge(v))
        else:
            v = text_cleaner.around_purge(v)
        body_dict[k] = v

    return body_dict


if __name__ == "__main__":
    mail = {
        'body': '【お名前】貴社太郎\n【貴社名】貴社\n【弊社製品・サービス等について、将来弊社からご連絡を差し上げてもよろしいですか。】\nはい\n\n----'
    }
    column_num = 3
    special_sentence = '----'
    processed_mail = process_mail_body(mail, column_num, special_sentence)
    print(processed_mail)
