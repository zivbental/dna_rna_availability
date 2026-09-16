# YGL067W
Status: ok. Length: 1298 nt. Measured usable bases: 685. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 685 | 0.3214 | 0.2966 |
| rnafold | ok | 685 | 0.2973 | 0.2796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.6781 | -0.4085 |
| seed_p | 121 | -0.2922 | -0.3265 |
| seed_p_vs_seed_pars | 90 | -0.7346 | -0.6865 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
