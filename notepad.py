import unittest
import time
from appium import webdriver

class SimpleNotepadTests(unittest.TestCase):

    def setUp(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "Notepad.exe"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities= desired_caps)

    def tearDown(self):
        self.driver.quit()

    #def test_initialize(self):
    #    #Make sure we're in standard mode
    #    result = self.driver.find_element_by_xpath("//Window/TitleBar[starts-with(@Name, \"Untitled - Notepad\")]");
    #    self.assertEqual(str(result.text),"Untitled - Notepad")

    def test_addition(self):
        textData=["1. Write Some python","2. Run it with Appium","3. ???","4. PROFIT!"]
        el2 = self.driver.find_element_by_xpath("/Window/Edit")
        el2.click()
        for item in textData:
            el2.send_keys(item+"\n")
        time.sleep(2)
        el2.clear()
        #self.driver.SendKeys("1. Write Script\\r\\n")
        #result = self.driver.find_element_by_name("text editor")
        #self.assertEqual(str(result.text), "1.Write Script")

    #def test_combination(self):
    #    self.driver.find_element_by_name("Seven").click()
    #    self.driver.find_element_by_name("Multiply by").click()
    #    self.driver.find_element_by_name("Nine").click()
    #    self.driver.find_element_by_name("Plus").click()
    #    self.driver.find_element_by_name("One").click()
    #    self.driver.find_element_by_name("Equals").click()
    #    self.driver.find_element_by_name("Divide by").click()
    #    self.driver.find_element_by_name("Eight").click()
    #    self.driver.find_element_by_name("Equals").click()

    #    result = self.driver.find_element_by_accessibility_id("CalculatorResults")
    #    self.assertEqual(str(result.text), "Display is 8")

    #def test_division(self):
    #    self.driver.find_element_by_name("Eight").click()
    #    self.driver.find_element_by_name("Eight").click()
    #    self.driver.find_element_by_name("Divide by").click()
    #    self.driver.find_element_by_name("One").click()
    #    self.driver.find_element_by_name("One").click()
    #    self.driver.find_element_by_name("Equals").click()

    #    result = self.driver.find_element_by_accessibility_id("CalculatorResults")
    #    self.assertEqual(str(result.text), "Display is 8")

    #def test_multiplication(self):
    #    self.driver.find_element_by_name("Nine").click()
    #    self.driver.find_element_by_name("Multiply by").click()
    #    self.driver.find_element_by_name("Nine").click()
    #    self.driver.find_element_by_name("Equals").click()

    #    result = self.driver.find_element_by_accessibility_id("CalculatorResults")
    #    self.assertEqual(str(result.text), "Display is 81")

    #def test_subtraction(self):
    #    self.driver.find_element_by_name("Nine").click()
    #    self.driver.find_element_by_name("Minus").click()
    #    self.driver.find_element_by_name("One").click()
    #    self.driver.find_element_by_name("Equals").click()

    #    result = self.driver.find_element_by_accessibility_id("CalculatorResults")
    #    self.assertEqual(str(result.text), "Display is 8")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleNotepadTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
