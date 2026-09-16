# YDL171C
Status: ok. Length: 6585 nt. Measured usable bases: 3410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3410 | 0.3597 | 0.3426 |
| rnafold | ok | 3410 | 0.2819 | 0.2790 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 774 | -0.1132 | -0.2780 |
| seed_p | 774 | -0.2363 | -0.2494 |
| seed_p_vs_seed_pars | 589 | -0.3270 | -0.2972 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
