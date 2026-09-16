# YMR042W
Status: ok. Length: 665 nt. Measured usable bases: 386. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 386 | 0.2984 | 0.2882 |
| rnafold | ok | 386 | 0.2074 | 0.2174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | 0.4346 | 0.3985 |
| seed_p | 110 | 0.3020 | 0.4095 |
| seed_p_vs_seed_pars | 77 | 0.3312 | 0.3384 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
