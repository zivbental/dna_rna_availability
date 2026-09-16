# YER026C
Status: ok. Length: 1003 nt. Measured usable bases: 749. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 749 | 0.2684 | 0.2451 |
| rnafold | ok | 749 | 0.2521 | 0.2470 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 590 | -0.1459 | 0.0209 |
| seed_p | 590 | -0.2875 | -0.2118 |
| seed_p_vs_seed_pars | 497 | -0.4409 | -0.2774 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
