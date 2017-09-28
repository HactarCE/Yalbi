# Suffixes

[TODO] Clean up


-- If you're looking to edit `suffixes.md`, you're in the right place. Any changes made here will be reflected in `suffixes.md` next time the lexicon is recompiled.
-- Lines beginning with two dashes will not appear in `suffixes.md`.
--OUTFILE ../suffixes.md
--AUTOGEN_WARNING [`suffixes_template.md`](autogen/suffixes_template.md) or [`suffixes.hjson`](autogen/suffixes.hjson)

Suffixes are the most powerful morphological tool in Yalbi. They can function as adjectives or adverbs and are capable of conveying nearly any morphological category. Every formative requires at least one suffix, which specifies either Case (for nouns and framed verbs) or Illocution and Validation (for main verbs). The last suffix in a word must convey either Case or Illocution.

## Case suffixes

Degree is listed along the top; consonantal VxC values are listed along the left.

| VxC (Case) |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | Case category |
|:----------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---------------|
|    (h)     | ABS | IND | ERG | DER | OBL | SIT | EFF | ESS | AFF | Transrelative |
|     m      | GEN | ITP | OGN | PDC | COR | PAR | IDP | POS | PRP | Possessive    |
|     lv     |  -  |  -  |  -  | APL | UTL | PUR |  -  |  -  |  -  | Utilitative   |
|     n      | DAT | APP | ASI | REF | FUN | CNV | TSP | CLA | CSD | Associative 1 |
|     rf     | CRS | CMP | MED | COM | TFM | CNJ | CPS | CVS | CMM | Associative 2 |
|     ln     | AVR | CON | EXC | PTL | DEP | PVS | EXM | PRD | BEN | Associative 3 |
|     rm     | PLM | ELP | PCV | CNR | SML | ASC | PCR | ALP | LIM | Temporal 1    |
|     lm     | INP | EPS | ASS | PER | DFF | PRO |  -  |  -  |  -  | Temporal 2    |
|     rn     |  -  | ABL |  -  | PSV | LOC | NAV | ORI | ALL |  -  | Spatial       |
|     x      |  -  |  -  |  -  |  -  | VOC |  X  | ITJ |  X  |  -  | Interjective  |

**h** is omitted if word-final

## Illocution/Validation suffixes

Only Assertive, Allegative, and Imputative illocutions can be used with Validation. For these, the vowel of the suffix indicates Validation and the consonant indicates Illocution.

| Validation    | Vx value |
|---------------|:--------:|
| Epistemic     |    a     |
| Axiomatic     |    ai    |
| Participatory |    e     |
| Confirmative  |    o     |
| Indirective   |    i     |
| Conclusory    |    oi    |
| Inferential   |    ei    |
| Assumptive    |    au    |
| Intuitive     |    u     |
| Subjective    |    oa    |
| Presumptive   |    ia    |
| Purportive    |    ie    |
| Putative      |    io    |

| Suffix | Illocution |
|--------|------------|
| -l     | Assertive  |
| -f     | Allegative |
| -v     | Imputative |

For the remaining eight Illocutions, the consonant is simply **r** and the vowel indicates Illocution.

| -r | Illocution          |
|----|---------------------|
| 1  | `IRG` Interrogative |
| 2  | `EXV` Expatiative   |
| 3  | `THR` Theoretical   |
| 4  | -                   |
| 5  | `DEC` Declarative   |
| 6  | `OPT` Optative      |
| 7  | `ADM` Admonitive    |
| 8  | `HOR` Hortative     |
| 9  | `DIR` Directive     |

## Collective suffixes

These four suffixes serve the role of Ithkuil's [Configuration](http://ithkuil.net/03_morphology.html#Sec3o1) and [Affiliation](http://ithkuil.net/03_morphology.html#Sec3o2) categories.

| Degree | Configuration                                                             |
|--------|---------------------------------------------------------------------------|
| 1      | `UNI` Uniplex - a single thing                                            |
| 2      | `DPX` Duplex - a pair of things                                           |
| 3      | `DCT` Discrete - a group of similar things                                |
| 4      | `AGG` Aggregative - a group of different things                           |
| 5      | `SEG` Segmentative - a connected group of similar things                  |
| 6      | `CPN` Componential - a connected group of different things                |
| 7      | `COH` Coherent - a single entity composed of a group of similar things    |
| 8      | `CST` Composite - a single entity composed of a group of different things |
| 9      | `MLT` Multiform - a group of X-like things                                |

| Suffix | Affiliation                               |
|--------|-------------------------------------------|
| -mt    | `CSL` Consolidative - neutral to purpose  |
| -mk    | `ASO` Associative - unified purpose       |
| -mp    | `VAR` Variative - opposing purposes       |
| -ms    | `COA` Coalescent - complementary purposes |
