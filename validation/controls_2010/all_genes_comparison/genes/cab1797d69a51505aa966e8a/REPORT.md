# YCR059C
Status: ok. Length: 953 nt. Measured usable bases: 698. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 698 | 0.2590 | 0.2431 |
| rnafold | ok | 698 | 0.1776 | 0.1711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 541 | 0.2002 | 0.1385 |
| seed_p | 541 | -0.0165 | 0.0287 |
| seed_p_vs_seed_pars | 482 | -0.1365 | 0.0854 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
