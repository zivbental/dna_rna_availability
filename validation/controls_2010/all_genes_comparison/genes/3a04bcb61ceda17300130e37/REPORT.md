# YMR153W
Status: ok. Length: 1618 nt. Measured usable bases: 807. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 807 | 0.3858 | 0.3825 |
| rnafold | ok | 807 | 0.3010 | 0.3084 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.4663 | -0.4184 |
| seed_p | 150 | -0.3541 | -0.3821 |
| seed_p_vs_seed_pars | 127 | -0.0307 | 0.0122 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
