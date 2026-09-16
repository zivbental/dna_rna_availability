# YCR008W
Status: ok. Length: 2201 nt. Measured usable bases: 1010. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1010 | 0.3468 | 0.3209 |
| rnafold | ok | 1010 | 0.3059 | 0.2862 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 154 | 0.2157 | 0.2050 |
| seed_p | 154 | 0.4708 | 0.2959 |
| seed_p_vs_seed_pars | 122 | 0.2220 | 0.0872 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
