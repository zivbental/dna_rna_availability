# YHR151C
Status: ok. Length: 1581 nt. Measured usable bases: 684. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 684 | 0.3041 | 0.3027 |
| rnafold | ok | 684 | 0.2320 | 0.2262 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | 0.5627 | 0.2218 |
| seed_p | 74 | -0.1835 | -0.1918 |
| seed_p_vs_seed_pars | 64 | -0.3344 | -0.2502 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
