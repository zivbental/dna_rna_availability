# YJR091C
Status: ok. Length: 3457 nt. Measured usable bases: 1486. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1486 | 0.3039 | 0.2859 |
| rnafold | ok | 1486 | 0.2641 | 0.2467 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | -0.2564 | -0.3626 |
| seed_p | 147 | -0.1669 | -0.2541 |
| seed_p_vs_seed_pars | 109 | -0.2141 | -0.4885 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
