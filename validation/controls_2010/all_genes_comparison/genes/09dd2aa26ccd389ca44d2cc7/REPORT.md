# YOR167C
Status: ok. Length: 318 nt. Measured usable bases: 237. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 237 | 0.2353 | 0.2136 |
| rnafold | ok | 237 | 0.2313 | 0.2024 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | -0.3117 | -0.1960 |
| seed_p | 178 | -0.5010 | -0.5415 |
| seed_p_vs_seed_pars | 169 | -0.6579 | -0.6926 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
