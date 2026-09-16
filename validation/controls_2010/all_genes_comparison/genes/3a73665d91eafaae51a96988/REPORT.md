# YIL137C
Status: ok. Length: 2937 nt. Measured usable bases: 1501. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1501 | 0.2680 | 0.2601 |
| rnafold | ok | 1501 | 0.1801 | 0.1615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 276 | 0.0252 | -0.1922 |
| seed_p | 276 | -0.2784 | -0.2263 |
| seed_p_vs_seed_pars | 203 | -0.0792 | -0.0509 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
