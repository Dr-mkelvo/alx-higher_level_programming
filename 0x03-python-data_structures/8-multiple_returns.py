#!/usr/bin/python3


def multiple_returns(sentence):
    for element in sentence:
        if len(sentence) == 0:
            return (0, none)
        else:
            return (len(sentence), sentence[0])
