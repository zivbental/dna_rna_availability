# YKL122C
Status: ok. Length: 593 nt. Measured usable bases: 242. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 242 | 0.2950 | 0.2794 |
| rnafold | ok | 242 | 0.3299 | 0.2944 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.1471 | -0.4830 |
| seed_p | 79 | -0.4859 | -0.5406 |
| seed_p_vs_seed_pars | 47 | -0.2776 | -0.4596 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
