# YOR231W
Status: ok. Length: 1805 nt. Measured usable bases: 763. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 763 | 0.2893 | 0.2807 |
| rnafold | ok | 763 | 0.2733 | 0.2516 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | 0.3735 | 0.7425 |
| seed_p | 70 | 0.6688 | 0.6917 |
| seed_p_vs_seed_pars | 48 | 0.5885 | 0.6156 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
