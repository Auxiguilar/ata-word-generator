from unittest import TestCase

from src.classes import Manner, Place, VowelHeight, VowelBackness, Phoneme, Syllable, Morpheme


class TestPhonemeClass(TestCase):
    def test_phoneme_invalid(self):
        with self.assertRaisesRegex(ValueError, "Missing place of articulation for vowel."):
            invalid_vowel = Phoneme(
                symbol="a",
                manner=Manner.VOWEL,
                place=None,
                voiced=True,
                height=None,
                backness=None,
                rounded=False
            )
        with self.assertRaisesRegex(ValueError, "Missing place of articulation for consonant."):
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
        phoneme = Phoneme(
            symbol="a",
            manner=Manner.VOWEL,
            place=Place.ALVEOLAR,
            voiced=True,
            height=VowelHeight.OPEN,
            backness=VowelBackness.FRONT,
            rounded=False
        )
        self.assertIsNone(phoneme.place)

    def test_phoneme_string(self):
        phoneme = Phoneme(
            symbol="a",
            manner=Manner.VOWEL,
            place=None,
            voiced=True,
            height=VowelHeight.OPEN,
            backness=VowelBackness.FRONT,
            rounded=False
        )
        self.assertEqual(str(phoneme), "a")

    def test_phoneme_eq(self):
        phoneme_a_1 = Phoneme(
            symbol="a",
            manner=Manner.VOWEL,
            place=None,
            voiced=True,
            height=VowelHeight.OPEN,
            backness=VowelBackness.FRONT,
            rounded=False
        )
        phoneme_a_2 = Phoneme(
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
        self.assertEqual(phoneme_a_1, phoneme_a_2)
        self.assertNotEqual(phoneme_a_1, phoneme_b)

        with self.assertRaises(ValueError):
            eq = phoneme_b == "b"

    def test_phoneme_properties(self):
        phoneme = Phoneme(
            symbol="a",
            manner=Manner.VOWEL,
            place=None,
            voiced=True,
            height=VowelHeight.OPEN,
            backness=VowelBackness.FRONT,
            rounded=False
        )
        self.assertFalse(phoneme.is_approximant)
        self.assertTrue(phoneme.is_vowel)
        self.assertTrue(phoneme.is_sonorant)
        self.assertFalse(phoneme.is_obstruent)


class TestSyllableClass(TestCase):
    def test_syllable_string(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )
        self.assertEqual(str(syllable), "bab")

    def test_syllable_iterator(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )

        self.assertListEqual(list(syllable), [phoneme_b, phoneme_a, phoneme_b])

    def test_syllable_indexing(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )

        self.assertEqual(syllable[0], phoneme_b)


class TestMorphemeClass(TestCase):
    def test_morpheme_string(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )
        morpheme = Morpheme([syllable, syllable])

        self.assertEqual(str(morpheme), "babbab")

    def test_morpheme_iterator(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )
        morpheme = Morpheme([syllable, syllable])

        self.assertListEqual(list(morpheme), list(syllable) + list(syllable))


    def test_morpheme_indexing(self):
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
        syllable = Syllable(
            [phoneme_b],
            [phoneme_a],
            [phoneme_b]
        )
        morpheme = Morpheme([syllable, syllable])

        self.assertEqual(morpheme[0], phoneme_b)
