# YPL214C
Status: ok. Length: 1721 nt. Measured usable bases: 827. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 827 | 0.3610 | 0.3540 |
| rnafold | ok | 827 | 0.2303 | 0.2179 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.2198 | -0.4614 |
| seed_p | 180 | -0.1975 | -0.2436 |
| seed_p_vs_seed_pars | 136 | -0.0367 | -0.1204 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
