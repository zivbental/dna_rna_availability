# YDL145C
Status: ok. Length: 3983 nt. Measured usable bases: 2767. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2767 | 0.3186 | 0.3071 |
| rnafold | ok | 2767 | 0.2566 | 0.2527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1651 | -0.1448 | -0.1837 |
| seed_p | 1651 | -0.3381 | -0.3211 |
| seed_p_vs_seed_pars | 1161 | -0.4207 | -0.4063 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
