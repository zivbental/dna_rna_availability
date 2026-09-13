# 6. Reading the output

What each file contains, and how to actually read a report.

---

## 6.1 The files

Every run can produce six things. `--save-run` writes all of them into a
timestamped directory; individual flags write them wherever you point.

| File | Flag | One row / section per | Use it for |
|---|---|---|---|
| terminal output, `report.txt` | (default) | candidate | reading now |
| `report.json` | `--json FILE` | everything | any downstream analysis |
| `report.tsv` | `--tsv FILE` | candidate | spreadsheets, plotting |
| `report.profile.tsv` | `--profile-tsv FILE` | **position** | whole-transcript tracks |
| `report.html` | `--html FILE` | candidate + transcript | looking at it |
| `meta.json` | (with `--save-run`) | run | provenance |

### Run directories

```bash
rnavail scan transcript.fa --window 20 --keep 10 --save-run --run-tag first-pass
# run saved to runs/20260906-161118-first-pass/
```

Each invocation gets `runs/<timestamp>[-tag]/`. Two runs in the same second
get a numeric suffix rather than one overwriting the other, and
`runs/latest` is a symlink to the most recent — so `cat runs/latest/report.txt`
always shows the last thing you ran.

`meta.json` records the exact command line, the input files, the folding
protocol, which tools ran/failed/were skipped, the wall-clock duration, and
the top candidates at a glance. It also records target SHA-256, recognition
and condition declarations, and source revision availability. It is what
makes a run reproducible three months later.

---

## 6.2 The text report

```
==============================================================================
rnavail scan: gfpuv  (717 nt, RNA, GC 41.0%)
protocol: T37/turner2004/d2/L150/W200/GLall
recognition: antisense_oligo; seed any / 10 nt; endpoint structural_opening
condition: buffer-A; 37 °C; preparation heat_refolded
probing: SHAPE / deigan; coverage 82%; probing:deigan:…
evidence tracks: 1; annotation only; condition status matched
============================================================================== 

tools that ran (11): rnaplfold, gquad-scan, rnaplfold, rnaplfold-cli, ...
tools that failed:
   kinwalker: RuntimeError: sequence is 717 nt; kinwalker's runtime explodes...

screened 698 windows, kept 10 for detailed analysis
```

The **protocol line** is the folding-model signature. `L150/W200` is the
local RNAplfold span/window and `GLall` means whole-sequence calculations were
unrestricted; a finite `GL…` value is an explicit global span limit. Compare
runs only when their relevant protocol, recognition specification, condition,
and probing track/conversion are comparable.

The recognition and condition lines state the requested event and environment.
They do not mean that every declared field was modelled. `-v` lists the
settings each tool applied or rejected, and the JSON report lists unmodelled
recognition or environmental assumptions explicitly. The probing line appears
only when a track was supplied.

An **evidence tracks** line appears when `--evidence` was supplied. The JSON
root holds the complete source tracks, while each candidate lists only
overlapping records in `biological_evidence`, with `matched`,
`different_condition`, or `unverified` status. These records are displayed as
annotations: their presence does not change `heuristic_rank_score` and does
not establish occupancy, blocking, or a binding effect.

**Tools that failed or were skipped are always listed, with the reason.** A
missing binary or a refused calculation costs one row, never the run, and it
is never silent.

### The ranked table

```
      region      len     rank    seedP    P_unp   dGopen    dG/nt
        w205       20    1.000    0.975    0.934     0.04     0.00
        w357       20    0.953    0.335    0.025     2.47     0.12
         w11       20    0.952    0.427 8.52e-03     3.08     0.15
```

