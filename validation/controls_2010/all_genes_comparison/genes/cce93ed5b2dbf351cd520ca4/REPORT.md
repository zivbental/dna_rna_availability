# YNL169C
Status: ok. Length: 1629 nt. Measured usable bases: 975. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 975 | 0.2848 | 0.2738 |
| rnafold | ok | 975 | 0.2257 | 0.2202 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | 0.0236 | 0.2860 |
| seed_p | 377 | 0.0512 | 0.2134 |
| seed_p_vs_seed_pars | 278 | -0.0913 | 0.1766 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
