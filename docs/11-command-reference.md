# 11. Current command reference

This page describes the CLI implemented in `rnavail/cli.py`. Run
`rnavail <command> --help` for the authoritative parser-generated list.

## Commands

| Command | Use it when | Result |
|---|---|---|
| `rnavail tools` | checking installation | all adapters, availability, versions and fix hints |
| `rnavail scan TARGET` | the location is unknown | tiles, screens, shortlists and deeply evaluates candidates |
| `rnavail evaluate TARGET --region SPEC` | locations are already known | deeply evaluates one or more named intervals |

There are no current partner-interaction, gate-design, CGMD or trajectory
planning commands. Recognition and partner fields declare the intended event;
they do not activate a binding calculation.

## Current defaults

| Setting | Default | Meaning |
|---|---:|---|
| molecule | RNA | selects RNA rather than DNA parameters |
| scan window | 25 nt | intended binder footprint |
| scan step | 1 nt | tests every start position |
| shortlist | 25 | non-overlapping candidates sent to the deep stage |
| displayed top | 10 | rows printed/rendered by default |
| seed length | 10 nt | exploratory nucleation subinterval |
| temperature | 37 °C | folding temperature |
| RNA parameters | Turner 2004 | nearest-neighbor energy set |
| dangling ends | model 2 | ViennaRNA dangling-end treatment |
| local pair span | 150 nt | longest pair allowed in RNAplfold |
| local window | 200 nt | neighborhood folded by RNAplfold |
| global pair span | unrestricted | whole-RNA calculations do not inherit the local cap |
| samples | 2,000 | Boltzmann structures drawn by `ensemble-sample` |
| visualization flank | 60 nt per side | context shown around each candidate |
| tools | every available adapter | use `--max-cost` or `--tools` to restrict |

Defaults are computational conveniences. In particular, the footprint must
match the physical binder rather than the table above.

## Minimal recipes

```bash
# Unknown location: scan the full expressed transcript.
rnavail scan transcript.fa --window 20 --keep 15 --save-run

# Known locations: one-based, inclusive coordinates.
rnavail evaluate transcript.fa \
  --region site_a:205-224 --region site_b:357-376 --save-run

# Complementary recognition with explicit seed logic and conditions.
rnavail scan transcript.fa --window 25 \
  --binder-class antisense_oligo --seed-length 8 --seed-mode any \
  --endpoint binding --temperature 37 --salt 0.15 \
  --condition-id buffer_A --save-run

# Add the two robustness criteria used by the default rank.
rnavail scan transcript.fa --window 25 \
  --robustness --length-robustness --save-run

# Add sequence and context warnings as well.
rnavail evaluate transcript.fa --region 205-229 \
  --ribosnitch --context-robustness --save-run
```

## Region syntax

`--region` accepts `205-224`, `name:205-224`, or a literal subsequence. It is
repeatable. Coordinates are one-based and inclusive; `205-224` has length 20.
For a multi-record FASTA, select a record with `--record`.

## Recognition options

| Option | What it declares |
|---|---|
| `--binder-class` | mechanism label; complementary classes can use seed ranking |
| `--partner-sequence` | partner identity/provenance, not an interaction calculation |
| `--partner-chemistry` | RNA, DNA or modified chemistry description |
| `--seed-mode` | `any`, 5′, 3′, fixed or listed allowed placement |
| `--seed-start` | one-based permitted start for fixed/listed mode |
| `--orientation` | partner orientation relative to the target |
| `--endpoint` | declared goal, such as structural opening, binding or cleavage |

Declaring `endpoint=binding` does not make the structural score a binding
probability. It documents what the user ultimately cares about and exposes
which assumptions remain unsupported.

## Folding options

`--temperature`, `--param-set`, `--dangles`, `--no-lonely-pairs`, `--no-gu`,
`--circular`, and compatible `--salt` settings modify the folding protocol.
`--max-bp-span` and `--window-size` apply to the local RNAplfold approximation.
`--global-max-bp-span` is a separate opt-in restriction for whole-RNA folds.

`--gquad` requests G-quadruplex-aware behavior where a backend can support it.
The current joint-opening implementations cannot enforce a G4-free forced-open
event safely, so unsupported combinations are refused rather than labeled as
corrected G4-aware probabilities. `gquad-scan` remains a propensity warning.

