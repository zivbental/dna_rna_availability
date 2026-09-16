# YAR002W
Status: ok. Length: 1746 nt. Measured usable bases: 916. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 916 | 0.3352 | 0.3292 |
| rnafold | ok | 916 | 0.2545 | 0.2613 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 234 | 0.2143 | 0.2870 |
| seed_p | 234 | 0.0368 | 0.0147 |
| seed_p_vs_seed_pars | 181 | 0.0044 | -0.0916 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
