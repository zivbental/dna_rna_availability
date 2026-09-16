# YDL147W
Status: ok. Length: 1525 nt. Measured usable bases: 870. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 870 | 0.3095 | 0.3071 |
| rnafold | ok | 870 | 0.2713 | 0.2601 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 342 | -0.0303 | 0.1051 |
| seed_p | 342 | -0.0113 | 0.0409 |
| seed_p_vs_seed_pars | 219 | -0.1938 | -0.1125 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
