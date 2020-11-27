import collections
import unittest

from tasks.task3.sequences import DNA, RNA, Protein


class TestSequences(unittest.TestCase):
    def test_dna(self):
        dna = DNA("GATTACA")
        self.assertEqual(set("ACGT"), set(dna.alphabet))
        self.assertEqual("DNA", dna.seq_type)
        self.assertEqual("GATTACA", dna.sequence)
        self.assertEqual(7, dna.length)
        self.assertEqual(dict(G = 1, A = 3, T = 2, C = 1), dna.get_stat())
        self.assertEqual(2104.46, dna.mass())
        self.assertEqual(dna, DNA("GATTACA"))
        self.assertFalse(dna == DNA("GAT"))
        self.assertEqual(DNA("TGTAATC"), dna.revc())
        self.assertEqual(RNA("UGUAAUC"), dna.transcription())

    def test_rna(self):
        rna = RNA("GAUUACA")
        self.assertEqual(set("ACUG"), set(rna.alphabet))
        self.assertEqual("RNA", rna.seq_type)
        self.assertEqual("GAUUACA", rna.sequence)
        self.assertEqual(7, rna.length)
        self.assertEqual(dict(G = 1, A = 3, U = 2, C = 1), rna.get_stat())
        self.assertEqual(2409.36, rna.mass())

    def test_translation(self):
        self.assertEqual(Protein("MAY"), RNA("AUG" + "GCU" + "UAC" + "UAA").translation())

    def test_protein(self):
        protein = Protein("MAY")
        self.assertEqual(149.2124 + 89.0935 + 181.1894, protein.mass())
        self.assertEqual(3, protein.length)
        self.assertEqual(dict(M = 1, A = 1, Y = 1), protein.get_stat())
        self.assertEqual("MAY", protein.sequence)
        self.assertEqual("Protein", protein.seq_type)
        self.assertEqual(20, len(protein.alphabet))

    def test_sequence(self):
        dna = DNA("GATTACA")
        self.assertTrue(all(n in dna for n in "ACGT"))
        self.assertEqual(list("ACATTAG"), list(reversed(dna)))
        self.assertTrue(isinstance(dna, collections.Sequence))

    def test_random_letter(self):
        for cls in (DNA, RNA, Protein):
            self.assertTrue(all(cls.random_factory.letter() in set(cls.metadata.alphabet) for _ in range(1000)))

    def test_random_sequence(self):
        dna = DNA.random_factory.sequence()
        self.assertTrue(isinstance(dna, DNA))
        self.assertEqual(1000, len(dna))

    def test_random_sequence_rand_len(self):
        for _ in range(100):
            dna = DNA.random_factory.sequence_rand_len()
            self.assertTrue(isinstance(dna, DNA))
            self.assertTrue(10 <= len(dna) <= 1000)


if __name__ == "__main__":
    unittest.main()
