# Affixes

* [Cd - Derived root](#cr-and-cs)
* [Cp - Carrier type](#cp)
* [Cs - Stem](#cvr-and-cs)
* [CVc - Case](#cvc)
* [CVf - Case-frame + Function + Perspective](#vf)
* [CVm - Modifier](#cvm)
* [CVn - Illocution + Validation + Function + Perspective](#cvn)
* [CVr - Root](#cvr-and-cs)
* [Ve - Extension + Perspective + Essence](#ve)
* [Vi - Modifier role](#vi)

## Cp

Cp specifies the information which follows a carrier word.

[TODO]

## CVm

CVm conveys a modifier. The consonantal portion of CVm is listed in the [modifiers lexicon](modifiers.md). The vocalic portion of CVm conveys type and degree.

| Vm     | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 | Degree 6 | Degree 7 | Degree 8 | Degree 9 |
|--------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| Type 1 |    au    |    ai    |    oi    |    ei    |    a     |    e     |    o     |    i     |    u     |
| Type 3 |    iu    |    ia    |    io    |    ie    |    oa    |    ue    |    uo    |    ua    |    ui    |
| Type 2 |   aiu    |   aia    |   aio    |   aie    |    oe    |   aue    |   auo    |   aua    |   aui    |

## CVn

CVn conveys Illocution, Validation, Function, and Perspective. It is split into two smaller affixes: CVn1 and CVn2.

### CVn1

CVn1 conveys Function.

| Function | CVn1 |
|----------|:----:|
| `STA`    |  -   |
| `DYN`    |  s   |
| `MNF`    |  c   |

The CVn1 value for `STA/M` is **h** if CVn2 conveys `IPU` Imputative, `AXM`, or `ADM` Axiomatic illocution; otherwise it is blank.

[TODO] Why would a verb be Abstract but still have Illocution? Abstract verbs should have case instead -- like framed verbs without a case-frame.

### CVn2

CVn2 conveys Illocution and Validation.

| Cn                              | `ASR` | `ALG` | `IPU` | `THR` | `EXV` | `AXM` | `DIR` | `IRG` | `ADM` | `HOR` | `DEC` |
|---------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `CNF` Confirmative              |  la   |  ra   |  ta   |   -   |   -   |  pa   |  kia  |  kie  |  ka   |  kio  |  kiu  |
| `AFM` Affirmative               |  le   |  re   |  te   |   -   |   -   |  pe   |   -   |   -   |  ke   |   -   |   -   |
| `RPT` Reportative               |  li   |  ri   |  ti   |   -   |   -   |  pi   |   -   |   -   |  ki   |   -   |   -   |
| `INF` Inferential               |  lo   |  ro   |  to   |  tia  |  tie  |  po   |   -   |   -   |  ko   |   -   |   -   |
| `ITU` Intuitive                 |  lau  |  rau  |  tau  |  tio  |  tiu  |  pau  |   -   |   -   |  kau  |   -   |   -   |
| `PSM-TEN` Presumptive-Tentative |  lai  |  rai  |  tai  |   -   |   -   |  pai  |   -   |   -   |  kai  |   -   |   -   |
| `PSM-PUT` Presumptive-Putative  |  lei  |  rei  |  tei  |   -   |   -   |  pei  |   -   |   -   |  kei  |   -   |   -   |
| `PSM-DUB` Presumptive-Dubious   |  loi  |  roi  |  toi  |   -   |   -   |  poi  |   -   |   -   |  koi  |   -   |   -   |
| `PPT-TEN` Purportive-Tentative  |  loa  |  roa  |  toa  |   -   |   -   |  poa  |   -   |   -   |  koa  |   -   |   -   |
| `PPT-PUT` Purportive-Putative   |  loe  |  roe  |  toe  |   -   |   -   |  poe  |   -   |   -   |  koe  |   -   |   -   |
| `PPT-DUB` Purportive-Dubious    |  lu   |  ru   |  tu   |   -   |   -   |  pu   |   -   |   -   |  ku   |   -   |   -   |
| `IPB-TEN` Improbable-Tentative  |  lua  |  rua  |  tua  |   -   |   -   |  pua  |   -   |   -   |  kua  |   -   |   -   |
| `IPB-PUT` Improbable-Putative   |  lue  |  rue  |  tue  |   -   |   -   |  pue  |   -   |   -   |  kue  |   -   |   -   |
| `IPB-DUB` Improbable-Dubious    |  lui  |  rui  |  tui  |   -   |   -   |  pui  |   -   |   -   |  kui  |   -   |   -   |

## CVr and Cs

CVr is any root from the [roots lexicon](roots.md). Cs is a predefined consonantal stem, which is listed for each root. The default value for Cs is **l**.

## CVc

CVc conveys Case. Each Case is also marked as to whether it pertains to the verb (e.g. `OBL`), the previous noun (e.g. `OBLp`), or the next noun (e.g. `OBLn`). Cases are grouped into modifier-like sets of nine; each case is assigned a vowel based on its degree and "type" (1 = pertains to verb, 2 = previous noun, 3 = next noun), using the vocalic values of [CVm](#cvm). Case "type" does not at all correlate with modifier "type" except that they use the same endings. [TODO] This is really confusing.

Degrees are listed along the top and consonants are listed along the left; the intersections correspond to cases.

| CVc |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | Case category |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---------------|
| (h) | ABS | IND | ERG | DER | OBL | SIT | EFF | ESS | AFF | Transrelative |
|  b  | GEN | ITP | OGN | PDC | COR | PAR | IDP | POS | PRP | Possessive    |
|  d  |  -  |  -  |  -  | APL | UTL | PUR |  -  |  -  |  -  | Utilitative   |
|  m  |  -  | APP | ASI | REF | FUN | CNV | TSP | CLA | CSD | Associative 1 |
|  n  | CRS | CMP | MED | COM | TFM | CNJ | CPS | CVS | CMM | Associative 2 |
|  ŋ  | AVR | CON | EXC | PTL | DEP | PVS | EXM | PRD | BEN | Associative 3 |
| sp  | PLM | ELP | PCV | CNR | SML | ASC | PCR | ALP | LIM | Temporal 1    |
| st  | INP | EPS | ASS | PER | DFF | PRO |  -  |  -  |  -  | Temporal 2    |
| sk  |  -  | ABL |  -  | PSV | LOC | NAV | ORI | ALL |  -  | Spatial       |
|  x  |  -  |  -  |  -  |  -  | VOC |  X  | ITJ |  X  |  X  | Interjective  |

[TODO] Comparison cases (**s**/**c** + nasal)

**h** is omitted if word-initial.

## CVf

CVf conveys Case-frame and Function.

| CVf               | `FRM` Framed |
|-------------------|:------------:|
| `STA` Stative     |      xe      |
| `DYN` Dynamic     |      xi      |
| `MNF` Manifestive |      xu      |

## Ve

Ve conveys Perspective, Essence, and Context.

| Ve      | `EXS` Existential | `MTR` Metaphorical |
|---------|:-----------------:|:------------------:|
| `M/NRM` |         a         |         ua         |
| `M/RPS` |        ai         |         ia         |
| `U/NRM` |         e         |         ue         |
| `U/RPS` |        ei         |         ie         |
| `N/NRM` |         o         |         uo         |
| `N/RPS` |        oi         |         io         |
| `A/NRM` |         u         |         i          |
| `A/RPS` |        ui         |         iu         |

## Vi

Vi conveys the role of a detached modifier. Its values are listed under [the independent modifier section](morphophonology.md#independent-modifier) in [Morphophonology](morphophonology.md).
