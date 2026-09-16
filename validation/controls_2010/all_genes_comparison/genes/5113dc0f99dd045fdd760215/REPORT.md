# YCR043C
Status: ok. Length: 575 nt. Measured usable bases: 373. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 373 | 0.1352 | 0.1341 |
| rnafold | ok | 373 | 0.0849 | 0.0902 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 201 | -0.0580 | -0.1563 |
| seed_p | 201 | -0.3063 | -0.2141 |
| seed_p_vs_seed_pars | 153 | -0.4640 | -0.3832 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
