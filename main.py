from src.classes import Manner, Place, VowelHeight, VowelBackness, Phoneme, Syllable, Morpheme, Word


def main():
    print("Hello from ata-word-generator!")

    phoneme_a = Phoneme(
        symbol="a",
        manner=Manner.VOWEL,
        place=None,
        voiced=True,
        height=VowelHeight.OPEN,
        backness=VowelBackness.FRONT,
        rounded=False
    )
    phoneme_b = Phoneme(
        symbol="b",
        manner=Manner.PLOSIVE,
        place=Place.BILABIAL,
        voiced=True,
        height=None,
        backness=None,
        rounded=None
    )
    phoneme_c = Phoneme(
        symbol="c", # Technically incorrect symbol.
        manner=Manner.PLOSIVE,
        place=Place.VELAR,
        voiced=False,
        height=None,
        backness=None,
        rounded=None
    )
    phoneme_s = Phoneme(
        symbol="s",
        manner=Manner.FRICATIVE,
        place=Place.ALVEOLAR,
        voiced=False,
        height=None,
        backness=None,
        rounded=None
    )
    syllable = Syllable(
        [phoneme_c],
        [phoneme_a],
        [phoneme_b]
    )
    morpheme_cab = Morpheme(
        list(syllable)
    )
    morpheme_s = Morpheme(
        [phoneme_s]
    )
    word = Word([morpheme_cab, morpheme_s])

    print(syllable) # "cab," except it's said funny.
    print(syllable[0])
    print([p for p in list(syllable)])
    for p in list(syllable):
        print(p)
    print(repr(syllable))
    print(repr(morpheme_cab))
    print(word) # "cabs"; now plural for your phonemic(?) pleasure
    print(repr(word))


if __name__ == "__main__":
    main()
