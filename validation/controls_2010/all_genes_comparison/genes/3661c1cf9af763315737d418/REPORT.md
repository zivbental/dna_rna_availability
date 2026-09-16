# YML126C
Status: ok. Length: 1476 nt. Measured usable bases: 614. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 614 | 0.3357 | 0.3365 |
| rnafold | ok | 614 | 0.2155 | 0.2218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 569 | -0.1847 | -0.1600 |
| seed_p | 569 | -0.3263 | -0.2931 |
| seed_p_vs_seed_pars | 483 | -0.4515 | -0.4380 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