## Conditions: modeled versus recorded

| Field | Current structural handling |
|---|---|
| temperature | modeled by compatible folding engines |
| sodium/monovalent salt | modeled by compatible ViennaRNA paths |
| potassium | recorded, not separately modeled |
| total/free magnesium | recorded, not modeled |
| pH | recorded, not modeled |
| preparation and incubation | recorded, not modeled |
| partner concentration | recorded, not modeled |
| crowding agent/concentration | recorded, not modeled |
| organism, cell type, compartment | recorded, not modeled |

The report distinguishes “declared” from “applied.” This prevents metadata
from being mistaken for a physical correction.

## Experimental data

`--shape FILE` reads position/reactivity data. `--shape-method` selects
`deigan`, `zarringhalam`, or `eddy2`; DMS data require an explicit conversion.
Conversion parameters are exposed as `--shape-slope`, `--shape-intercept`, and
`--shape-beta`.

`--evidence JSON` adds validated, condition-linked annotations such as contact,
protein-interaction, ribosome, modification, variant or direct-hybridization
records. Evidence overlaps are reported but do not alter the uncalibrated
structural rank.

## Tool and uncertainty controls

- `--tools a,b,c` requests a named subset. Explicitly requested unavailable
  tools remain visible as skipped/failed records.
- `--max-cost N` limits the default selection by runtime class, not scientific
  importance.
- `--robustness` perturbs temperature, dangles, lonely-pair handling and local
  span/window settings; it supplies the scored model-spread criterion.
- `--length-robustness` varies the footprint by ±3 and ±6 nt; it supplies the
  scored length-spread criterion.
- `--ribosnitch` tries every single-base substitution inside each candidate.
- `--context-robustness` varies the amount of flanking sequence.
- `--samples` and `--sampling-seed` control the Monte Carlo diagnostic.

## Output and reproducibility

`--save-run` creates a timestamped directory containing text, JSON, TSV,
profile TSV where available, standalone HTML, and `meta.json`. `--no-html`
disables automatic HTML generation. `--visualize-flank` controls the context
in candidate figures.

`meta.json` records the command, target identity and hash, protocol,
recognition, condition, tools, failures, runtime and top candidates. The JSON
report is the complete machine-readable artifact; the rank table is only a
summary.

## Complete option index

This compact index names every long option accepted by `scan`; `evaluate`
shares the common options and replaces scan tiling options with repeatable
`--region`.

| Group | Options |
|---|---|
| input | `--record`, `--molecule`, `--seed-length` |
| scan tiling | `--window`, `--step`, `--keep`, `--screen-tool`, `--profile-tsv` |
| recognition | `--binder-class`, `--partner-sequence`, `--partner-chemistry`, `--seed-mode`, `--seed-start`, `--orientation`, `--endpoint` |
| folding | `--temperature`, `--param-set`, `--dangles`, `--max-bp-span`, `--global-max-bp-span`, `--window-size`, `--salt`, `--no-lonely-pairs`, `--no-gu`, `--gquad`, `--circular` |
| condition | `--condition-id`, `--potassium`, `--magnesium-total`, `--magnesium-free`, `--ph`, `--incubation-seconds`, `--preparation`, `--partner-concentration`, `--crowding-agent`, `--crowding-concentration`, `--organism`, `--cell-type`, `--compartment` |
| experimental data | `--shape`, `--shape-method`, `--probing-chemistry`, `--shape-slope`, `--shape-intercept`, `--shape-beta`, `--evidence` |
| tools and uncertainty | `--tools`, `--weights`, `--max-cost`, `--robustness`, `--ribosnitch`, `--context-robustness`, `--length-robustness`, `--samples`, `--sampling-seed` |
| output | `--json`, `--tsv`, `--top`, `--verbose`, `--quiet` |
| saved runs | `--save-run`, `--run-tag` |
| HTML | `--html`, `--no-html`, `--visualize-flank` |

`rnavail tools` additionally accepts `--json` to emit its inventory in
machine-readable form.

**See also:** [reading the output](06-outputs.md) and
[limitations](07-limitations.md).
