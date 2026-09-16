# YBR196C
Status: ok. Length: 1846 nt. Measured usable bases: 1744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1744 | 0.3151 | 0.2991 |
| rnafold | ok | 1744 | 0.2597 | 0.2509 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1739 | -0.0448 | -0.1870 |
| seed_p | 1739 | -0.1316 | -0.2314 |
| seed_p_vs_seed_pars | 1693 | -0.2260 | -0.2369 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
