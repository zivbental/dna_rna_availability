# YML131W
Status: ok. Length: 1321 nt. Measured usable bases: 637. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 637 | 0.3397 | 0.3412 |
| rnafold | ok | 637 | 0.2774 | 0.2458 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.4673 | -0.5163 |
| seed_p | 79 | -0.3541 | -0.4008 |
| seed_p_vs_seed_pars | 63 | -0.5076 | -0.4851 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
