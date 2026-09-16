# YBR084W
Status: ok. Length: 3160 nt. Measured usable bases: 2317. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2317 | 0.3520 | 0.3385 |
| rnafold | ok | 2317 | 0.3290 | 0.3100 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1553 | -0.0092 | 0.0507 |
| seed_p | 1553 | -0.1968 | -0.1040 |
| seed_p_vs_seed_pars | 1271 | -0.3071 | -0.1708 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
