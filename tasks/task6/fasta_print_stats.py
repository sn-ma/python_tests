from sys import stdout

from tasks.task6.fasta_reader import read_fasta


def fasta_print_stats(fname, SequenceType, file = stdout):
    alphabet = SequenceType.metadata().alphabet
    f_line = "{name:20} {length:6} " + " ".join("{" + ch + ":4}" for ch in alphabet)
    print(f_line.format(name = "Name", length = "Length", **{ch: ch for ch in alphabet}), file = file)
    print("-" * 50, file = file)
    for read in read_fasta(fname, SequenceType):
        line = f_line.format(name = read.name, length = read.length, **read.get_stat())
        print(line, file = file)
