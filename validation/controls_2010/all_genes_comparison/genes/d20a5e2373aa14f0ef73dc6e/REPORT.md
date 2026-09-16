# YKL206C
Status: ok. Length: 887 nt. Measured usable bases: 442. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 442 | 0.4558 | 0.4428 |
| rnafold | ok | 442 | 0.4011 | 0.3775 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.8591 | -0.7910 |
| seed_p | 61 | -0.8045 | -0.7901 |
| seed_p_vs_seed_pars | 53 | -0.9134 | -0.9541 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
