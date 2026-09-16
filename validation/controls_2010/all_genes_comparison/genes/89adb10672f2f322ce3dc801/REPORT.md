# YGL122C
Status: ok. Length: 1816 nt. Measured usable bases: 993. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 993 | 0.2900 | 0.2865 |
| rnafold | ok | 993 | 0.2027 | 0.2065 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 280 | 0.1671 | 0.1099 |
| seed_p | 280 | 0.1023 | 0.0326 |
| seed_p_vs_seed_pars | 207 | 0.1159 | 0.1717 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
