import unittest


class AhoCorasickTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(Aho_Corasick("aabfc", {"ab", "ac", "bfc"}), {1, 2})
        self.assertEqual(Aho_Corasick("abcd", {"ab", "abc", "cd"}), {0, 0, 2})
        self.assertEqual(Aho_Corasick("aaabd", {"a", "aa", "abd"}), {0, 0, 1, 1, 2, 2})
        self.assertEqual(Aho_Corasick("abcd", {"abd", "dcd"}), {''})

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            Aho_Corasick(146, {{"ab", "ac", "bfc"}})
        # with self.assertRaises(ValueError):
        #     Aho_Corasick(5, 5)

if __name__ == '__main__':
    unittest.main()
