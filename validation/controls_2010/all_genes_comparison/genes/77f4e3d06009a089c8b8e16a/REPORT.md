# YLL023C
Status: ok. Length: 976 nt. Measured usable bases: 592. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 592 | 0.3087 | 0.2832 |
| rnafold | ok | 592 | 0.2997 | 0.2740 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 320 | -0.2537 | -0.1318 |
| seed_p | 320 | -0.2824 | -0.1900 |
| seed_p_vs_seed_pars | 197 | -0.1754 | -0.1061 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
