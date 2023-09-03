
class Utils:
    def assert_list_items_text(self, list_name, value):

        count = 1
        for stop in list_name:
            print("Type of flight is:", stop.text)
            assert stop.text == value
            print("(Test", count, "of", len(list_name), ") Passed!")
            count += 1

        def sendText(self, text):
            self.element.clear()
            self.element.send_keys(text)


