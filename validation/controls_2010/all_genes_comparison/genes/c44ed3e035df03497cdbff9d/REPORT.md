# YGR046W
Status: ok. Length: 1648 nt. Measured usable bases: 613. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.3191 | 0.3166 |
| rnafold | ok | 613 | 0.2738 | 0.2767 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | 0.4817 | 0.7161 |
| seed_p | 20 | -0.0515 | 0.3287 |
| seed_p_vs_seed_pars | 14 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
