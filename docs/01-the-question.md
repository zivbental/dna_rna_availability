# 1. The question this repository answers

*No molecular biology assumed. If you already know what a hairpin is, skim to
[1.4](#14-the-mistake-this-tool-exists-to-prevent).*

---

## 1.1 A thirty-second biology primer

RNA is a chain of four kinds of unit — **A**, **C**, **G**, **U** — strung
together in a line. That line is the *sequence*, and it is what you get from
a database or a synthesis order:

```
AUGAGUAAAGGAGAAGAACUUUUCACUGGAGUUGUCCCAAUU...
```

But RNA does not stay a line. Certain units stick to certain others — **A**
pairs with **U**, **G** pairs with **C** (and, more weakly, **G** with
**U**) — so a single strand folds back on itself and glues to itself wherever
it finds a complementary stretch. The result is a shape:

```
        loop
      A     A
     A       A          the stem: paired, stuck shut
      G-----C
      G-----C
      C-----G
      A-----U
  ----        ----      the rest of the molecule
```

That is a **hairpin**: a stem where the strand has paired with itself, and a
loop where it has not. A real RNA is a landscape of stems, loops, bulges and
junctions, all formed by the molecule sticking to itself.

Crucially, an RNA molecule is not frozen in one shape. It jiggles between
many shapes, constantly. At body temperature it is better to think of it as a
*statistical cloud* of shapes — some common, some rare — than as a single
picture. Physicists call that cloud the **ensemble**, and the tools in this
repository are, almost all of them, machines for reasoning about it.

## 1.2 The practical problem

Suppose you want something to stick to a specific stretch of an RNA. That
"something" might be:

| What you're designing | How long a stretch it needs |
|---|---|
| An antisense oligo (to knock the RNA down) | 15–25 units |
| A toehold switch trigger (synthetic biology) | 20–30 units |
| A CRISPR guide (sgRNA spacer) | 20 units |
| A PCR or reverse-transcription primer | 18–25 units |
| A microRNA seed | 6–8 units |

In every case the plan is the same: pick a stretch of the target, design
something complementary to it, and let base pairing do the rest.

Here is the catch, and it is the entire reason this repository exists:

> **A stretch being present in the sequence does not mean it is available to
> bind.**

If your chosen stretch is buried inside a stem — already stuck to another
part of the same molecule — then your oligo, guide or trigger arrives to find
the site occupied. It cannot pair with something that is already paired. The
site is *there* and it is *useless*.

So the real question is not "where is this stretch?" It is:

> **How often is this stretch actually open?**

## 1.3 Turning that into a number

Because the molecule is a cloud of shapes rather than one shape, "is it
open?" has a probabilistic answer. For a stretch running from position *i* to
position *j*, define:

```
P_unpaired(i, j)  =  the probability that every position from i to j
                     is simultaneously unpaired
```

That is a number between 0 and 1. A site with `P_unpaired = 0.9` is open
nine times out of ten. One with `P_unpaired = 0.000001` is essentially never
open.

Probabilities that span many orders of magnitude are awkward to compare, so
the same fact is usually expressed as an energy — the thermodynamic work you
would have to do to force the site open:

```
dG_open(i, j)  =  −RT · ln P_unpaired(i, j)
```

where `R` is the gas constant and `T` the temperature (`RT ≈ 0.616 kcal/mol`
at 37 °C). The convenient property of this form is that it is **additive**
and reported in familiar units: **kcal/mol**, low is good.

| `P_unpaired` | `dG_open` | Reading |
|---|---|---|
| 0.9 | 0.06 kcal/mol | essentially free to open |
| 0.1 | 1.4 kcal/mol | opens readily |
| 0.001 | 4.3 kcal/mol | costly |
| 10⁻⁶ | 8.5 kcal/mol | effectively shut |

`rnavail` is, at its core, a machine for estimating `P_unpaired` and
`dG_open` for candidate sites — carefully, across explicitly labeled model
scopes and adapter capabilities, and with an honest account of how much the
answer depends on assumptions nobody can defend exactly.

## 1.4 The mistake this tool exists to prevent

There is a tempting shortcut that is wrong, and it is wrong by a *lot*.

The shortcut: ask, for each individual position, "how often is *this one
base* unpaired?", then average those numbers across your stretch. Call that
the **per-base** or *marginal* view. It is easy to compute and every folding
program gives it to you.

For an endpoint that requires the complete footprint to be available before
association, the problem is that a binding partner does not need each base
open *at some point*. It needs the whole footprint open **at the same
moment**. Those are different questions, and they can differ enormously. A
complementary strand can sometimes initiate through a shorter seed instead;
that is a distinct declared event, not a reason to substitute marginal
per-base probabilities for either joint quantity.

A worked example from this repository's own test molecule (`tests/test_adapters.py`),
region 9–20:

```
mean per-base unpaired      0.81       "81% open — looks great"
joint P_unpaired(9,20)      0.00026    "open all at once 1 time in 3800"
```

A factor of **three thousand**. Both numbers are correct; they answer
different questions. The first says each nucleotide spends most of its time
free. The second says they are *never free together* — the region breathes,
but the different parts of it breathe at different times.

The analogy: a row of twenty parking spaces, each empty 81% of the day. If
you need one space, you will always find one. If you need all twenty
simultaneously for a truck, you will never get them.

On a real transcript this is not a curiosity, it changes the answer. Ranking
every 20-nt window of a bacterial GFP transcript both ways:

- Spearman rank correlation between the two rankings: **0.74**
- Overlap of their top-20 site lists: **10 of 20**
- Worst single position (85): per-base view overstates availability by a
  factor of **5.5 × 10⁷**

So the per-base number gets you roughly half the right answer, with no
warning about which half. `rnavail` computes both, ranks on the **joint**
one, reports the per-base one as a *diagnostic only*, and prints an explicit
note whenever the two diverge for a candidate.

## 1.5 Nucleation: why a buried site can still work

One refinement keeps the picture honest in the other direction.

Binding does not happen all at once. A partner strand makes contact over a
few bases first — **nucleation** — and if that toehold holds, the pairing
zips outward from there, prying the rest of the site open as it goes. The
energy released by each new pair pays for opening the next one.

This means a site whose *full* footprint is essentially never open can still
be a perfectly good target, provided some shorter stretch inside it opens
reliably. That shorter stretch is the **seed**.

So `rnavail` reports two accessibility numbers per candidate:

- `p_unpaired` — the whole site open at once (the strict requirement)
- `seed_p_unpaired` — the best short window inside it (the nucleation
  requirement, default 10 nt, `--seed-length`)

and when the two diverge sharply it says so:

> *the full 20 nt site is far less available (P=0.0033) than its best seed
> (P=0.44); a toehold-style design that only needs to nucleate here is much
> more plausible than one requiring the whole site open at once*

Seed accessibility carries the largest single weight in the composite score
(2.0 of 6.0) for exactly this reason: a site that cannot nucleate cannot be
rescued by anything downstream.

## 1.6 What this tool does *not* answer

This matters as much as what it does answer, and the boundary is deliberate.

**`rnavail` answers a single-molecule question.** Given one sequence and a
region within it, it estimates how open that region is *within that
molecule's own folded structure*. It does **not** predict whether some other
specific RNA will bind there.

That second question — RNA–RNA interaction prediction — is a genuinely harder
and still largely unsolved problem. Adapters for it (IntaRNA, RNAup,
RNAduplex/RNAcofold, OligoWalk) were built here, worked, and were removed
once the scope was deliberately fixed to the single-molecule question.

The practical consequence: **an open site is necessary, not sufficient.** A
top-ranked candidate here is a shortlist entry — "this site is physically
reachable" — not a validated design. Whether your particular oligo binds it,
and binds it in preference to somewhere else, is a separate question this
tool does not attempt.

See [7. Limitations](07-limitations.md) for the full list of what is out of
reach and why.

---

**Next:** [2. How it works, end to end](02-pipeline.md) — the top-down walk
through every step from a FASTA file to a ranked list.
