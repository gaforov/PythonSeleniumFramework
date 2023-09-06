import inspect
import logging


class Utils:
    def assert_list_items_text(self, list_name, value):
        count = 1
        for stop in list_name:
            print("Type of flight is:", stop.text)
            assert stop.text == value
            print("(Test", count, "of", len(list_name), ") Passed!")
            count += 1

    def test_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        handler = logging.FileHandler("automation.log", mode="w")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def read_data_from_excel_file(self, file_name):
        wb = load_workbook(filename='demo_excel.xlsx')
