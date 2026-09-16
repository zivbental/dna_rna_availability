# YMR093W
Status: ok. Length: 1709 nt. Measured usable bases: 1069. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1069 | 0.3117 | 0.3031 |
| rnafold | ok | 1069 | 0.2368 | 0.2459 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 454 | -0.1406 | -0.0682 |
| seed_p | 454 | -0.2564 | -0.1470 |
| seed_p_vs_seed_pars | 326 | -0.2604 | -0.1843 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
