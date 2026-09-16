# YDR041W
Status: ok. Length: 778 nt. Measured usable bases: 348. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 348 | 0.3027 | 0.2911 |
| rnafold | ok | 348 | 0.3111 | 0.3105 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | -0.0206 | -0.1066 |
| seed_p | 88 | -0.1918 | -0.1782 |
| seed_p_vs_seed_pars | 54 | -0.7413 | -0.6550 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
