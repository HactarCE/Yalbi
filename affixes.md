# Affixes

* [Cd - Derived root](#cr-and-cs)
* [Cf - Case-frame + Function + Perspective](#cf)
* [Cp - Carrier type](#cp)
* [Cs - Stem](#cvr-and-cs)
* [CVc - Case](#vc-and-cvc)
* [CVm - Modifier](#cvm)
* [CVn - Illocution + Validation + Function + Perspective](#cvn)
* [CVr - Root](#cvr-and-cs)
* [Vc - Case](#vc-and-cvc)
* [Ve - Extension + Perspective + Essence](#ve)
* [Vi - Modifier role](#vi)
* [Vr - Pattern + Stem + Designation](#vr)

## Cf

Cf conveys Case-frame, Function, and Perspective.

| Cf            | `M` | `U` | `N` | `A` |
|---------------|:---:|:---:|:---:|:---:|
| `STA/FRM`     |  s  |  c  | sr  | cr  |
| `DYN/FRM`     | st  | ct  | str | ctr |
| `STA/FRM-IRG` | sp  | cp  | spr | cpr |
| `DYN/FRM-IRG` | sk  | ck  | skr | ckr |

Cf and CVn are easy to tell apart; CVn never has **s** or **c**, while Cf always begins with one of them.

## Cp

Cp specifies the information which follows a carrier word.

[TODO]

## CVm

CVm conveys a modifier. The consonantal portion of CVm is listed in the [modifiers lexicon](modifiers.md). The vocalic portion of CVm conveys type and degree.

| Vm     | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 | Degree 6 | Degree 7 | Degree 8 | Degree 9 |
|--------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| Type 1 |  iu/ui   |  ia/ua   |  io/uo   |  ie/ue   |    a     |    ei    |    oi    |    ai    |    au    |
| Type 3 |   aui    |   aua    |    oa    |    oe    |    o     |   aiu    |   aia    |   aio    |   aie    |
| Type 2 |   eie    |   eio    |   eia    |   eiu    |    e     |   oie    |   oio    |   oia    |   oiu    |

## CVn

CVn conveys Illocution, Validation, Function, and Perspective. It is split into two smaller affixes: CVn1 and CVn2.

### CVn1

CVn1 conveys Function.

| Perspective | CVn1 |
|-------------|:----:|
| `M`         | (h)  |
| `U`         |  f   |
| `N`         |  p   |
| `A`         |  k   |

The CVn1 value for `M` is **h** if CVn2 conveys `AXM` Axiomatic illocution; otherwise it is blank.

### CVn2

CVn2 conveys Illocution and Validation.

| Cn                              | `ASR` | `ALG` | `IPU` | `THR` | `EXV` | `AXM` | `DIR` | `IRG` | `ADM` | `HOR` | `DEC` |
|---------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `CNF` Confirmative              |  la   |  ra   |  ya   |   -   |   -   |   a   |  ria  |  rie  |  wa   |  rio  |  riu  |
| `AFM` Affirmative               |  le   |  re   |  ye   |   -   |   -   |   e   |   -   |   -   |  we   |   -   |   -   |
| `RPT` Reportative               |  li   |  ri   | yaui  |   -   |   -   |   i   |   -   |   -   |  wi   |   -   |   -   |
| `INF` Inferential               |  lo   |  ro   |  yo   |  lia  |  lie  |   o   |   -   |   -   |  wo   |   -   |   -   |
| `ITU` Intuitive                 |  lau  |  rau  |  yau  |  lio  |  liu  |  au   |   -   |   -   |  wau  |   -   |   -   |
| `PSM-TEN` Presumptive-Tentative |  lai  |  rai  |  yai  |   -   |   -   |  ai   |   -   |   -   |  wai  |   -   |   -   |
| `PSM-PUT` Presumptive-Putative  |  lei  |  rei  |  yei  |   -   |   -   |  ei   |   -   |   -   |  wei  |   -   |   -   |
| `PSM-DUB` Presumptive-Dubious   |  loi  |  roi  |  yoi  |   -   |   -   |  oi   |   -   |   -   |  woi  |   -   |   -   |
| `PPT-TEN` Purportive-Tentative  |  loa  |  roa  |  yoa  |   -   |   -   |  oa   |   -   |   -   |  woa  |   -   |   -   |
| `PPT-PUT` Purportive-Putative   |  loe  |  roe  |  yoe  |   -   |   -   |  oe   |   -   |   -   |  woe  |   -   |   -   |
| `PPT-DUB` Purportive-Dubious    |  lu   |  ru   |  yu   |   -   |   -   |   u   |   -   |   -   | waiu  |   -   |   -   |
| `IPB-TEN` Improbable-Tentative  |  lua  |  rua  |  yua  |   -   |   -   |  ua   |   -   |   -   |  wia  |   -   |   -   |
| `IPB-PUT` Improbable-Putative   |  lue  |  rue  |  yue  |   -   |   -   |  ue   |   -   |   -   |  wie  |   -   |   -   |
| `IPB-DUB` Improbable-Dubious    |  lui  |  rui  |  yui  |   -   |   -   |  ui   |   -   |   -   |  wiu  |   -   |   -   |

## CVr and Cs

CVr is any root from the [roots lexicon](roots.md). Cs is a predefined consonantal stem, which is listed for each root. The default value for Cs is **l**.

## Vc and CVc

Vc and CVc each convey Case. For nouns and framed verbs, the vocalic values are listed under [the Case section](morphology.md#case) in [Morphology](morphology.md). The consonantal portion of CVc is always **m**. For unframed verbs and integrated quotations [TODO], which carry no Case, Vc is **ə**.

## Ve

Ve conveys Perspective, Essence, and Context.

| Ve      | `EXS` Existential | `MTR` Metaphorical |
|---------|:-----------------:|:------------------:|
| `M/NRM` |        (a)        |       ia/ua        |
| `M/RPS` |        ai         |       ie/ue        |
| `U/NRM` |         e         |       io/uo        |
| `U/RPS` |        ei         |       iu/ui        |
| `N/NRM` |         o         |         oa         |
| `N/RPS` |        oi         |         oe         |
| `A/NRM` |        i/u        |        aia         |
| `A/RPS` |        au         |        aie         |

## Vi

Vi conveys the role of a detached modifier. Its values are listed under [the independent modifier section](morphophonology.md#independent-modifier) in [Morphophonology](morphophonology.md).
