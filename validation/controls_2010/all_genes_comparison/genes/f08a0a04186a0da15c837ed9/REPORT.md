# YLR397C
Status: ok. Length: 2343 nt. Measured usable bases: 1182. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1182 | 0.2990 | 0.3105 |
| rnafold | ok | 1182 | 0.2627 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.1464 | -0.0749 |
| seed_p | 206 | -0.2681 | -0.2641 |
| seed_p_vs_seed_pars | 165 | -0.3323 | -0.4104 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
