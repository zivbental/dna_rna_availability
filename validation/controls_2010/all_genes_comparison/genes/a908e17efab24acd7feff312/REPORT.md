# YOL026C
Status: ok. Length: 432 nt. Measured usable bases: 304. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 304 | 0.4170 | 0.4172 |
| rnafold | ok | 304 | 0.3858 | 0.4000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 181 | -0.2910 | -0.1283 |
| seed_p | 181 | -0.2862 | -0.2744 |
| seed_p_vs_seed_pars | 164 | -0.2790 | -0.1174 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
