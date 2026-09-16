# YDR361C
Status: ok. Length: 1116 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.3247 | 0.3089 |
| rnafold | ok | 633 | 0.3451 | 0.3313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 279 | -0.2031 | -0.0308 |
| seed_p | 279 | -0.1879 | -0.0437 |
| seed_p_vs_seed_pars | 172 | -0.4732 | -0.3221 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
