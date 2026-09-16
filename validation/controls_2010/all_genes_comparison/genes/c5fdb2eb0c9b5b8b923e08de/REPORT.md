# YGL006W
Status: ok. Length: 3932 nt. Measured usable bases: 1332. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1332 | 0.3456 | 0.3231 |
| rnafold | ok | 1332 | 0.2874 | 0.2594 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.3118 | -0.0983 |
| seed_p | 92 | -0.2396 | -0.2757 |
| seed_p_vs_seed_pars | 53 | -0.4115 | -0.4622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
