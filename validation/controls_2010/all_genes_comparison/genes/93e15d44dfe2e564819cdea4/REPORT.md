# YGR105W
Status: ok. Length: 454 nt. Measured usable bases: 226. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 226 | 0.2616 | 0.2546 |
| rnafold | ok | 226 | 0.2778 | 0.2928 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | 0.0422 | 0.0234 |
| seed_p | 137 | -0.4625 | -0.4255 |
| seed_p_vs_seed_pars | 110 | -0.2779 | -0.2944 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
