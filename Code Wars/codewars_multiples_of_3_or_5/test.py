# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


import codewars_test as test
from solution import solution


@test.describe("Sample tests")
def sample_tests():
    @test.it("Should return 3 for n=4")
    def _():
        test.assert_equals(solution(4), 3)

    @test.it("Should return 8 for n=6")
    def _():
        test.assert_equals(solution(6), 8)

    @test.it("Should return 60 for n=16")
    def _():
        test.assert_equals(solution(16), 60)

    @test.it("Should return 0 for n=3")
    def _():
        test.assert_equals(solution(3), 0)

    @test.it("Should return 3 for n=5")
    def _():
        test.assert_equals(solution(5), 3)

    @test.it("Should return 45 for n=15")
    def _():
        test.assert_equals(solution(15), 45)

    @test.it("Should return 0 for n=0")
    def _():
        test.assert_equals(solution(0), 0)

    @test.it("Should return 0 for n=-1")
    def _():
        test.assert_equals(solution(-1), 0)

    @test.it("Should return 23 for n=10")
    def _():
        test.assert_equals(solution(10), 23)

    @test.it("Should return 78 for n=20")
    def _():
        test.assert_equals(solution(20), 78)

    @test.it("Should return 9168 for n=200")
    def _():
        test.assert_equals(solution(200), 9168)
