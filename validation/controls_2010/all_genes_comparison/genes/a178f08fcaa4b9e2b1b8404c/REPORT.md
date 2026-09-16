# YDL111C
Status: ok. Length: 798 nt. Measured usable bases: 556. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.2174 | 0.2087 |
| rnafold | ok | 556 | 0.1722 | 0.1759 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 304 | 0.1944 | -0.0722 |
| seed_p | 304 | 0.1262 | 0.0078 |
| seed_p_vs_seed_pars | 239 | 0.1293 | 0.0572 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
