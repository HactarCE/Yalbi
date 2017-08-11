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

CVn conveys Illocution and Validation.

| Cn                                | `ASR` | `ALG` | `IPU` | `THR` | `EXV` | `AXM` | `DIR` | `IRG` | `ADM` | `HOR` | `DEC` |
|-----------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `CNF` Confirmative                |  la   |  le   |  li   |   -   |   -   |  lo   |  rai  |  rei  |  lu   |  lai  |  lei  |
| `AFM` Affirmative                 |  ra   |  re   |  ri   |   -   |   -   |  ro   |   -   |   -   |  ru   |   -   |   -   |
| `RPT` Reportative                 |  ja   |  je   |  ji   |   -   |   -   |  jo   |   -   |   -   |  ju   |   -   |   -   |
| `INF` Inferential                 |  sa   |  se   |  si   |  sai  |  sei  |  so   |   -   |   -   |  su   |   -   |   -   |
| `ITU` Intuitive                   |  ca   |  ce   |  ci   |  cai  |  cei  |  co   |   -   |   -   |  cu   |   -   |   -   |
| `TS-V` Trustworthy-Verifiable     |  bla  |  ble  |  bli  |   -   |   -   |  blo  |   -   |   -   |  blu  |   -   |   -   |
| `TS-U` Trustworthy-Unknown        |  ba   |  be   |  bi   |   -   |   -   |  bo   |   -   |   -   |  bu   |   -   |   -   |
| `TS-N` Trustworthy-Unverifiable   |  bra  |  bre  |  bri  |   -   |   -   |  bro  |   -   |   -   |  bru  |   -   |   -   |
| `US-V` Unknown-Verifiable         |  za   |  ze   |  zi   |   -   |   -   |  zo   |   -   |   -   |  zu   |   -   |   -   |
| `US-U` Unknown-Unknown            |  da   |  de   |  di   |   -   |   -   |  do   |   -   |   -   |  du   |   -   |   -   |
| `US-N` Unknown-Unverifiable       |  dra  |  dre  |  dri  |   -   |   -   |  dro  |   -   |   -   |  dru  |   -   |   -   |
| `NS-V` Untrustworthy-Verifiable   |  gla  |  gle  |  gli  |   -   |   -   |  glo  |   -   |   -   |  glu  |   -   |   -   |
| `NS-U` Untrustworthy-Unknown      |  ga   |  ge   |  gi   |   -   |   -   |  go   |   -   |   -   |  gu   |   -   |   -   |
| `NS-N` Untrustworthy-Unverifiable |  gra  |  gre  |  gri  |   -   |   -   |  gro  |   -   |   -   |  gru  |   -   |   -   |

CVn is not allowed if Ve conveys `A` Abstract perspective.

## CVr and Cs

CVr is any root from the [roots lexicon](roots.md). Cs is a predefined consonantal stem, which is listed for each root. The default value for Cs is **l**.

## CVc

CVc conveys Case. Each Case is also marked as to whether it pertains to the verb (e.g. `OBL`), the previous noun (e.g. `OBLp`), or the next noun (e.g. `OBLn`). Cases are grouped into modifier-like sets of nine; each case is assigned a vowel based on its degree and "type" (1 = pertains to verb, 2 = previous noun, 3 = next noun), using the vocalic values of [CVm](#cvm). Case "type" does not at all correlate with modifier "type" except that they use the same endings. [TODO] This is really confusing.

Degrees are listed along the top and consonants are listed along the left; the intersections correspond to cases.

| CVc |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | Case category |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---------------|
| (h) | ABS | IND | ERG | DER | OBL | SIT | EFF | ESS | AFF | Transrelative |
|  m  | GEN | ITP | OGN | PDC | COR | PAR | IDP | POS | PRP | Possessive    |
|  n  |  -  |  -  |  -  | APL | UTL | PUR |  -  |  -  |  -  | Utilitative   |
|  p  |  -  | APP | ASI | REF | FUN | CNV | TSP | CLA | CSD | Associative 1 |
|  t  | CRS | CMP | MED | COM | TFM | CNJ | CPS | CVS | CMM | Associative 2 |
|  k  | AVR | CON | EXC | PTL | DEP | PVS | EXM | PRD | BEN | Associative 3 |
| sp  | PLM | ELP | PCV | CNR | SML | ASC | PCR | ALP | LIM | Temporal 1    |
| st  | INP | EPS | ASS | PER | DFF | PRO |  -  |  -  |  -  | Temporal 2    |
| sk  |  -  | ABL |  -  | PSV | LOC | NAV | ORI | ALL |  -  | Spatial       |
|  x  |  -  |  -  |  -  |  -  | VOC |  X  | ITJ |  X  |  -  | Interjective  |

[TODO] Comparison cases (**s**/**c** + nasal)

**h** is omitted if word-initial.

## CVf

CVf conveys Case-frame and Function.

| CVf | Case frame |
|-----|:----------:|
| xe  |    Nope    |
| xi  |    Yup     |

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
