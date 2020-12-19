import os
import unittest
from io import StringIO

from tasks.task3.sequences import DNA
from tasks.task6.fasta_print_stats import fasta_print_stats


class TestFastaPrintStats(unittest.TestCase):
    def test_fasta_print_stats(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "file.fasta")
        buf = StringIO()
        fasta_print_stats(path, DNA, buf)

        self.assertEqual(
"""Name                 Length A    C    G    T   
--------------------------------------------------
Gattaca code              7    3    1    1    2
Multiline sequence       14    6    2    2    4
""", buf.getvalue())


if __name__ == '__main__':
    unittest.main()
