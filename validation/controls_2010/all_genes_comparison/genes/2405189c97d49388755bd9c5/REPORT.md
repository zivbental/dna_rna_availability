# YGR094W
Status: ok. Length: 3479 nt. Measured usable bases: 2666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2666 | 0.3621 | 0.3372 |
| rnafold | ok | 2666 | 0.2720 | 0.2536 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2096 | -0.1235 | -0.0614 |
| seed_p | 2096 | -0.2562 | -0.1330 |
| seed_p_vs_seed_pars | 1674 | -0.4512 | -0.3325 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
