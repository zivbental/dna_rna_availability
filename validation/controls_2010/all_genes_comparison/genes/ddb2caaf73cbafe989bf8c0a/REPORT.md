# YGL002W
Status: ok. Length: 926 nt. Measured usable bases: 554. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 554 | 0.3490 | 0.3379 |
| rnafold | ok | 554 | 0.3289 | 0.3298 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 226 | -0.2321 | -0.3886 |
| seed_p | 226 | -0.1411 | -0.1563 |
| seed_p_vs_seed_pars | 179 | -0.3166 | -0.4187 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
