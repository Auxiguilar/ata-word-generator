from enum import Enum, auto


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


class Phoneme:
    def __init__(self,
            symbol: str,
            manner: Manner,
            place: Place | None,
            voiced: bool,
            height: VowelHeight | None,
            backness: VowelBackness | None,
            rounded: bool | None
        ) -> None:
        self.symbol = symbol
        self.manner = manner
        self.place = place
        self.voiced = voiced

        # Vowels
        self.height = height
        self.backness = backness
        self.rounded = rounded

        # Verify
        if self.manner == Manner.VOWEL:
            if self.height is None or self.backness is None:
                raise ValueError("Missing place of articulation for vowel.")
            elif self.place is not None:
                self.place = None # Ignore consonant articulation
        elif manner != Manner.VOWEL and self.place is None:
            raise ValueError("Missing place of articulation for consonant.")

    # TODO: Dubious definition of approximant?
    @property
    def is_approximant(self) -> bool:
        return self.manner in (Manner.GLIDE, Manner.LIQUID)

    @property
    def is_vowel(self) -> bool:
        return self.manner == Manner.VOWEL

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

    def __eq__(self, other: object) -> bool:
        if type(other) != Phoneme:
            raise ValueError("Phoneme can only compare against own type.")
        elif (
            self.symbol == other.symbol and
            self.manner == other.manner and
            self.place == other.place and
            self.voiced == other.voiced and
            self.height == other.height and
            self.backness == other.backness and
            self.rounded == other.rounded
        ):
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.symbol


class Syllable:
    def __init__(self, onset: list[Phoneme], nucleus: list[Phoneme], coda: list[Phoneme]) -> None:
        self.onset = onset
        self.nucleus = nucleus
        self.coda = coda

    def __iter__(self):
        for p in self.onset:
            yield p
        for p in self.nucleus:
            yield p
        for p in self.coda:
            yield p

    def __getitem__(self, index):
        return list(self)[index]

    def __len__(self):
        return len(self.onset) + len(self.nucleus) + len(self.coda)

    def __str__(self) -> str:
        return "".join(str(p) for p in self)


class Morpheme:
    def __init__(self, syllables: list[Syllable]) -> None:
        self.syllables = syllables

    def __iter__(self):
        for syllable in self.syllables:
            for p in syllable:
                yield p

    def __getitem__(self, index):
        return list(self)[index]

    def __len__(self):
        counter = 0
        for s in self.syllables:
            counter += len(s)
        return counter

    def __str__(self) -> str:
        return "".join(str(p) for p in self)


class Grapheme:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol # Any number of characters.