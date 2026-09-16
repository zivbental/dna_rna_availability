# YML121W
Status: ok. Length: 1250 nt. Measured usable bases: 526. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 526 | 0.2881 | 0.2831 |
| rnafold | ok | 526 | 0.2903 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.2736 | -0.1735 |
| seed_p | 79 | 0.1103 | 0.1933 |
| seed_p_vs_seed_pars | 48 | -0.3762 | -0.1024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
