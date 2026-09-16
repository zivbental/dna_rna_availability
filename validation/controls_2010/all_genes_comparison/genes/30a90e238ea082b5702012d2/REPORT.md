# YPL177C
Status: ok. Length: 1413 nt. Measured usable bases: 666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 666 | 0.3603 | 0.3589 |
| rnafold | ok | 666 | 0.2711 | 0.2788 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 220 | -0.2392 | -0.3600 |
| seed_p | 220 | -0.2366 | -0.3249 |
| seed_p_vs_seed_pars | 157 | -0.3914 | -0.4222 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
