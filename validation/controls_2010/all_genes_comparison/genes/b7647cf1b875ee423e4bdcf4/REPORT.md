# YGL206C
Status: ok. Length: 5288 nt. Measured usable bases: 3122. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3122 | 0.3067 | 0.2932 |
| rnafold | ok | 3122 | 0.2564 | 0.2410 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 974 | -0.0507 | -0.0902 |
| seed_p | 974 | -0.0067 | 0.0064 |
| seed_p_vs_seed_pars | 764 | -0.0657 | -0.0739 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
