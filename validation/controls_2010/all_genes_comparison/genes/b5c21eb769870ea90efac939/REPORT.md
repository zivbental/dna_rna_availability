# YER056C
Status: ok. Length: 1778 nt. Measured usable bases: 1311. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1311 | 0.3639 | 0.3354 |
| rnafold | ok | 1311 | 0.3088 | 0.2871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1047 | -0.0218 | -0.0477 |
| seed_p | 1047 | -0.2182 | -0.1961 |
| seed_p_vs_seed_pars | 842 | -0.4602 | -0.4074 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
