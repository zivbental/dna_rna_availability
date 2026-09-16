# YDR541C
Status: ok. Length: 1345 nt. Measured usable bases: 591. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 591 | 0.1857 | 0.1819 |
| rnafold | ok | 591 | 0.1054 | 0.1151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | 0.0661 | -0.0186 |
| seed_p | 77 | 0.4124 | 0.2650 |
| seed_p_vs_seed_pars | 68 | 0.4898 | 0.5243 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
