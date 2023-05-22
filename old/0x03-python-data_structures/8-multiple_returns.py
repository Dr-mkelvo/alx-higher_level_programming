#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if len(sentence) == 0:
            return (0, None)
        else:
            return (len(sentence), sentence[0])
