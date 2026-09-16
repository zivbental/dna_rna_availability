# YDL181W
Status: ok. Length: 433 nt. Measured usable bases: 211. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 211 | 0.3873 | 0.3735 |
| rnafold | ok | 211 | 0.2671 | 0.2664 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | -0.0439 | 0.2591 |
| seed_p | 59 | -0.0453 | -0.2262 |
| seed_p_vs_seed_pars | 44 | 0.0154 | -0.0780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
