import cmd_view
import bgmax_generator
import file_handler


def main():
    date = '2017-03-11'
    file_content = bgmax_generator.create_start_post(date)
    file_content += bgmax_generator.create_opening_post()
    ocr = cmd_view.get_ocr()
    amount = cmd_view.get_amount()
    file_content += bgmax_generator.create_payment_post(ocr, amount)
    file_content += bgmax_generator.create_deposit_post(date, amount, 1)
    file_handler.create_file(file_content)


if __name__ == '__main__':
    main()
