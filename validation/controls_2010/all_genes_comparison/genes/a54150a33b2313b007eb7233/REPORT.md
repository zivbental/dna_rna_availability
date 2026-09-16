# YGR079W
Status: ok. Length: 1205 nt. Measured usable bases: 546. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 546 | 0.3852 | 0.3518 |
| rnafold | ok | 546 | 0.2580 | 0.2365 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.0511 | 0.0348 |
| seed_p | 166 | -0.1538 | -0.0535 |
| seed_p_vs_seed_pars | 134 | -0.3819 | -0.2466 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
