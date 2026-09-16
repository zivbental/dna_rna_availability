# YPL145C
Status: ok. Length: 1997 nt. Measured usable bases: 1533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1533 | 0.2700 | 0.2666 |
| rnafold | ok | 1533 | 0.2128 | 0.2048 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1094 | -0.1986 | -0.1111 |
| seed_p | 1094 | -0.2619 | -0.1979 |
| seed_p_vs_seed_pars | 876 | -0.4006 | -0.2577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
