# YPL262W
Status: ok. Length: 1556 nt. Measured usable bases: 1229. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1229 | 0.3367 | 0.3194 |
| rnafold | ok | 1229 | 0.2927 | 0.2876 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 982 | -0.0199 | 0.0200 |
| seed_p | 982 | -0.0220 | -0.0176 |
| seed_p_vs_seed_pars | 864 | -0.1725 | -0.0780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
