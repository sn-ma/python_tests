from tasks.task3.sequences import AbstractSequence


def read_fasta(fname, SequenceType):
    assert issubclass(SequenceType, AbstractSequence)
    with open(fname) as fin:
        name, sequence = None, ""
        for line in fin:
            line = line.strip()
            if line.startswith(">"):
                if name is not None and sequence != "":
                    yield SequenceType(sequence, name)
                name = line[1:]
                sequence = ""
            else:
                sequence += line
        if name is not None and sequence != "":
            yield SequenceType(sequence, name)
