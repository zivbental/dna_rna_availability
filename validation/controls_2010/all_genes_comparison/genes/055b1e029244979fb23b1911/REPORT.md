# YMR194W
Status: ok. Length: 402 nt. Measured usable bases: 231. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 231 | 0.2645 | 0.2660 |
| rnafold | ok | 231 | 0.2213 | 0.2243 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 156 | -0.3490 | -0.3738 |
| seed_p | 156 | -0.2965 | -0.4453 |
| seed_p_vs_seed_pars | 129 | -0.0921 | -0.3100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
