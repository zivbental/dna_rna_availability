# YAL039C
Status: ok. Length: 897 nt. Measured usable bases: 408. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 408 | 0.3587 | 0.3619 |
| rnafold | ok | 408 | 0.2802 | 0.3070 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | 0.3002 | 0.0530 |
| seed_p | 91 | -0.0996 | -0.0555 |
| seed_p_vs_seed_pars | 62 | -0.5694 | -0.4900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
