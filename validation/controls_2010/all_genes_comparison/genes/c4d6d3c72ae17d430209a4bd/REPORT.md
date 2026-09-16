# YCR047C
Status: ok. Length: 1063 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.3888 | 0.3886 |
| rnafold | ok | 522 | 0.3648 | 0.3560 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 113 | -0.0601 | -0.5575 |
| seed_p | 113 | -0.2896 | -0.4305 |
| seed_p_vs_seed_pars | 53 | -0.2376 | 0.2329 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
