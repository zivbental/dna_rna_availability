# YGR157W
Status: ok. Length: 2932 nt. Measured usable bases: 1802. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1802 | 0.3312 | 0.3059 |
| rnafold | ok | 1802 | 0.2658 | 0.2593 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 836 | -0.0821 | -0.2298 |
| seed_p | 836 | -0.1978 | -0.2663 |
| seed_p_vs_seed_pars | 557 | -0.4176 | -0.3213 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
