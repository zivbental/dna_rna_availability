# YDR013W
Status: ok. Length: 746 nt. Measured usable bases: 290. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 290 | 0.2749 | 0.2759 |
| rnafold | ok | 290 | 0.2677 | 0.2726 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | 0.2377 | 0.1226 |
| seed_p | 20 | -0.4346 | -0.4088 |
| seed_p_vs_seed_pars | 10 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
