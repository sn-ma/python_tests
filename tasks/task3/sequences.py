"""
Nucleotid masses is calculated as said in http://biotools.nubic.northwestern.edu/OligoCalc.html#helpMW
Amino Acid masses are taken from https://ru.webqc.org/aminoacids.php
"""

from abc import ABC, abstractmethod
from collections import Counter, Sequence, namedtuple
import random

from tasks.task3 import genetic_code


SequenceTypeMetadata = namedtuple("SequenceTypeMetadata", "alphabet sequence_type")


class RandomFactory:
    def __init__(self, sequence_class: type):
        assert issubclass(sequence_class, AbstractSequence)
        assert sequence_class is not AbstractSequence

        self.__sequence_class = sequence_class
        self.__metadata = sequence_class.metadata
        assert isinstance(self.__metadata, SequenceTypeMetadata)

    def letter(self):
        return random.choice(self.__metadata.alphabet)

    def sequence(self, length = 1000):
        seq = ''.join(self.letter() for _ in range(length))
        return self.__sequence_class(seq)

    def sequence_rand_len(self, min_len = 10, max_len = 1000):
        return self.sequence(random.randint(min_len, max_len))


class AbstractSequence(ABC, Sequence):
    metadata: SequenceTypeMetadata
    random_factory: RandomFactory

    def __init__(self, metadata: SequenceTypeMetadata, sequence, ):
        assert all(ch in metadata.alphabet for ch in sequence)

        self.__metadata = metadata
        self.__sequence = sequence

    @property
    def alphabet(self):
        return self.__metadata.alphabet

    @property
    def seq_type(self):
        return self.__metadata.sequence_type

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
        return "{}({})".format(self.__metadata.sequence_type, self.__sequence)

    def __eq__(self, other):
        if not isinstance(other, AbstractSequence):
            return False
        return self.__metadata == other.__metadata \
                and self.__sequence == other.__sequence


class DNA(AbstractSequence):
    metadata = SequenceTypeMetadata("ACGT", "DNA")

    def __init__(self, sequence):
        super(DNA, self).__init__(
            DNA.metadata,
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
    metadata = SequenceTypeMetadata("ACGU", "RNA")

    def __init__(self, sequence):
        super(RNA, self).__init__(
            RNA.metadata,
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
    metadata = SequenceTypeMetadata([aa.single_letter for aa in genetic_code.AA_to_RNA.keys()], "Protein")

    def __init__(self, sequence):
        super(Protein, self).__init__(
            metadata = Protein.metadata,
            sequence = sequence
        )

    def mass(self):
        return sum(genetic_code.single_letter_to_mass[aa] for aa in self)


DNA.random_factory = RandomFactory(DNA)
RNA.random_factory = RandomFactory(RNA)
Protein.random_factory = RandomFactory(Protein)
