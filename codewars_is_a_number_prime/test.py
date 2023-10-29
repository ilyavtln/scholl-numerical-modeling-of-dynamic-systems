# codewars_test can be installed from https://github.com/codewars/python-test-framework
# run "pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test"


import codewars_test as test
@test.describe("Basic")
def basic():
    
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(is_prime(0),  False, "0  is not prime")
        test.assert_equals(is_prime(1),  False, "1  is not prime")
        test.assert_equals(is_prime(2),  True, "2  is prime")
        test.assert_equals(is_prime(73), True, "73 is prime")
        test.assert_equals(is_prime(75), False, "75 is not prime")
        test.assert_equals(is_prime(-1), False, "-1 is not prime")

    
    @test.it("Test prime")
    def test_prime():
        test.assert_equals(is_prime(3),  True, "3  is prime");
        test.assert_equals(is_prime(5),  True, "5  is prime");
        test.assert_equals(is_prime(7),  True, "7  is prime");
        test.assert_equals(is_prime(41), True, "41 is prime");
        test.assert_equals(is_prime(5099), True, "5099 is prime");
        
    @test.it("Test not prime")
    def test_not_prime():
        test.assert_equals(is_prime(4),  False, "4  is not prime");
        test.assert_equals(is_prime(6),  False, "6  is not prime");
        test.assert_equals(is_prime(8),  False, "8  is not prime");
        test.assert_equals(is_prime(9), False, "9 is not prime");
        test.assert_equals(is_prime(45), False, "45 is not prime");
        test.assert_equals(is_prime(-5), False, "-5 is not prime");
        test.assert_equals(is_prime(-8), False, "-8 is not prime");
        test.assert_equals(is_prime(-41), False, "-41 is not prime");
