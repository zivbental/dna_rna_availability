# YGR177C
Status: ok. Length: 1608 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.2629 | 0.2692 |
| rnafold | ok | 846 | 0.2168 | 0.2353 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 200 | -0.0023 | 0.1872 |
| seed_p | 200 | -0.1441 | -0.0469 |
| seed_p_vs_seed_pars | 130 | -0.0788 | -0.0125 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
