# YLR020C
Status: ok. Length: 1814 nt. Measured usable bases: 870. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 870 | 0.2967 | 0.2921 |
| rnafold | ok | 870 | 0.2711 | 0.2749 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | 0.1650 | 0.3113 |
| seed_p | 191 | 0.0288 | 0.0859 |
| seed_p_vs_seed_pars | 119 | 0.1562 | 0.1675 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
