# YML001W
Status: ok. Length: 766 nt. Measured usable bases: 573. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 573 | 0.2860 | 0.2657 |
| rnafold | ok | 573 | 0.2116 | 0.2119 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 444 | -0.1942 | -0.2226 |
| seed_p | 444 | -0.2090 | -0.2170 |
| seed_p_vs_seed_pars | 376 | -0.4428 | -0.3868 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
