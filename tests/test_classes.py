from unittest import TestCase

from src.classes import Manner, Place, VowelHeight, VowelBackness, Phoneme, Syllable, Morpheme

phoneme_c = Phoneme(
    symbol="c",
    manner=Manner.PLOSIVE,
    place=Place.VELAR,
    voiced=False,
    height=None,
    backness=None,
    rounded=False
)
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
syllable_cab = Syllable(
    [phoneme_c],
    [phoneme_a],
    [phoneme_b]
)
morpheme_cabcab = Morpheme((list(syllable_cab) + list(syllable_cab)))

class TestPhonemeClass(TestCase):
    def test_phoneme_invalid(self):
        with self.assertRaisesRegex(ValueError, "height and backnes"):
            invalid_vowel = Phoneme(
                symbol="a",
                manner=Manner.VOWEL,
                place=None,
                voiced=True,
                height=None,
                backness=None,
                rounded=False
            )
        with self.assertRaisesRegex(ValueError, "place of articulation"):
            invalid_consonant = Phoneme(
                symbol="b",
                manner=Manner.PLOSIVE,
                place=None,
                voiced=True,
                height=None,
                backness=None,
                rounded=False
            )

    def test_ignored_articulation(self):
        phoneme = phoneme_a
        self.assertIsNone(phoneme.place)

    def test_phoneme_string(self):
        phoneme = phoneme_a
        self.assertEqual(str(phoneme), "a")

    def test_phoneme_eq(self):
        phoneme_a_1 = phoneme_a
        phoneme_a_2 = phoneme_a
        phoneme_b_1 = phoneme_b
        self.assertEqual(phoneme_a_1, phoneme_a_2)
        self.assertNotEqual(phoneme_a_1, phoneme_b_1)

    def test_phoneme_properties(self):
        phoneme = phoneme_a
        self.assertFalse(phoneme.is_approximant)
        self.assertTrue(phoneme.is_vowel)
        self.assertTrue(phoneme.is_sonorant)
        self.assertFalse(phoneme.is_obstruent)


class TestSyllableClass(TestCase):
    def test_syllable_string(self):
        syllable = syllable_cab
        self.assertEqual(str(syllable), "cab")

    def test_syllable_iterator(self):
        phoneme_c_1 = phoneme_c
        phoneme_a_1 = phoneme_a
        phoneme_b_1 = phoneme_b
        syllable = syllable_cab
        self.assertListEqual(list(syllable), [phoneme_c_1, phoneme_a_1, phoneme_b_1])

    def test_syllable_indexing(self):
        phoneme = phoneme_c
        syllable = syllable_cab
        self.assertEqual(syllable[0], phoneme)

    def test_syllable_length(self):
        syllable = syllable_cab
        self.assertEqual(len(syllable), 3)


class TestMorphemeClass(TestCase):
    def test_morpheme_string(self):
        morpheme = morpheme_cabcab
        self.assertEqual(str(morpheme), "cabcab")

    def test_morpheme_iterator(self):
        morpheme = morpheme_cabcab
        syllable = syllable_cab
        self.assertListEqual(list(morpheme), list(syllable) + list(syllable))
        
    def test_morpheme_indexing(self):
        morpheme = morpheme_cabcab
        self.assertEqual(morpheme[0], phoneme_c)

    def test_morpheme_length(self):
        morpheme = morpheme_cabcab
        self.assertEqual(len(morpheme), 6)


class TestWordClass(TestCase):
    ...
