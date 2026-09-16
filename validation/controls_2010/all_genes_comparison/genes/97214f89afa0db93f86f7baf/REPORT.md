# YNL156C
Status: ok. Length: 1174 nt. Measured usable bases: 638. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 638 | 0.2693 | 0.2817 |
| rnafold | ok | 638 | 0.2702 | 0.2770 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 250 | 0.2199 | 0.0819 |
| seed_p | 250 | -0.1504 | -0.1559 |
| seed_p_vs_seed_pars | 216 | -0.0511 | -0.0004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
