# YNL261W
Status: ok. Length: 1901 nt. Measured usable bases: 866. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 866 | 0.2767 | 0.2819 |
| rnafold | ok | 866 | 0.3040 | 0.3161 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 146 | -0.2662 | -0.3102 |
| seed_p | 146 | -0.3636 | -0.4527 |
| seed_p_vs_seed_pars | 85 | -0.5670 | -0.5888 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
