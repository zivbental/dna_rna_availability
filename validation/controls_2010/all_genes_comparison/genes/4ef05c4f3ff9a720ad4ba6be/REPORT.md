# YDR378C
Status: ok. Length: 456 nt. Measured usable bases: 262. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 262 | 0.3167 | 0.3345 |
| rnafold | ok | 262 | 0.3373 | 0.3517 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 237 | -0.1879 | -0.1469 |
| seed_p | 237 | -0.1739 | -0.3007 |
| seed_p_vs_seed_pars | 220 | -0.4543 | -0.5420 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
