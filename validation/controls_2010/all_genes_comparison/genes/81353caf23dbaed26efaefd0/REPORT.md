# YBR287W
Status: ok. Length: 1373 nt. Measured usable bases: 814. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 814 | 0.2941 | 0.2756 |
| rnafold | ok | 814 | 0.2195 | 0.2018 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 255 | -0.1397 | -0.2155 |
| seed_p | 255 | -0.4557 | -0.5362 |
| seed_p_vs_seed_pars | 185 | -0.4258 | -0.5183 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