| Column | Meaning |
|---|---|
| `region` | `w205` = the 20-nt window starting at position 205 |
| `rank` | `heuristic_rank_score`, 0–1, higher is preferred ([5.2](05-consensus-and-scoring.md#52-turning-metrics-into-a-score)); it is not a binding or function probability |
| `seedP` | probability the selected seed is open for complementary or exploratory recognition; `-` when seed nucleation is diagnostic only |
| `P_unp` | probability the **whole** site is open at once — the strict requirement |
| `dGopen` | the same thing as an energy, kcal/mol, lower is better |
| `dG/nt` | length-normalised, so sites of different length are comparable |

The two probability columns are the ones to read together. `seedP` ≫ `P_unp`
means a toehold-style design is plausible where a full-footprint one is not.
For a non-complementary binder class, this inference is intentionally absent:
the report records `detail.recognition_scoring` and leaves seed-derived rank
criteria out of the heuristic rank.

### The notes

Below the table, each candidate gets its diagnoses — the sentences that
change what you would do next:

```
w457  ACGGCAGACAAACAAAAGAA
   heuristic rank score 0.4040 (coverage 85% of scoring weight)
   primary opening: vienna-exact / global_ensemble; P=0.0246, dG=3.50;
     unconditioned
   - the windowed engines (RNAplfold) report an opening cost 3.3 kcal/mol
     lower than the whole-sequence calculation — inspect the local/global
     protocol difference before treating either value as decisive
   - a single point mutation can move the opening cost by 7.1 kcal/mol
     (position 332, A→G is the worst case); this is a riboSNitch candidate
```

**`coverage`** is the fraction of the intended scoring weight that actually
had data behind it. 88% means one criterion was missing — usually a sweep you
did not enable.

The **primary opening** line identifies the one coherent source for the
candidate's displayed `P_unp`, `dGopen`, and selected seed values. It prevents
a probability from one tool and an energy from another being shown as if they
were one observation. Other tool values remain available as consensus and raw
tool rows.

### `-v` adds the derivation

Two extra blocks per candidate. **Score components** — which criteria
produced the number:

```
   score components:
      seed accessibility                     value=0.6435  desirability=1.000 weight=2.0
      opening cost per nucleotide            value=0.1748  desirability=0.869 weight=1.5
      robustness across window length        value=0.1497  desirability=0.002 weight=0.75
      not scored (no data): dg_open_spread
```

A desirability of 1.000 means that criterion is pinned at its anchor and is
doing no ranking work for this candidate — see the saturation warning in
[5.5](05-consensus-and-scoring.md#55-checks-the-run-makes-on-itself).

**Cross-tool agreement** — who reported what, and whether they agreed:

```
   cross-tool agreement:
      dg_open: median 3.496 kcal/mol across 2 independent measurements, 3
         tools (spread 3.273) [rnaplfold=1.859, rnaplfold-cli=1.859,
         vienna-exact=5.133]
```

Read **"2 independent measurements, 3 tools"** as: three tools reported, but
two of them are the same calculation ([5.1](05-consensus-and-scoring.md#51-four-gates-before-any-averaging)),
so only two declared calculation groups stand behind the median. A large `spread` is
the honest signal that the site is model-dependent.

When a requested setting is material but unsupported by an adapter, its raw
result remains under `tool_results`; it is named in the candidate consensus as
`excluded_for_protocol` and is not pooled into a compatible probability
median. The same separation applies to incompatible probing conditioning.

Where a metric mixes kinds of number, the excluded ones are named:

```
      not blended into the median (different estimand): contrafold (posterior),
      eternafold (posterior), linearfold (single_structure),
      probknot (single_structure)
```

### Warnings

Run-level issues are collected at the bottom: sweep frame caveats, saturated
scoring criteria, sampling limits, ambiguous input bases.

---

## 6.3 The HTML report

`--html FILE`, or automatically with `--save-run`. A single self-contained
file — every image is an embedded base64 PNG, so there is no companion
directory and it survives being emailed.

**Top: whole-transcript accessibility** *(scan only)*

- **the profile** — `dG_open/nt` for a window starting at every position,
  single-nucleotide resolution regardless of `--step`, with the ranked
  candidates shaded. The valleys are the accessible regions.
- **the landscape** — the same quantity over every *(start position, window
  length)* pair. **A vertical streak** is a site cheap to open across many
  lengths: a broad, robust element you could target with almost any binder
  footprint. **An isolated fleck** is accessible at one specific length only.
  Grey is "not computed at that combination" (too close to a sequence end for
  that length to fit).

**Then: the ranked summary table**, same columns as the text report.

**Then: one card per candidate**, containing

1. the subsequence and its heuristic-rank badge
2. a **properties table** — up to 16 metrics, whichever the candidate has
3. the **notes**
4. a **score breakdown** — exactly which criteria fed the score, each with its
   value, a desirability bar, and its weight, plus anything not scored
5. two images: a **base-pair probability heatmap** and a **2D structure
   diagram**, both for the candidate folded with ±`--visualize-flank` nt of
   context (default 60), because a bare site folded in isolation would remove
   exactly the neighbouring sequence that might bury or expose it

Structure layouts come from ViennaRNA's own naview engine — the same one
behind RNAplot — not a bespoke approximation.

Rendering needs matplotlib (`pip install -e .[viz]`). Without it the HTML is
skipped with a warning rather than failing the run.

---

## 6.4 `report.json` — everything

The complete record, and the right input for any downstream analysis.

```
{
  "report_schema_version": "2.0",
  "mode": "scan",
  "sequence": {"name", "length", "molecule", "gc_fraction", "sha256"},
  "settings": {...}, "protocol": "T37/turner2004/d2/L150/W200/GLall",
  "recognition_spec_id": "recognition:…",
  "recognition": {...}, "condition": {...}, "probing": {...},
  "evidence_tracks": [{"evidence_type", "condition_id", "sequence_hash", "records": [...]}],
  "tools": {"ran": [...], "failed": [...], "skipped": [...]},
  "candidates": [
    {
      "region": {"start", "end", "length", "name"},
      "subsequence": "...",
      "metrics": {"p_unpaired": 0.0246, ...},        # the flattened values
      "consensus": {                                   # the full derivation
        "p_unpaired": {
          "median", "spread", "n_tools", "n_eligible", "n_primary", "n_independent",
          "by_tool": {"rnaplfold": 0.04895, "vienna-exact": 0.0002417, ...},
          "groups": {...}, "eligible_for_primary": [...],
          "primary_for_median": [...], "excluded_from_median": {...},
          "excluded_for_conditioning": {...},
          "excluded_for_protocol": {...}
        }
      },
      "heuristic_rank_score": 0.404,
      "score": {"heuristic_rank_score", "coverage", "components": [...], "missing_metrics": [...]},
      "primary_opening_observation_id": "…",
      "opening_observations": [...], "biological_evidence": [...],
      "notes": [...], "detail": {...}
    }
  ],
  "tool_results": [ ... every raw per-region value from every adapter ... ],
  "warnings": [...],
  "detail": {"profile": {...}, "score_saturation": {...}, "length_sweep": {...}, ...}
}
```

`consensus[metric].by_tool` holds every successful raw adapter value. Its
`eligible_for_primary` and `primary_for_median` lists show which of those
values could answer the requested conditioning and protocol, then which could
enter the estimand-compatible median. A raw value excluded for conditioning or
protocol remains inspectable without silently becoming a fallback estimate;
if none are compatible, the median is `null`. Seed placements live in
`tool_results[].regions[region].detail.seed_trials`; exact-budget-skipped,
censored, and sampling-bound trials remain distinguishable there.

---

## 6.5 The TSV files

`report.tsv` — one row per candidate, one column per metric, sorted by rank.
Straight into a spreadsheet or pandas.

`report.profile.tsv` — one row per **position** (scan only):

```
start   end   dg_open_per_nt_window20
1       20    0.0992399
2       21    0.098572
3       22    0.130203
```

The whole-transcript accessibility track as plain numbers, at
single-nucleotide resolution, for plotting alongside your own annotations.

---

## 6.6 A worked reading

From a real GFP run:

```
w457  ACGGCAGACAAACAAAAGAA          heuristic rank 0.404, coverage 88%
   seedP 0.6435    P_unp 0.0246    dGopen 3.50    dG/nt 0.175
```

- **`seedP` 0.64 but `P_unp` 0.025** — the best 10-nt seed is open two thirds
  of the time, the full 20-nt site only 2.5%. Nucleation is plausible; a
  design requiring the whole footprint open at once is not.
- **the windowed-vs-exact note fired at 3.3 kcal/mol** — `rnaplfold` says
  1.86, `vienna-exact` says 5.13. This is a local/global scope disagreement:
  it can be consistent with long-range pairing, but does not establish a
  mechanism or identify which estimate is physically correct.
- **riboSNitch at 7.1 kcal/mol** — one substitution at position 332 moves the
  answer by more than the answer itself. If this target has population
  variation, verify the actual sequence.
- **coverage 88%** — one scoring criterion had no data.

Verdict: a seed-only design worth considering, with a sequence-verification
caveat, and worth re-checking on the full construct rather than the bare CDS.

---

**Next:** [7. Limitations](07-limitations.md) — what this cannot tell you.
