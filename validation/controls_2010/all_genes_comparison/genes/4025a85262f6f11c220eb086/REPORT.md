# YPL023C
Status: ok. Length: 2223 nt. Measured usable bases: 1119. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1119 | 0.3315 | 0.3118 |
| rnafold | ok | 1119 | 0.2808 | 0.2538 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | -0.2008 | -0.2120 |
| seed_p | 249 | -0.2291 | -0.1959 |
| seed_p_vs_seed_pars | 158 | -0.4192 | -0.3250 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
