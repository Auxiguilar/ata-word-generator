from enum import Enum, auto
from dataclasses import dataclass


class Manner(Enum):
    PLOSIVE = auto()
    FRICATIVE = auto()
    AFFRICATE = auto()
    NASAL = auto()
    LIQUID = auto() # Trouble in paradise! What is this?
    GLIDE = auto()
    VOWEL = auto()


class Place(Enum):
    BILABIAL = auto()
    LABIODENTAL = auto()
    DENTAL = auto()
    ALVEOLAR = auto()
    POSTALVEOLAR = auto()
    PALATAL = auto()
    VELAR = auto()
    UVULAR = auto()
    GLOTTAL = auto()


class VowelHeight(Enum):
    CLOSE = auto()
    NEAR_CLOSE = auto()
    CLOSE_MID = auto()
    MID = auto()
    OPEN_MID = auto()
    NEAR_OPEN = auto()
    OPEN = auto()


class VowelBackness(Enum):
    FRONT = auto()
    CENTRAL = auto()
    BACK = auto()


@dataclass(frozen=True)
class Phoneme:
    symbol: str
    manner: Manner
    place: Place | None = None
    voiced: bool | None = None
    height: VowelHeight | None = None
    backness: VowelBackness | None = None
    rounded: bool | None = None

    def __post_init__(self):
        # Validate
        if self.manner == Manner.VOWEL:
            if (self.height is None or
                self.backness is None or
                self.rounded is None):
                raise ValueError("Invalid vowel.")
        else:
            if self.place is None or self.voiced is None:
                raise ValueError("Invalid consonant.")

        # Normalize
        if self.manner == Manner.VOWEL:
            object.__setattr__(self, "place", None)
        else:
            object.__setattr__(self, "height", None)
            object.__setattr__(self, "backness", None)
            object.__setattr__(self, "rounded", None)

    # TODO: Dubious definition of approximant?
    @property
    def is_approximant(self) -> bool:
        return self.manner in (Manner.GLIDE, Manner.LIQUID)

    @property
    def is_sonorant(self) -> bool:
        return self.manner in (
            Manner.NASAL,
            Manner.LIQUID,
            Manner.GLIDE,
            Manner.VOWEL
        )

    @property
    def is_obstruent(self) -> bool:
        return self.manner in (
            Manner.PLOSIVE,
            Manner.FRICATIVE,
            Manner.AFFRICATE
        )

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return (
            f"Phoneme(symbol={self.symbol!r}, "
            f"manner={self.manner!r}, "
            f"place={self.place!r}, "
            f"voiced={self.voiced!r}, "
            f"height={self.height!r}, "
            f"backness={self.backness!r}, "
            f"rounded={self.rounded!r})"
        )


class Syllable:
    def __init__(self,
            onset: list[Phoneme] | None,
            nucleus: list[Phoneme],
            coda: list[Phoneme] | None) -> None:
        self.onset = onset if onset is not None else []
        self.nucleus = nucleus
        self.coda = coda if coda is not None else []

    def __iter__(self):
        for p in self.onset:
            yield p
        for p in self.nucleus:
            yield p
        for p in self.coda:
            yield p

    def __getitem__(self, index: int):
        return (self.onset + self.nucleus + self.coda)[index]

    def __len__(self):
        return len(self.onset) + len(self.nucleus) + len(self.coda)

    def __str__(self) -> str:
        return "".join(str(p) for p in self)

    def __repr__(self) -> str:
        return (
            f"Syllable(onset={self.onset!r}, "
            f"nucleus={self.nucleus!r}, "
            f"coda={self.coda!r})"
        )


class Morpheme:
    def __init__(self, phoneme: list[Phoneme]) -> None:
        self.phonemes = phoneme

    def __iter__(self):
        yield from self.phonemes

    def __getitem__(self, index: int):
        return self.phonemes[index]

    def __len__(self):
        return len(self.phonemes)

    def __str__(self) -> str:
        return "".join(str(p) for p in self)

    def __repr__(self) -> str:
        return (
            f"Morpheme(phonemes={self.phonemes!r})"
        )


class Word:
    def __init__(self,
            morphemes: list[Morpheme],
            syllables: list[Syllable] | None = None) -> None:
        self.morphemes = morphemes
        self._syllables = syllables
        if self.syllables is not None:
            self._validate_syllables()

    def _validate_syllables(self):
        if self._syllables is None:
            return
        
        phonemes_from_syllables: list[Phoneme] = []
        for s in self._syllables:
            phonemes_from_syllables.extend(list(s))
        if len(phonemes_from_syllables) != len(self):
            raise ValueError("Invalid syllabification: unequal length")
        
        phonemes_from_morphemes: list[Phoneme] = []
        for m in self.morphemes:
            phonemes_from_morphemes.extend(m)
        for i in range(len(phonemes_from_morphemes)):
            if phonemes_from_morphemes[i] != phonemes_from_syllables[i]:
                raise ValueError(
                    f"Invalid syllabification: phoneme mismatch ({phonemes_from_morphemes[i]}, {str(phonemes_from_syllables[i])})"
                )

    @property
    def syllables(self):
        # This whole affair seems kinda stupid.
        if self._syllables is None:
            return []
        return self._syllables

    def syllabify(self, syllabifier):
        # Later implementation.
        ...

    def __iter__(self):
        for m in self.morphemes:
            yield from m

    def __getitem__(self, index: int):
        phonemes = []
        for m in self.morphemes:
            phonemes.extend(m)
        return phonemes[index]

    def __len__(self):
        return sum(len(morpheme) for morpheme in self.morphemes)

    def __str__(self) -> str:
        return "".join(str(p) for p in self)

    def __repr__(self) -> str:
        return (
            f"Word(morphemes={self.morphemes!r})"
        )


class Grapheme:
    def __init__(self, symbol: str, phonemes: list[Phoneme]) -> None:
        self.symbol = symbol # Any number of characters.
        self.phonemes = phonemes
