from test import TestCase, editor, ROOT


class ReferenceTest(TestCase):

    def test_references_search(self):
        """Jedi must find all references to object."""

        response = editor(
            'test/jedi_reference/fixtures/simple.py', 1, 4,
            'reference')

        expected = {
            ROOT + 'test/jedi_reference/fixtures/simple.py:4 - a@4,4': {
                'module_path': ROOT + 'test/jedi_reference/fixtures/simple.py',
                'line': 4,
                'column': 4,
                'description': 'a@4,4'
            },
            ROOT + 'test/jedi_reference/fixtures/simple.py:5 - a@5,4': {
                'module_path': ROOT + 'test/jedi_reference/fixtures/simple.py',
                'line': 5,
                'column': 4,
                'description': 'a@5,4'
            }
        }

        self.assertEqual(response, expected)

    def test_empty_references(self):
        """Strip unknown references."""

        response = editor(
            'test/jedi_reference/fixtures/useless.py', 1, 4,
            'reference')

        self.assertIsNone(response)
