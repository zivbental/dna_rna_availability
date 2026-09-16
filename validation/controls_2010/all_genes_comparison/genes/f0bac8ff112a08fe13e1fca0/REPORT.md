# YIL063C
Status: ok. Length: 1030 nt. Measured usable bases: 423. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 423 | 0.4103 | 0.4103 |
| rnafold | ok | 423 | 0.3354 | 0.3335 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | 0.6847 | 0.4699 |
| seed_p | 50 | 0.3178 | 0.3502 |
| seed_p_vs_seed_pars | 35 | 0.0861 | 0.1813 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
