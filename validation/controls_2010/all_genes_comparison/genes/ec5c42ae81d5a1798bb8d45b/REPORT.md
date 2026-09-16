# YAL023C
Status: ok. Length: 2475 nt. Measured usable bases: 2028. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2028 | 0.3240 | 0.3079 |
| rnafold | ok | 2028 | 0.2808 | 0.2736 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1801 | -0.1177 | -0.1761 |
| seed_p | 1801 | -0.2022 | -0.1407 |
| seed_p_vs_seed_pars | 1535 | -0.2539 | -0.2310 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
