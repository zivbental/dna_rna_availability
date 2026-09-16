# YDL157C
Status: ok. Length: 528 nt. Measured usable bases: 249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 249 | 0.4213 | 0.4287 |
| rnafold | ok | 249 | 0.2009 | 0.2087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.8784 | -0.7796 |
| seed_p | 51 | -0.8631 | -0.6709 |
| seed_p_vs_seed_pars | 31 | -0.7263 | -0.5378 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
