# YDR077W
Status: ok. Length: 1417 nt. Measured usable bases: 1022. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1022 | 0.1345 | 0.1060 |
| rnafold | ok | 1022 | 0.0797 | 0.0676 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 906 | -0.0135 | 0.0768 |
| seed_p | 906 | -0.0290 | -0.0081 |
| seed_p_vs_seed_pars | 847 | -0.1295 | -0.1742 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
