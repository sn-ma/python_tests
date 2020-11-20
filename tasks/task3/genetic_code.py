from collections import namedtuple
from os.path import realpath, dirname, join

AminoAcid = namedtuple("AminoAcid", "short_name single_letter mass")

AA_to_RNA = {}
RNA_to_AA = {}
single_letter_to_mass = {}


def __load():
    dir = dirname(realpath(__file__))
    fname = join(dir, "coding_table.tsv")
    with open(fname) as fin:
        start_codes, stop_codes = None, None
        for line in fin:
            line = line.strip()
            if line == "":
                continue
            name, codes, mass = line.split("\t", 3)
            codes = tuple(codes.split(", "))

            if name == "START":
                start_codes = codes
            elif name == "STOP":
                stop_codes = codes
            else:
                mass = float(mass)
                amino_acid = AminoAcid(*name.split("/", 2), mass)
                assert len(amino_acid.short_name) == 3
                assert len(amino_acid.single_letter) == 1

                AA_to_RNA[amino_acid] = codes
                single_letter_to_mass[amino_acid.single_letter] = mass
                for code in codes:
                    RNA_to_AA[code] = amino_acid
        return start_codes, stop_codes


start_codes, stop_codes = __load()
