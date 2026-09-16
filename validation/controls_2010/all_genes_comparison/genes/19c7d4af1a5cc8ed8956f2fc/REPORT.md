# YDR368W
Status: ok. Length: 1174 nt. Measured usable bases: 901. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 901 | 0.3269 | 0.3288 |
| rnafold | ok | 901 | 0.2530 | 0.2592 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 684 | -0.1982 | -0.1776 |
| seed_p | 684 | -0.2053 | -0.2147 |
| seed_p_vs_seed_pars | 570 | -0.1563 | -0.2003 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
