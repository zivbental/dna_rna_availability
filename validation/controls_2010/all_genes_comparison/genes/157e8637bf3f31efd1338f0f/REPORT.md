# YDR497C
Status: ok. Length: 1916 nt. Measured usable bases: 1588. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1588 | 0.2807 | 0.2685 |
| rnafold | ok | 1588 | 0.2046 | 0.2003 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1414 | -0.0719 | 0.0097 |
| seed_p | 1414 | -0.2794 | -0.1632 |
| seed_p_vs_seed_pars | 1129 | -0.3820 | -0.2715 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
