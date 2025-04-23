import unittest
from src.utils.cleaning import (
    strip_yaml,
    remove_images,
    simplify_internal_links,
    extract_journal_content,
    clean_content,
    remove_date_like_headers
)


class TestCleaningFunctions(unittest.TestCase):

    def test_strip_yaml(self):
        text = "---\ntitle: Test\n---\n# Journal\nThis is content."
        expected = "# Journal\nThis is content."
        self.assertEqual(expected, strip_yaml(text))

        text = "---\ntitle: Test\n---"
        expected = ""
        self.assertEqual(expected, strip_yaml(text))

    def test_remove_images(self):
        text = "Here is an image ![alt](path/to/image.jpg)"
        expected = "Here is an image "
        actual = remove_images(text)
        self.assertEqual(expected, actual)

    def test_simplify_internal_links(self):
        text = "This links to [[My Note]] in the vault."
        expected = "This links to My Note in the vault."
        actual = simplify_internal_links(text)
        self.assertEqual(expected, actual)

    def test_extract_journal_content(self):
        text = "# Journal\nThis is my journal entry.\n# Done\nTask complete."
        expected = "This is my journal entry."
        actual = extract_journal_content(text)
        self.assertEqual(expected, actual)

    def test_extract_without_journal_content(self):
        text = "This is my journal entry.\nSecond line\nTask complete."
        expected = "This is my journal entry.\nSecond line\nTask complete."
        actual = extract_journal_content(text)
        self.assertEqual(expected, actual)

    def test_full_clean_content(self):
        text = (
            "---\ntitle: Entry\ndate: 2025-03-28\n---\n"
            "# What I want today\nEat healthy\n"
            "# Journal\nToday was a good day. [[Gratitude]] 🙏\n"
            "![image](pic.jpg)\n"
            "# New Resources\n- [Link](https://example.com)"
        )
        expected = "Today was a good day. Gratitude 🙏"
        cleaned = clean_content(text)
        self.assertEqual(expected, cleaned.strip())

    def test_remove_date_like_headers_basic(self):
        text = "# Dec 30 🟢🔴🟢x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_spaces(self):
        text = "# De# c#  # 30#  # 🟢🔴# 🟢# x# \nMore text here."
        expected = "More text here."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_no_symbols(self):
        text = "#Nov 01\nAnother line of text."
        expected = "Another line of text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_multiple_lines(self):
        text = "# Dec 30 🟢🔴🟢x\nThis is some text.\n# De# c#  # 30#  # 🟢🔴# 🟢# x# \nMore text here.\n#Nov 01\nAnother line of text."
        expected = "This is some text.\nMore text here.\nAnother line of text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_no_header(self):
        text = "This is some text.\nMore text here.\nAnother line of text."
        expected = "This is some text.\nMore text here.\nAnother line of text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_mixed_case_month(self):
        text = "#nOv 01\nAnother line of text."
        expected = "Another line of text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_single_digit_day(self):
        text = "# Dec 1 🟢🔴🟢x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_no_month(self):
        text = "# 1 🟢🔴🟢x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_invalid_header(self):
        text = "#Invalid header\nSome more text"
        expected = "#Invalid header\nSome more text"
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_hash_in_text(self):
        text = "This is a #hashtag\n# Dec 30 🟢🔴🟢x\nThis is some text."
        expected = "This is a #hashtag\nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_hash(self):
        text = "#\nThis is some text."
        expected = "#\nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_hash_and_spaces(self):
        text = "#   \nThis is some text."
        expected = "#   \nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_hash_and_symbol(self):
        text = "# x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month(self):
        text = "# Dec\nThis is some text."
        expected = "# Dec\nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_spaces(self):
        text = "# Dec  \nThis is some text."
        expected = "# Dec  \nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_symbol(self):
        text = "# 🟢\nThis is some text."
        expected = "# This some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_symbol_and_spaces(self):
        text = "#   \nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_day(self):
        text = "# 30\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_day_and_spaces(self):
        text = "#  30  \nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_day_and_symbol(self):
        text = "# 30 x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_day_and_symbol_and_spaces(self):
        text = "#  30  x  \nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_symbol(self):
        text = "# Dec x\nThis is some text."
        expected = "# Dec x\nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_symbol_and_spaces(self):
        text = "# Dec  x  \nThis is some text."
        expected = "# Dec  x  \nThis is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_day(self):
        text = "# Dec 30\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_day_and_spaces(self):
        text = "# Dec  30  \nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_day_and_symbol(self):
        text = "# Dec 30 x\nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_day_and_symbol_and_spaces(self):
        text = "# Dec  30  x  \nThis is some text."
        expected = "This is some text."
        self.assertEqual(expected, remove_date_like_headers(text))

    def test_remove_date_like_headers_with_only_month_and_day_and_multiple_symbols(self):
        text = "# Dec 30 🟢🔴🟢\nThis is some text."
        expected = "This is some text."


if __name__ == '__main__':
    unittest.main()
