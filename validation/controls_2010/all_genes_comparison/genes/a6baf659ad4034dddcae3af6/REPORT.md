# RDN58-2
Status: ok. Length: 158 nt. Measured usable bases: 147. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 147 | 0.1303 | 0.1180 |
| rnafold | ok | 147 | 0.1221 | 0.0924 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | 0.1727 | 0.1538 |
| seed_p | 123 | 0.2246 | 0.1615 |
| seed_p_vs_seed_pars | 123 | 0.1627 | 0.2040 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
