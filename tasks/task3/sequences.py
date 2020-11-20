"""
Nucleotid masses is calculated as said in http://biotools.nubic.northwestern.edu/OligoCalc.html#helpMW
Amino Acid masses are taken from https://ru.webqc.org/aminoacids.php
"""

from abc import ABC, abstractmethod
from collections import Counter

from tasks.task3 import genetic_code


class AbstractSequence(ABC):
    def __init__(self, alphabet, seq_type, sequence, ):
        assert all(ch in alphabet for ch in sequence)

        self.__alphabet = alphabet
        self.__seq_type = seq_type
        self.__sequence = sequence

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def seq_type(self):
        return self.__seq_type

    @property
    def sequence(self):
        return self.__sequence

    @property
    def length(self):
        return len(self.__sequence)

    def __len__(self):
        return self.length

    def __iter__(self):
        for ch in self.__sequence:
            yield ch

    def get_stat(self):
        return Counter(self.__sequence)

    @abstractmethod
    def mass(self):
        pass

    def __repr__(self):
        return "{}({})".format(self.__seq_type, self.__sequence)

    def __eq__(self, other):
        if not isinstance(other, AbstractSequence):
            return False
        return self.__alphabet == other.__alphabet \
                and self.__sequence == other.__sequence \
                and self.__seq_type == other.__seq_type


class DNA(AbstractSequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(
            alphabet = "ACGT",
            seq_type = "DNA",
            sequence = sequence
        )

    __masses = {"A": 313.21, "T": 304.2, "C": 289.18, "G": 329.21}
    __complement = {"A": "T", "G": "C", "T": "A", "C": "G"}
    __complement_to_rna = {"A": "U", "G": "C", "T": "A", "C": "G"}

    def mass(self):
        return sum(DNA.__masses[b] for b in self) - 61.96

    def revc(self):
        complement = [DNA.__complement[b] for b in self]
        return DNA("".join(reversed(complement)))

    def transcription(self):
        complement = [DNA.__complement_to_rna[b] for b in self]
        return RNA("".join(reversed(complement)))


class RNA(AbstractSequence):
    def __init__(self, sequence):
        super(RNA, self).__init__(
            alphabet = "ACGU",
            seq_type = "RNA",
            sequence = sequence
        )

    __masses = {"A": 329.21, "U": 306.17, "C": 305.18, "G": 345.21}
    __complement = {"A": "U", "G": "C", "U": "A", "C": "G"}

    def mass(self):
        return sum(RNA.__masses[b] for b in self) + 159.0

    def revc(self):
        complement = [RNA.__complement[b] for b in self]
        return RNA("".join(reversed(complement)))

    def translation(self):
        for start_pos in range(len(self) - 2):
            if self.sequence[start_pos:start_pos + 3] in genetic_code.start_codes:
                break
        else:
            raise TranslationException("Start code not found")
        def tripletes():
            left = start_pos
            while True:
                right = left + 3
                if right > len(self):
                    raise TranslationException("Stop code not found")
                triplet = self.sequence[left:right]
                if triplet in genetic_code.stop_codes:
                    return
                yield triplet
                left = right
        protein_sequence = (genetic_code.RNA_to_AA[tr].single_letter for tr in tripletes())
        return Protein(''.join(protein_sequence))


class TranslationException(Exception):
    def __init__(self, message):
        super(TranslationException, self).__init__(message)


class Protein(AbstractSequence):
    def __init__(self, sequence):
        alphabet = set(aa.single_letter for aa in genetic_code.AA_to_RNA.keys() if isinstance(aa, genetic_code.AminoAcid))
        super(Protein, self).__init__(
            alphabet = alphabet,
            seq_type = "Protein",
            sequence = sequence
        )

    def mass(self):
        return sum(genetic_code.single_letter_to_mass[aa] for aa in self)


if __name__ == '__main__':
    print(RNA("AACUGAUGAAAUUUCCCUGA").translation().mass())
    # print(Protein("").alphabet)
