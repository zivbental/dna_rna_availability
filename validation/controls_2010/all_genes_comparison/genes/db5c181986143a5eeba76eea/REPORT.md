# YLL061W
Status: ok. Length: 1814 nt. Measured usable bases: 801. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 801 | 0.2666 | 0.2394 |
| rnafold | ok | 801 | 0.2610 | 0.2115 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.2949 | -0.0319 |
| seed_p | 84 | -0.1644 | -0.1548 |
| seed_p_vs_seed_pars | 55 | -0.4211 | -0.2622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
