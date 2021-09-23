import codewars_test as test
from solution import two_sort


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]),
                           'b***i***t***c***o***i***n')
        test.assert_equals(two_sort(
            ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]),
                           'a***r***e')
        test.assert_equals(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]),
                           'a***b***o***u***t')
        test.assert_equals(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]),
                           'c***o***d***e')
        test.assert_equals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]),
                           'L***e***t***s')


@test.describe("Random Tests")
def random_tests():
    import random

    def _solution(a):
        return "***".join(list(sorted(a)[0]))

    options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for _ in range(100):
        s = ["".join([random.choice(options) for i in range(random.randint(3, 8))]) for j in
             range(random.randint(5, 10))]
        expected = _solution(s)

        @test.it(f"testing for stwo_sort({s})")
        def test_case():
            test.assert_equals(two_sort(s[:]), expected)
