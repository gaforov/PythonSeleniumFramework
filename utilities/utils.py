
class Utils:
    def assert_list_items_text(self, list_name, value):

        number = 1
        for stop in list_name:
            print("Type of flight is:", stop.text)
            assert stop.text == value
            print("(Test", number, "of", len(list_name), ") Passed!")
            number += 1

