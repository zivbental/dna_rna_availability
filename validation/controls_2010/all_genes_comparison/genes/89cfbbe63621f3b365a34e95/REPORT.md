# YJR013W
Status: ok. Length: 1301 nt. Measured usable bases: 656. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 656 | 0.2211 | 0.2175 |
| rnafold | ok | 656 | 0.2398 | 0.2363 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | 0.3804 | 0.3019 |
| seed_p | 102 | -0.2527 | -0.0630 |
| seed_p_vs_seed_pars | 72 | -0.5856 | -0.5031 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
