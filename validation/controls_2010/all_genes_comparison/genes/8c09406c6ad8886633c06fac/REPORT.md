# YBR249C
Status: ok. Length: 1338 nt. Measured usable bases: 1149. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1149 | 0.3710 | 0.3587 |
| rnafold | ok | 1149 | 0.2866 | 0.2971 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1063 | -0.1545 | -0.1780 |
| seed_p | 1063 | -0.2120 | -0.1774 |
| seed_p_vs_seed_pars | 946 | -0.4815 | -0.3508 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
