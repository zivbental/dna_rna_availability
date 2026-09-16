# YDR363W-A
Status: ok. Length: 369 nt. Measured usable bases: 207. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 207 | 0.4345 | 0.4476 |
| rnafold | ok | 207 | 0.4472 | 0.4577 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | -0.6706 | -0.7779 |
| seed_p | 87 | -0.7903 | -0.8309 |
| seed_p_vs_seed_pars | 53 | -0.7485 | -0.6759 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
