import os
import unittest
from types import GeneratorType

from tasks.task3.sequences import DNA
from tasks.task6.fasta_reader import read_fasta


class TestFastaReader(unittest.TestCase):
    def test_fasta_reader(self):
        path = os.path.dirname(os.path.realpath(__file__))
        gen = read_fasta(os.path.join(path, "file.fasta"), DNA)
        self.assertTrue(isinstance(gen, GeneratorType))
        sequences = list(gen)
        self.assertEqual(2, len(sequences))
        self.assertEqual([
            DNA("GATTACA"),
            DNA("GGAATTTTAACCAA"),
        ], sequences)
        self.assertEqual([
            "Gattaca code",
            "Multiline sequence"
        ], [e.name for e in sequences])


if __name__ == '__main__':
    unittest.main()
