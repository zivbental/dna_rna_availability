# YGL070C
Status: ok. Length: 698 nt. Measured usable bases: 354. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 354 | 0.2748 | 0.2793 |
| rnafold | ok | 354 | 0.2677 | 0.2551 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.1630 | 0.3807 |
| seed_p | 101 | 0.2570 | 0.2213 |
| seed_p_vs_seed_pars | 65 | 0.1692 | -0.2115 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
