import cmd_view
import bgmax_generator
import file_handler


def main():
    date = cmd_view.get_payment_date()
    file_content = bgmax_generator.create_start_post(date)
    file_content += bgmax_generator.create_opening_post()
    ocr = cmd_view.get_ocr()
    amount = cmd_view.get_amount()
    file_content += bgmax_generator.create_payment_post(ocr, amount)
    file_content += bgmax_generator.create_deposit_post(date, amount, 1)

    payer_name_1 = cmd_view.get_payer_name_1()
    payer_name_2 = cmd_view.get_payer_name_2()
    if payer_name_1:
        file_content += bgmax_generator.create_name_post(payer_name_1, payer_name_2)

    address = cmd_view.get_payer_address()
    zip_code = cmd_view.get_payer_zip_code()
    if address or zip_code:
        file_content += bgmax_generator.create_payer_address_post(address, zip_code)

    city = cmd_view.get_payer_city()
    country_code = cmd_view.get_payer_country_code()
    if city or country_code:
        file_content += bgmax_generator.create_payer_address_post_2(city, '', country_code)

    file_handler.create_file(file_content)


if __name__ == '__main__':
    main()
