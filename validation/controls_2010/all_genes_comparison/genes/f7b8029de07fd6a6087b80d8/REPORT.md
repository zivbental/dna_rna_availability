# YER149C
Status: ok. Length: 1586 nt. Measured usable bases: 562. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 562 | 0.3989 | 0.4031 |
| rnafold | ok | 562 | 0.3598 | 0.3813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.2029 | -0.1519 |
| seed_p | 82 | -0.3921 | -0.3651 |
| seed_p_vs_seed_pars | 76 | -0.0798 | -0.0093 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
