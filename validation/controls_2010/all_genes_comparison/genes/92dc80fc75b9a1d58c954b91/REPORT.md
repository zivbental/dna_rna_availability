# YMR149W
Status: ok. Length: 1020 nt. Measured usable bases: 763. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 763 | 0.2638 | 0.2484 |
| rnafold | ok | 763 | 0.2373 | 0.2332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 710 | -0.2255 | -0.1865 |
| seed_p | 710 | -0.2704 | -0.2359 |
| seed_p_vs_seed_pars | 604 | -0.3456 | -0.2788 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
