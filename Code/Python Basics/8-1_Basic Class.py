# basic class
class GameClass:
    test_var = "Hello"

    def test_func(self):
        print("function in GameClass.")
        print(f"The varibale inside the class named test_var contains {self.test_var}")
        self.another_test_func(123456)

    def another_test_func(self, test_param):
        print(test_param)

# create an instance of the class
test = GameClass()
print(test.test_var)
test.test_var = "new values"
print(test.test_var)

test2 = GameClass()
print(test2.test_var)
test2.test_var = "another values"
print(test2.test_var)

test2.test_func()
test2.another_test_func("TEST")