# YDR347W
Status: ok. Length: 1167 nt. Measured usable bases: 619. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 619 | 0.3510 | 0.3355 |
| rnafold | ok | 619 | 0.3227 | 0.3294 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 194 | -0.0164 | 0.0020 |
| seed_p | 194 | -0.1507 | -0.1002 |
| seed_p_vs_seed_pars | 140 | -0.3069 | -0.1348 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
