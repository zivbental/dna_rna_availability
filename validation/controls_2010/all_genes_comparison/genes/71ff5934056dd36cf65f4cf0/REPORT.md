# YDR143C
Status: ok. Length: 1964 nt. Measured usable bases: 781. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 781 | 0.2837 | 0.2829 |
| rnafold | ok | 781 | 0.3042 | 0.3140 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.0484 | 0.0238 |
| seed_p | 96 | -0.2387 | -0.2624 |
| seed_p_vs_seed_pars | 65 | 0.1891 | 0.1227 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
