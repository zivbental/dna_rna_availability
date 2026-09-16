# YCR009C
Status: ok. Length: 922 nt. Measured usable bases: 642. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 642 | 0.3323 | 0.3151 |
| rnafold | ok | 642 | 0.2703 | 0.2668 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 423 | 0.0752 | -0.0517 |
| seed_p | 423 | -0.0177 | -0.0863 |
| seed_p_vs_seed_pars | 345 | -0.1281 | -0.1515 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
