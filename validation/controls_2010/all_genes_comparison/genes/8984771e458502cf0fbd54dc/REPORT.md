# YHR042W
Status: ok. Length: 2234 nt. Measured usable bases: 1747. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1747 | 0.2627 | 0.2545 |
| rnafold | ok | 1747 | 0.2126 | 0.2083 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1405 | -0.1113 | -0.2270 |
| seed_p | 1405 | -0.1687 | -0.2039 |
| seed_p_vs_seed_pars | 1125 | -0.2865 | -0.2950 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
