# YLL013C
Status: ok. Length: 3240 nt. Measured usable bases: 1125. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1125 | 0.2206 | 0.2023 |
| rnafold | ok | 1125 | 0.2087 | 0.2052 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | 0.0025 | 0.3429 |
| seed_p | 102 | 0.1007 | 0.1805 |
| seed_p_vs_seed_pars | 78 | 0.0557 | 0.0812 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
