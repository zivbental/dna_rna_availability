# YGR254W
Status: ok. Length: 1505 nt. Measured usable bases: 409. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 409 | 0.1618 | 0.1471 |
| rnafold | ok | 409 | 0.0805 | 0.0747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 193 | 0.1722 | -0.1053 |
| seed_p | 193 | 0.0795 | -0.1855 |
| seed_p_vs_seed_pars | 148 | 0.0761 | -0.3763 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
