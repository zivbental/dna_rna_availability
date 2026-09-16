# YML128C
Status: ok. Length: 1813 nt. Measured usable bases: 776. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 776 | 0.3189 | 0.3063 |
| rnafold | ok | 776 | 0.2604 | 0.2602 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | 0.1802 | 0.4883 |
| seed_p | 76 | 0.2444 | 0.2516 |
| seed_p_vs_seed_pars | 68 | 0.1787 | 0.1702 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
