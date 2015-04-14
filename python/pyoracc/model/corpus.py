from __future__ import print_function
import sys
import os
import codecs
from ..atf.atffile import AtfFile


class Corpus(object):
    def __init__(self, pattern="*.atf", **kwargs):
        self.texts = []
        self.failures = 0
        self.successes = 0
        if 'source' in kwargs:
            for dirpath, _, files in os.walk(kwargs['source']):
                for file in files:
                    try:
                        path = os.path.join(dirpath, file)
                        print("Parsing file", path, "... ", end="")
                        content = codecs.open(path,
                                              encoding='utf-8-sig').read()
                        self.texts.append(AtfFile(content))

                        self.successes += 1
                        print("OK")
                    except:
                        self.texts.append(None)
                        self.failures += 1
                        print("Failed")


if __name__ == '__main__':
    corpus = Corpus(source=sys.argv[1])
    print()
    print("Failed with ", corpus.failures, " out of ",
          corpus.failures + corpus.successes, "(",
          corpus.failures * 100.0 / (corpus.failures + corpus.successes),
          "%)")
