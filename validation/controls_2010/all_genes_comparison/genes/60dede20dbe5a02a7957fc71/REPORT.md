# YPL134C
Status: ok. Length: 1229 nt. Measured usable bases: 479. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 479 | 0.4568 | 0.4476 |
| rnafold | ok | 479 | 0.4116 | 0.4242 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.5888 | -0.5458 |
| seed_p | 65 | -0.3033 | -0.2722 |
| seed_p_vs_seed_pars | 40 | -0.4456 | -0.6062 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
