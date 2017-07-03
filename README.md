# Yalbi

After trying to reform [Ithkuil](http://www.ithkuil.net/) and discovering several deeply rooted morphological flaws and ambiguities, I decided to try to create my own language using my favorite parts of Ithkuil as a starting point. The result is Yalbi, Yet Another Language Based on Ithkuil.

* [Phonology](#phonology)
* [Morphology](#morphology)
* [Morphophonology](#morphophonology)
* [Lexicon](#lexicon)

## Phonology

Yalbi's phonology is quite barebones compared to Ithkuil, and even compared to [my attempt to reform it](https://github.com/HactarCE/I.tkuil).

* [Consonants](#consonants)
* [Vowels](#vowels)
* [Stress and Tone](#stress-and-tone)

### Consonants

Where plosives and fricatives appear in pairs, the one on the left is unvoiced and the one on the right is voiced. Otherwise it is unvoiced.

|              | Nasal  | Plosive | Fricative | Approximant |
|--------------|:------:|:-------:|:---------:|:-----------:|
| Bilabial     |   m    |   p b   |           |             |
| Labiodental  |        |         |    f v    |             |
| Alveolar     |   n    |   t d   |    s z    |      r      |
| Postalveolar |        |         |    c j    |     (r)     |
| Palatal      |        |         |           |      y      |
| Labiovelar   |        |         |           |      w      |
| Velar/uvular | ŋ / .n |   k g   |     x     |             |
| Glottal      |        |    '    |     h     |             |
| Lateral      |        |         |           |      l      |

The alveolar approximant **r** may also be pronounced as an alveolar tap.

Word-initial nasals that do not form valid [syllable onsets](#syllable-onset) are pronounced as their own syllables. For example, **msral** is pronounced as **m-sral**.

Unvoiced plosives may optionally be aspirated when followed immediately by a vowel.

### Vowels

Front and central vowels are unrounded; back vowels are rounded.

|      |  Front  | Central |  Back   |
|------|:-------:|:-------:|:-------:|
| High | i /i~ɪ/ |         | u /u~ʊ/ |
| Mid  |  e /ɛ/  | ~ /ə~ʌ/ |  o /o/  |
| Low  |         |  a /a/  |         |

Yalbi has the following dipthongs:

* ai
* ei
* oi
* au

Any other two-vowel combinations are pronounced as two syllables. In three-vowel combinations, the first two vowels are treated as a diphthong and the third is pronounced as a separate syllable.

### Stress and Tone

Neither syllable stress nor tone is morphologically significant. Each word type has its own stress rules. Tone is used to convey grammatical information or for emphasis. [TODO]

### Phonotactics

_Readers who are not interested in helping to develop Yalbi or who do not care for formal linguistic stuff may want to skip this section._

The phonotactics listed below are written by a complete newbie and probably have a ton of flaws. If you find something in here that seems really hard to pronounce, or notice something simple that I've missed, or find a Yalbi word that does not follow these rules, please [submit an issue](https://github.com/HactarCE/Yalbi/issues/new) or let me know personally.

Syllables consist of three parts: [onset](#syllable-onset), [nucleus](#syllable-nucleus), and [coda](#syllable-coda). Additionally, all words must obey certain [phonotactic constraints](#phonotactic-constraints). Unless otherwise stated, the glottal stop **'** and glottal fricative **h** are not included in any generalized group below.

#### Syllable Onset

The onset of a syllable can follow any of these patterns:

21 * Any consonant (including **h** and the glottal stop, the latter of which is not written when word-initial)
12 * Nasal + approximant
28 * Fricative + approximant
6 * **s**/**c** + nasal
30 * **s**/**c** + unvoiced plosive (+ approximant)
30 * Unvoiced plosive + **s**/**c** (+ approximant)
10 * **dz**/**dj** (+ approximant)
10 * **pf**/**bv** (+ approximant)

Alternatively, if the syllable is not word-initial and is preceded by an empty coda, a syllable nucleus may be empty.

These rules permit a total of **147** syllable onsets (not including the empty onset).

#### Syllable Nucleus

The nucleus of a syllable can follow any of these patterns:

* Any vowel
* Any diphthong
* Any nasal, **l**, or **r** (if the nucleus and coda are both empty)

#### Syllable Coda

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

#### Phonotactic Constraints

The following phonotactic rules must be obeyed:

* Two consonants with the same place and manner of articulation (voicedness being ignored) cannot appear adjacent in a word

## Morphology

Most of Ithkuil's categories have been transformed into "modifiers," the reincarnation of derivational suffixes. Others have been replaced with the derivational consonant, which operates as a more powerful SSD. The rest have been vastly simplified.

* [Case](#case)
* [Illocution](#illocution)
* [Validation](#validation)
* [Extension](#extension)
* [Perspective](#perspective)
* [Essence](#essence)

### Case

Yalbi has only twelve cases.

| No. | Vc value | Abbreviation |        Name        |                                     Use                                     |
|:---:|:--------:|:------------:|:------------------:|---------------------------------------------------------------------------|
|  1  |    a     |    `OBL`     |      Oblique       |                                   Content                                   |
|  2  |    ei    |    `IND`     |      Inducive      |                               Agent + patient                               |
|  3  |    i     |    `ABS`     |     Absolutive     |                                   Patient                                   |
|  4  |    e     |    `ERG`     |      Ergative      |                                    Agent                                    |
|  5  |    ai    |    `EFF`     |    Effectuative    |                                   Enabler                                   |
|  6  |    ie    |    `AFF`     |     Affective      |                                 Experiencer                                 |
|  7  |    oi    |    `DAT`     |       Dative       |                               Indirect object                               |
|  8  |   aie    |    `DER`     |     Derivative     |                 Inanimate force or non-deliberate stimulus                  |
|  9  |   eia    |    `CPS`     |     Compsitive     |                               Thing consumed                                |
| 10  |   oia    |    `RSL`     |    Resultative     | Result ("into X" as in "transformed into a frog" OR "with the result of X") |
| 11  |    au    |    `FUN`     |      Functive      |                                Modifies verb                                |
| 12  |    o     |    `CORn`    | Correlative (next) |                             Modifies next noun                              |
| 12  |    u     |    `CORp`    | Correlative (prev) |                           Modifies previous noun                            |

All of Ithkuil's other cases have been replaced with modifiers, used in conjunction with one of the `FUN` Functive or `COR` Correlative cases.

### Illocution

Yalbi's Illocution merges Ithkuil's Illocution and Sanction.

| Abbreviation | Name          | Use                                                                     |
|:------------:|---------------|-------------------------------------------------------------------------|
|    `ASR`     | Assertive     | Neutral proposition of fact                                             |
|    `ALG`     | Allegative    | Proposition open to challenge/refutation                                |
|    `IPU`     | Imputative    | Rebuttable assertion otherwise assumed to be true                       |
|    `THR`     | Theoretical   | Testable hypothesis/theory                                              |
|    `EXV`     | Expatiative   | Hypothesis/theory that may not be verifiable                            |
|    `AXM`     | Axiomatic     | Objectively true, universal fact                                        |
|    `DIR`     | Directive     | Command ("Make it happen such that X")                                  |
|    `IRG`     | Interrogative | Question (used with <some suffix that hasn't been invented yet> [TODO]) |
|    `ADM`     | Admonitive    | Warning ("Be wary of X")                                                |
|    `HOR`     | Hortative     | Wishing ("If only X")                                                   |
|    `DEC`     | Declarative   | Formal announcement; effecting a change per se                          |

On its own, `IRG` Interrogative illocution asks a true/false question: "Is X true?" Alternatively, `IRG` can be used with certain suffixes to ask other types of questions.

### Validation

Yalbi's Validations resemble 2011 Ithkuil's original Validations more than its current ones. Note that many of these are not permitted with certain Illocutions.

| Abbreviation | Name                  | Use                                                   |
|:------------:|-----------------------|-------------------------------------------------------|
|    `CNF`     | Confirmative          | Direct observation/knowledge; verifiable by others    |
|    `AFM`     | Affirmative           | Direct observation/knowledge; unknown verifiability   |
|    `RPT`     | Reportative           | Direct observation/knowledge; unverifiable            |
|    `INF`     | Inferential           | Inference                                             |
|    `ITU`     | Intuitive             | Intuition/feeling                                     |
|  `PSM-TEN`   | Presumptive-Tentative | Trustworthy source; verifiable                        |
|  `PSM-PUT`   | Presumptive-Putative  | Trustworthy source; unknown verifiability             |
|  `PSM-DUB`   | Presumptive-Dubious   | Trustworthy source; unverifiable                      |
|  `PPT-TEN`   | Purportive-Tentative  | Unknown source trustworthiness; verifiable            |
|  `PPT-PUT`   | Purportive-Putative   | Unknown source trustworthiness; unknown verifiability |
|  `PPT-DUB`   | Purportive-Dubious    | Unknown source trustworthiness; unverifiable          |
|  `IPB-TEN`   | Improbable-Tentative  | Untrustworthy source; verifiable                      |
|  `IPB-PUT`   | Improbable-Putative   | Untrustworthy source; unknown verifiability           |
|  `IPB-DUB`   | Improbable-Dubious    | Untrustworthy source; unverifiable                    |

The abbreviations and names for the latter nine Validations have been changed from Ithkuil to be more regular and thus easier to remember.

`CNF` Confirmative is also used as a sort of default Validation for those Illocutions where Validation is not applicable.

With `IRG` Interrogative illocution, Validation might be translated as "I [think/heard/assume] that X is the case; is it so?" (with no applicable suffix) or "I [think/heard/assume] the answer to the following question: X?" (with an applicable suffix). In general, Illocution and Validation operate in parallel rather than modifying one another.

### Perspective

Perspective has been copied almost directly from Ithkuil.

| Abbreviation |   Name    | Nominal meaning       | Verbal meaning                                                          |
|:------------:|:---------:|-----------------------|-------------------------------------------------------------------------|
|     `M`      |  Monadic  | Singular              | An event occurring in the present context (simple present tense)        |
|     `U`      | Unbounded | Plural                | An event that does not occur in the present context (simple past tense) |
|     `N`      |   Nomic   | All instances ever    | Universal rule (eg. "Gravity is one of the fundamental forces")         |
|     `A`      | Abstract  | The idea of X, X-ness | "Timeless" verb form (infinitives, gerundives, etc.)                    |

Abstract perspective is generally not used with main verbs.

Collective nouns are shown either by derivations or using <some suffix that hasn't been invented yet>. [TODO]

Unlike Extension, Perspective is applied nominally or verbally based on grammatical role, not root or derivation.

Here are some examples of Perspective in use:

| Gloss                                  | English                  |
|----------------------------------------|--------------------------|
| _like_-N-[verb] _I_-AFF _cookie_-**M** | "I like a cookie."       |
| _like_-N-[verb] _I_-AFF _cookie_-**U** | "I like [some] cookies." |
| _like_-N-[verb] _I_-AFF _cookie_-**N** | "I like [all] cookies."  |
| _like_-N-[verb] _I_-AFF _cookie_-**A** | "I like cookie-ness."    |
| _jump_-**M**-[verb] _I_-IND            | "I am jumping"           |
| _jump_-**U**-[verb] _I_-IND            | "I was jumping"          |
| _jump_-**N**-[verb] _I_-IND            | "I jump [in general]"    |
| _jump_-**A**-[framed verb] _I_-IND     | "the idea of me jumping" |

### Essence

Yalbi's Essence is identical to Ithkuil's Essence, except that `RPV` Representative has been renamed to `RPS` Representational, to better match `NRM` Normal.

| Abbreviation |       Name       | Use                                                             |
|:------------:|:----------------:|-----------------------------------------------------------------|
|    `NRM`     |      Normal      | A real thing that exists (or a real event)                      |
|    `RPS`     | Representational | Something which doesn't really exist (or doesn't really happen) |

### Context

Yalbi's Context is similar to Ithkuil's Context, but with several changes. The `AMG` Amalgamative has been removed, and `FNC` Functional has been replaced with `SPC` Specific, and its usage has changed. Additionally, `RPS` Representative has been renamed to `MTR` Metaphorical to reduce confusion.

| Abbreviation |     Name     | Use                                                                | Example                             |
|:------------:|:------------:|--------------------------------------------------------------------|-------------------------------------|
|    `EXS`     | Existential  | Default context; no emphasis or special meaning                    | "It's a cat."                       |
|    `SPC`     |   Specific   | Emphasizes that a word means one thing rather than the alternative | "It's a cat (as opposed to a dog)." |
|    `MTR`     | Metaphorical | A metaphor for something; not to be taken literally                | "It's a (metaphorical) cat."        |

Note that the Metaphorical context operates independently from Essence; one can have a metaphor for a thing which really exists, or a metaphor for a thing which does not exist.

Yalbi's `MTR` Metaphorical essence corresponds to Ithkuil's Representational context, while Yalbi's `RPS` Representational essence corresponds to Ithkuil's `RPV` Representative essence. Confused yet?

## Morphophonology

As in Ithkuil, words are formed by following predefined formula with several slots, some of which may be omitted or repeated. Nouns and verbs, while grammatically treated very differently, follow the same morphological formula, which consists of seven morphological "slots," each containing one or more affixes.

|            1            |  2   |        3        |  4   |     5     |     6      |                 7                 |
|:-----------------------:|:----:|:---------------:|:----:|:---------:|:----------:|:---------------------------------:|
|         ( Cn )          |  Vc  |     ( CVc )     | CVr  | ( CVm … ) |     Cd     |              ( Ve )               |
| Illocution + Validation | Case | Additional Case | Root | Modifiers | Derivation | Extension + Perspective + Essence |

* If a word carries no case, slot 4 is stressed; otherwise, the syllable preceding slot 4 is stressed
* The presence of slot 1 indicates that the word is verb
* Slots 2, 4, and 6 are required; all others are optional
* Slot 7 cannot exist without slot 6
* Slot 5 may be repeated

The simplest noun is Vc CVr Cd.
The simplest verb is Cn Vc CVr Cd.

* [Cd - Root Derivation](#cvr-and-cd)
* [Cn - Illocution + Validation](#cn)
* [CVc - Case](#vc-and-cvc)
* [CVm - Modifier](#cvm)
* [CVr - Root](#cvr-and-cd)
* [Vc - Case](#vc-and-cvc)
* [Ve - Extension + Perspective + Essence](#ve)

### Cn

Cn conveys Illocution and Validation.

| Cn                              | `ASR` | `ALG` | `IPU` | `THR` | `EXV` |  `AXM`  | `DIR` | `IRG` | `ADM` | `HOR` | `DEC` |
|---------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `CNF` Confirmative              |   x   |   l   |   r   |   -   |   -   |  xw/xy  |   m   |   z   |   j   |  xl   |  xr   |
| `AFM` Affirmative               |   s   |  sl   |  sr   |   -   |   -   |  sw/sy  |   -   |  zr   |  jr   |   -   |   -   |
| `RPT` Reportative               |   c   |  cl   |  cr   |   -   |   -   |  cw/cy  |   -   |   n   |   ŋ   |   -   |   -   |
| `INF` Inferential               |   f   |  fl   |  fr   |  sn   |  sm   |  fw/fy  |   -   |  fs   |  fc   |   -   |   -   |
| `ITU` Intuitive                 |   v   |  vl   |  vr   |  cn   |  cm   |  vw/vy  |   -   |  vz   |  vj   |   -   |   -   |
| `PSM-TEN` Presumptive-Tentative |   p   |  pl   |  pr   |   -   |   -   |  pw/py  |   -   |   b   |  br   |   -   |   -   |
| `PSM-PUT` Presumptive-Putative  |  sp   |  spl  |  spr  |   -   |   -   | spw/spy |   -   |  bz   |  ps   |   -   |   -   |
| `PSM-DUB` Presumptive-Dubious   |  cp   |  cpl  |  cpr  |   -   |   -   | cpw/cpy |   -   |  bj   |  pc   |   -   |   -   |
| `PPT-TEN` Purportive-Tentative  |   t   |  tl   |  tr   |   -   |   -   |  tw/ty  |   -   |   d   |  dr   |   -   |   -   |
| `PPT-PUT` Purportive-Putative   |  st   |  stl  |  str  |   -   |   -   | stw/sty |   -   |  dz   |  ts   |   -   |   -   |
| `PPT-DUB` Purportive-Dubious    |  ct   |  ctl  |  ctr  |   -   |   -   | ctw/cty |   -   |  dj   |  tc   |   -   |   -   |
| `IPB-TEN` Improbable-Tentative  |   k   |  kl   |  kr   |   -   |   -   |  kw/ky  |   -   |   g   |  gr   |   -   |   -   |
| `IPB-PUT` Improbable-Putative   |  sk   |  skl  |  skr  |   -   |   -   | skw/sky |   -   |  gz   |  ks   |   -   |   -   |
| `IPB-DUB` Improbable-Dubious    |  ck   |  ckl  |  ckr  |   -   |   -   | ckw/cky |   -   |  gj   |  kc   |   -   |   -   |

### Vc and CVc

Vc and CVc each convey Case (for nouns) or Case-frame (for verbs). For nouns and framed verbs, the vocalic values are listed under [the Case section](#case) in [Morphology](#morphology). The consonantal portion of CVc is always **m**. For unframed verbs, which carry no Case, Vc is **~** (/ə/).

### CVr and Cd

CVr is any consonant-vowel root from the [roots lexicon](roots.md). Cd is a predefined consonantal derivation of that root, which is listed within the definition for each root.

### CVm

CVm conveys a modifier, which is nearly identical to one of Ithkuil's derivational suffixes. The consonantal portion of CVm is listed in the [modifiers lexicon](modifiers.md). The vocalic portion of CVm conveys two different values: type and degree.

A modifier may carry one of three types:

* Type 1 - Modifies the word
* Type 2 - Modifies the root
* Type 3 - Modifies the next modifier

Some suffixes have their own specific interpretations for each of these categories, but they will usually adhere to this outline.

A modifier may carry one of nine degrees, which generally form a spectrum from least to greatest.

The vocalic portion of CVm has the following values.

| Vm     | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 | Degree 6 | Degree 7 | Degree 8 | Degree 9 |
|--------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| Type 1 |  iu/ui   |  ia/ua   |  io/ua   |  ie/ue   |    a     |    ei    |    oi    |    ai    |    au    |
| Type 3 |   aui    |   aua    |    oa    |    oe    |    o     |   aiu    |   aia    |   aio    |   aie    |
| Type 2 |   eie    |   eio    |   eia    |   eiu    |    e     |   oie    |   oio    |   oia    |   oiu    |

### Ve

Ve conveys Perspective, and Essence, and Context.

| Ve      | `EXS` Existential | `SPC` Specific | `MTR` Metaphorical |
|---------|:-----------------:|:--------------:|:------------------:|
| `M/NRM` |        (a)        |       oa       |         oe         |
| `M/RPS` |        ai         |      aia       |        aie         |
| `U/NRM` |         e         |      aio       |        aiu         |
| `U/RPS` |        ei         |      eia       |        eie         |
| `N/NRM` |         o         |      eio       |        eiu         |
| `N/RPS` |        oi         |      oia       |        oie         |
| `A/NRM` |        i/u        |     ia/ua      |       ie/ue        |
| `A/RPS` |        au         |     io/uo      |       iu/ui        |

Only `DEL` Delimitive extension is irregular; all other Extensions follow a relatively simple pattern.
