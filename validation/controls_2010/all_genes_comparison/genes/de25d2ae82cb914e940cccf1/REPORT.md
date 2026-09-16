# YDL167C
Status: ok. Length: 2355 nt. Measured usable bases: 972. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 972 | 0.2744 | 0.2510 |
| rnafold | ok | 972 | 0.2851 | 0.2804 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | 0.3287 | 0.3898 |
| seed_p | 110 | -0.2988 | -0.0936 |
| seed_p_vs_seed_pars | 88 | -0.3332 | -0.0099 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
