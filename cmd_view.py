# coding=utf-8


def get_payment_date():
    return __input('Enter payment date [2017-03-11]: ')


def get_ocr():
    return __input('Post 20. Enter OCR: ')


def get_amount():
    return __input('Post 20. Enter amount [12,25]: ')


def get_payer_name_1():
    return __input('Poster 26. Enter payer name 1 [Svenska Mässan AB]. Enter to ignore: ')


def get_payer_name_2():
    return __input('Poster 26. Enter payer name 2 [c/o Svenska Mässan Stiftelse]. Enter to ignore: ')


def get_payer_address():
    return __input('Post 27. Enter payer address [Karpgatan 11]. Enter to ignore: ')


def get_payer_zip_code():
    return __input('Post 27. Enter payer zip code [593 40]. Enter to ignore: ')


def get_payer_city():
    return __input('Post 28. Enter payer city [Oskarshamn]. Enter to ignore: ')


def get_payer_country_code():
    return __input('Post 28. Enter payer country code [SE]. Enter to ignore: ')

def __input(label):
    return raw_input(label)
