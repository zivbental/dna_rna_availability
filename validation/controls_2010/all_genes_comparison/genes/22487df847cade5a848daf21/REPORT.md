# YDR414C
Status: ok. Length: 1388 nt. Measured usable bases: 699. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 699 | 0.1790 | 0.1683 |
| rnafold | ok | 699 | 0.1505 | 0.1443 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | 0.0342 | 0.0603 |
| seed_p | 126 | 0.2257 | 0.1543 |
| seed_p_vs_seed_pars | 88 | 0.1500 | 0.4318 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
