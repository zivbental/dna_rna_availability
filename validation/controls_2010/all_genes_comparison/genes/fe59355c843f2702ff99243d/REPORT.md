# YNR022C
Status: ok. Length: 529 nt. Measured usable bases: 241. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 241 | 0.3224 | 0.3380 |
| rnafold | ok | 241 | 0.2627 | 0.2808 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.2273 | -0.4515 |
| seed_p | 70 | -0.5213 | -0.6516 |
| seed_p_vs_seed_pars | 47 | -0.3922 | -0.5496 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
