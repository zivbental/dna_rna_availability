# YGL009C
Status: ok. Length: 2528 nt. Measured usable bases: 1743. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1743 | 0.3158 | 0.3087 |
| rnafold | ok | 1743 | 0.2668 | 0.2517 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 999 | 0.1351 | 0.0088 |
| seed_p | 999 | -0.0720 | -0.0780 |
| seed_p_vs_seed_pars | 783 | -0.2528 | -0.2496 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
