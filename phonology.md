# Phonology

Yalbi's phonology is quite barebones compared to Ithkuil, and even compared to [my attempt to reform it](https://github.com/HactarCE/I.tkuil).

**.n** and **.e** may be used as ASCII-friendly alternatives to **ŋ** and **ə**.

* [Consonants](#consonants)
* [Vowels](#vowels)
* [Stress and Tone](#stress-and-tone)
* [Phonotactics](#phonotactics)

## Consonants

Where plosives and fricatives appear in pairs, the one on the left is unvoiced and the one on the right is voiced. Otherwise it is unvoiced.

|              | Nasal | Plosive | Fricative | Approximant |
|--------------|:-----:|:-------:|:---------:|:-----------:|
| Bilabial     |   m   |   p b   |           |             |
| Labiodental  |       |         |    f v    |             |
| Alveolar     |   n   |   t d   |    s z    |      r      |
| Postalveolar |       |         |    c j    |     (r)     |
| Palatal      |       |         |           |      y      |
| Labiovelar   |       |         |           |      w      |
| Velar/uvular |   ŋ   |   k g   |     x     |             |
| Glottal      |       |    '    |     h     |             |
| Lateral      |       |         |           |      l      |

The alveolar approximant **r** may also be pronounced as an alveolar tap.

Word-initial nasals that do not form valid [syllable onsets](#syllable-onset) are pronounced as their own syllables. For example, **msral** is pronounced as **m-sral**.

Unvoiced plosives may optionally be aspirated when followed immediately by a vowel.

## Vowels

Front and central vowels are unrounded; back vowels are rounded.

|      |  Front  | Central |   Back   |
|------|:-------:|:-------:|:--------:|
| High | i /i~ɪ/ |         | u /u~ʊ/  |
| Mid  |  e /ɛ/  | ə /ə~ʌ/ | o /o~ou/ |
| Low  |         | a /a~ɑ/ |          |

Yalbi has the following dipthongs:

* ai /ai/
* ei /ei~e/
* oi /oi/
* au /au/

Any other two-vowel combinations are pronounced as two syllables. In three-vowel combinations, the first two vowels are treated as a diphthong and the third is pronounced as a separate syllable.

When an affix containing a disyllabic vowel combination is said to be stressed, only the second syllable of the vowel combination is actually stressed.

## Stress and Tone

Neither syllable stress nor tone is morphologically significant. Each word type has its own stress rules. Tone is used to convey grammatical information or for emphasis. [TODO]

## Phonotactics

_Readers who are not interested in helping to develop Yalbi or who do not care for formal linguistic stuff may want to skip this section._

The phonotactics listed below are written by a complete newbie and probably have a ton of flaws. If you find something in here that seems really hard to pronounce, or notice something simple that I've missed, or find a Yalbi word that does not follow these rules, please [submit an issue](https://github.com/HactarCE/Yalbi/issues/new) or let me know personally.

Syllables consist of three parts: [onset](#syllable-onset), [nucleus](#syllable-nucleus), and [coda](#syllable-coda). Additionally, all words must obey certain [phonotactic constraints](#phonotactic-constraints). Unless otherwise stated, the glottal stop **'** and glottal fricative **h** are not included in any generalized group below.

### Syllable Onset

The onset of a syllable can follow any of these patterns:

* Any consonant (including **h** and the glottal stop, the latter of which is not written when word-initial)
* Nasal + approximant
* Fricative + approximant
* **s**/**c** + nasal
* **s**/**c** + unvoiced plosive (+ approximant)
* Unvoiced plosive + **s**/**c** (+ approximant)
* **dz**/**dj** (+ approximant)
* **pf**/**bv** (+ approximant)

Alternatively, if the syllable is not word-initial and is preceded by an empty coda, a syllable nucleus may be empty.

These rules permit a total of **147** syllable onsets (not including the empty onset).

### Syllable Nucleus

The nucleus of a syllable can follow any of these patterns:

* Any vowel
* Any diphthong
* Any nasal, **l**, or **r** (if the nucleus and coda are both empty)

### Syllable Coda

* Any consonant except **w** or **y**
* (**l**/**r** +) Nasal + fricative (excluding **x**)
* **l**/**r** + plosive/fricative
* Unvoiced plosive + **s**/**c**
* Voiced plosive + **z**/**j**
* **s**/**c** + unvoiced plosive
* **z**/**j** + voiced plosive
* (**l**/**r** +) **mp**/**nt**/**ŋk**
* (**l**/**r** +) **np**

Alternatively, the syllable coda may be empty.

These rules permit a total of **135** syllable codas.

### Phonotactic Constraints

The following phonotactic rules must be obeyed:

* Two consonants with the same place and manner of articulation (voicedness being ignored) cannot appear adjacent in a word
