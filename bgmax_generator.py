
def create_start_post(date):
    date = __clean_date(date)
    date += '161001000001'  # adding "random" time
    start_post = '01' + 'BGMAX               ' + '01' + date + 'T' + '                                   '
    return __create_post(start_post)


def create_opening_post():
    receiver_bg_number = '0005566922'
    opening_post = '05' + receiver_bg_number + '          ' + 'SEK' + '                                                       '
    return __create_post(opening_post)


def create_payment_post(ocr, payment_amount):
    ocr_content = ocr.rjust(25, ' ')
    payment_post = '20' + '          ' + ocr_content + __clean_payment(payment_amount) + '2' + '1' + '590180253011' + '0' + '          '
    return __create_post(payment_post)


def create_deposit_post(date, payment_amount, number_of_payments):
    number_of_payments_content = str(number_of_payments).rjust(8, '0')
    # + '        '
    deposit_post = '15' + '00000000000000000000000000000000000' + __clean_date(date) + '00000' + __clean_payment(payment_amount) + 'SEK' + number_of_payments_content + ' '
    return __create_post(deposit_post)


def __clean_payment(payment_amount):
    payment_amount = payment_amount.replace(',', '')
    payment_amount_content = payment_amount.rjust(18, '0')
    return payment_amount_content


def __clean_date(date):
    return date.replace('-', '')


def __create_post(post_string):
    return post_string + '\n'
