# YBR220C
Status: ok. Length: 1958 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.2334 | 0.2394 |
| rnafold | ok | 1141 | 0.2014 | 0.1996 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 664 | 0.0936 | 0.2444 |
| seed_p | 664 | 0.1444 | 0.1758 |
| seed_p_vs_seed_pars | 473 | 0.0889 | 0.0891 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
