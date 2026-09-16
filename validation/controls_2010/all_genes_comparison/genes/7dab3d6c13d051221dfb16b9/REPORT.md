# YNR036C
Status: ok. Length: 609 nt. Measured usable bases: 424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 424 | 0.3576 | 0.3449 |
| rnafold | ok | 424 | 0.2473 | 0.2562 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 334 | -0.1631 | 0.0809 |
| seed_p | 334 | -0.1798 | -0.0337 |
| seed_p_vs_seed_pars | 307 | -0.5572 | -0.3753 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
