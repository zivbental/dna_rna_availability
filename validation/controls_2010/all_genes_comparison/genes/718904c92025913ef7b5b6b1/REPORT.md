# YIL039W
Status: ok. Length: 1563 nt. Measured usable bases: 1144. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1144 | 0.2840 | 0.2724 |
| rnafold | ok | 1144 | 0.2835 | 0.2660 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 750 | 0.1091 | 0.1735 |
| seed_p | 750 | 0.0617 | 0.1555 |
| seed_p_vs_seed_pars | 588 | -0.1048 | 0.0091 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
