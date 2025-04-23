import unittest

from src.analysis import analyze_entries


# from analysis import analyze_entries

class MyTestCase(unittest.TestCase):
    def test_analyze_simple_entry(self):
        entries = [
            {
                "content": "Today I felt really calm and grateful. #grateful\nWhy do I still feel tired?\nStillness matters. Stillness heals.",
                "path": "mock/path1.md",
                "modified": None
            },
            {
                "content": "I had the best day ever. Everything went well and I feel fantastic! #joy",
                "path": "mock/path2.md",
                "modified": None
            },
            {
                "content": "This was a terrible day. I felt awful and everything went wrong. I hate this day. It was the worst day ever. #frustrated",
                "path": "mock/path3.md",
                "modified": None
            }
        ]
        result = analyze_entries(entries)
        print(result)

        # Check common word extraction
        common_words = [word for word, _ in result['most_common_words']]
        self.assertIn("stillness", common_words)

        # Check tag extraction
        tags = [tag for tag, _ in result['tags']]
        self.assertIn("grateful", tags)

        # Check the question count
        self.assertEqual(result['questions_count'], 1)

        # Check average length
        self.assertGreater(result['average_length'], 5)

        # Check tone summary
        self.assertIn("positive", result['tone_summary'])
        # self.assertIn("neutral", result['tone_summary'])
        self.assertIn("negative", result['tone_summary'])

if __name__ == '__main__':
    unittest.main()
