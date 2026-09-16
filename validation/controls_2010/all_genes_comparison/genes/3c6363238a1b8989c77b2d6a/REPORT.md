# YPL002C
Status: ok. Length: 885 nt. Measured usable bases: 398. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 398 | 0.2867 | 0.2847 |
| rnafold | ok | 398 | 0.1093 | 0.0980 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.6793 | 0.3940 |
| seed_p | 66 | 0.5820 | 0.4673 |
| seed_p_vs_seed_pars | 58 | 0.6840 | 0.4291 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
