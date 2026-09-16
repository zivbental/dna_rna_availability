# YMR197C
Status: ok. Length: 847 nt. Measured usable bases: 421. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 421 | 0.2872 | 0.2683 |
| rnafold | ok | 421 | 0.2467 | 0.2486 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | 0.1388 | 0.1676 |
| seed_p | 95 | -0.6250 | -0.5830 |
| seed_p_vs_seed_pars | 78 | -0.7044 | -0.4302 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
