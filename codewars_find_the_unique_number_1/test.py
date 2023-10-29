# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


try:
    import codewars_test as test
except:
    pass


@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)