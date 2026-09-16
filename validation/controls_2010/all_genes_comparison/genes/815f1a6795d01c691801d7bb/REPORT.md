# YAL026C
Status: ok. Length: 4282 nt. Measured usable bases: 1688. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1688 | 0.3220 | 0.3014 |
| rnafold | ok | 1688 | 0.2492 | 0.2288 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | -0.1807 | -0.1881 |
| seed_p | 128 | -0.1679 | -0.2669 |
| seed_p_vs_seed_pars | 61 | -0.9076 | -0.6917 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
