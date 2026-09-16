# YGL035C
Status: ok. Length: 1856 nt. Measured usable bases: 741. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 741 | 0.3360 | 0.3320 |
| rnafold | ok | 741 | 0.2770 | 0.2795 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | 0.0458 | -0.3617 |
| seed_p | 49 | -0.2992 | -0.1069 |
| seed_p_vs_seed_pars | 37 | -0.5088 | -0.2193 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
