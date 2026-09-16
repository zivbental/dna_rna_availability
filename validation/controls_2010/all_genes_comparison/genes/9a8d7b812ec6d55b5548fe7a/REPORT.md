# YGL256W
Status: ok. Length: 1591 nt. Measured usable bases: 968. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 968 | 0.2929 | 0.2922 |
| rnafold | ok | 968 | 0.1411 | 0.1503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 380 | -0.2731 | -0.3637 |
| seed_p | 380 | -0.3113 | -0.2491 |
| seed_p_vs_seed_pars | 280 | -0.2562 | -0.0598 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
