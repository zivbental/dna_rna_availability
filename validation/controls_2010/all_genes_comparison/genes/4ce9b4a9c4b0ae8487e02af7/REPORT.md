# YGL008C
Status: ok. Length: 3486 nt. Measured usable bases: 3037. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3037 | 0.3333 | 0.3253 |
| rnafold | ok | 3037 | 0.2770 | 0.2672 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2764 | -0.2229 | -0.3004 |
| seed_p | 2764 | -0.2523 | -0.2642 |
| seed_p_vs_seed_pars | 2584 | -0.3020 | -0.3142 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
