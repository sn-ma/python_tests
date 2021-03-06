"""
Nucleotid masses is calculated as said in http://biotools.nubic.northwestern.edu/OligoCalc.html#helpMW
Amino Acid masses are taken from https://ru.webqc.org/aminoacids.php
"""

import random
from abc import ABC, abstractmethod
from collections import Counter, namedtuple
from collections.abc import Sequence
from functools import lru_cache

from tasks.task3 import genetic_code


SequenceTypeMetadata = namedtuple("SequenceTypeMetadata", "alphabet sequence_type")


class RandomFactory:
    def __init__(self, sequence_class: type):
        assert issubclass(sequence_class, AbstractSequence)
        assert sequence_class is not AbstractSequence

        self.__sequence_class = sequence_class
        self.__alphabet = sequence_class.metadata().alphabet
        self.__seq_type = sequence_class.metadata().sequence_type
        self.__count = 0

    def letter(self):
        return random.choice(self.__alphabet)

    def sequence(self, length = 1000):
        seq = ''.join(random.choices(self.__alphabet, k = length))
        self.__count += 1
        return self.__sequence_class(seq, "Random {} #{}".format(self.__seq_type, self.__count))

    def sequence_rand_len(self, min_len = 10, max_len = 1000):
        return self.sequence(random.randint(min_len, max_len))

    def gen_letters(self):
        while True:
            yield self.letter()

    def gen_sequences_fix_len(self, length = 1000):
        while True:
            yield self.sequence(length)

    def gen_sequences_rand_len(self, min_len = 10, max_len = 1000):
        while True:
            yield self.sequence_rand_len(min_len, max_len)


class AbstractSequence(ABC, Sequence):
    """
    Warning: equality only checks same type and same sequence, names are ignored!

    Note: to implement a concrete sequence class, you should override class field _metadata and method mass(self)
    """
    def __init__(self, sequence: str, name: str = None):
        assert all(ch in self.metadata().alphabet for ch in sequence)

        self.__sequence = sequence
        self.__name = name if name else "Unknown " + self.seq_type

    _metadata: SequenceTypeMetadata

    @classmethod
    def metadata(cls) -> SequenceTypeMetadata:
        return cls._metadata

    @classmethod
    @lru_cache(maxsize = None)
    def random_factory(cls):
        return RandomFactory(cls)

    @property
    def alphabet(self):
        return self.metadata().alphabet

    @property
    def seq_type(self):
        return self.metadata().sequence_type

    @property
    def name(self):
        return self.__name

    @property
    def sequence(self):
        return self.__sequence

    @property
    def length(self):
        return len(self.__sequence)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return self.__sequence[key]

    def get_stat(self):
        return Counter(self.__sequence)

    @abstractmethod
    def mass(self):
        pass

    def __repr__(self):
        return "{} \"{}\" ({})".format(self.metadata().sequence_type, self.__name, self.__sequence)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.__sequence == other.__sequence

    def __hash__(self):
        return hash(self.__sequence)

    def map(self, foo):
        return type(self)(''.join(map(foo, self)))

    def map2(self, foo):
        def prev_letter():
            yield None
            for letter in self:
                yield letter
        return type(self)(''.join(map(foo, prev_letter(), self)))


class DNA(AbstractSequence):
    _metadata = SequenceTypeMetadata("ACGT", "DNA")

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
    _metadata = SequenceTypeMetadata("ACGU", "RNA")

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

        def triplets():
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
        protein_sequence = (genetic_code.RNA_to_AA[tr].single_letter for tr in triplets())
        return Protein(''.join(protein_sequence))


class TranslationException(Exception):
    def __init__(self, message):
        super(TranslationException, self).__init__(message)


class Protein(AbstractSequence):
    _metadata = SequenceTypeMetadata([aa.single_letter for aa in genetic_code.AA_to_RNA.keys()], "Protein")

    def mass(self):
        return sum(genetic_code.single_letter_to_mass[aa] for aa in self)
