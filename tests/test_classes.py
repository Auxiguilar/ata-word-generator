from unittest import TestCase

from src.classes import Manner, Place, VowelHeight, VowelBackness, Phoneme, Syllable, Morpheme, Word

phoneme_c = Phoneme(
    symbol="c",
    manner=Manner.PLOSIVE,
    place=Place.VELAR,
    voiced=False
)
phoneme_a = Phoneme(
    symbol="a",
    manner=Manner.VOWEL,
    voiced=True,
    height=VowelHeight.OPEN,
    backness=VowelBackness.FRONT,
    rounded=False
)
phoneme_b = Phoneme(
    symbol="b",
    manner=Manner.PLOSIVE,
    place=Place.BILABIAL,
    voiced=True
)
phoneme_s = Phoneme(
    symbol="s",
    manner=Manner.FRICATIVE,
    place=Place.ALVEOLAR,
    voiced=False
)
syllable_cab = Syllable(
    [phoneme_c],
    [phoneme_a],
    [phoneme_b]
)
morpheme_cab = Morpheme(list(syllable_cab))
word_cabs = Word([
    morpheme_cab,
    Morpheme([phoneme_s])
])


class TestPhonemeClass(TestCase):
    def test_phoneme_invalid(self):
        with self.assertRaisesRegex(ValueError, "vowel"):
            invalid_vowel = Phoneme(
                symbol="a",
                manner=Manner.VOWEL,
                place=None,
                voiced=True,
                height=None,
                backness=None,
                rounded=False
            )
        with self.assertRaisesRegex(ValueError, "consonant"):
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
        morpheme = morpheme_cab
        self.assertEqual(str(morpheme), "cab")

    def test_morpheme_iterator(self):
        morpheme = morpheme_cab
        syllable = syllable_cab
        self.assertListEqual(list(morpheme), list(syllable))
        
    def test_morpheme_indexing(self):
        morpheme = morpheme_cab
        phoneme = phoneme_c
        self.assertEqual(morpheme[0], phoneme)

    def test_morpheme_length(self):
        morpheme = morpheme_cab
        self.assertEqual(len(morpheme), 3)


class TestWordClass(TestCase):
    def test_word_string(self):
        word = word_cabs
        self.assertEqual(str(word), "cabs")

    def test_word_iterator(self):
        word = word_cabs
        syllable = syllable_cab
        phoneme = phoneme_s
        self.assertListEqual(list(word), list(syllable) + [phoneme])

    def test_word_indexing(self):
        word = word_cabs
        phoneme = phoneme_s
        self.assertEqual(word[3], phoneme)

    def test_word_length(self):
        word = word_cabs
        self.assertEqual(len(word), 4)

    # Future: Test syllable validation
    # Possibly: Test syllabification.
