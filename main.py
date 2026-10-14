from src.classes import Manner, Place, VowelHeight, VowelBackness, Phoneme, Syllable, Morpheme


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
        rounded=False
    )
    phoneme_c = Phoneme(
        symbol="c", # Technically incorrect symbol.
        manner=Manner.PLOSIVE,
        place=Place.VELAR,
        voiced=False,
        height=None,
        backness=None,
        rounded=False
    )

    syllable = Syllable(
        [phoneme_c],
        [phoneme_a],
        [phoneme_b]
    )

    print(syllable) # "Cab," except it's said funny.
    print(syllable[0])
    print([str(p) for p in list(syllable)]) # cuz repr
    for p in list(syllable):
        print(p)


if __name__ == "__main__":
    main()
