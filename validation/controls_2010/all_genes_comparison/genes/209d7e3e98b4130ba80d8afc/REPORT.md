# YGR167W
Status: ok. Length: 891 nt. Measured usable bases: 567. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 567 | 0.3722 | 0.3586 |
| rnafold | ok | 567 | 0.3390 | 0.3238 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 310 | -0.1260 | -0.0847 |
| seed_p | 310 | -0.0637 | 0.0206 |
| seed_p_vs_seed_pars | 247 | -0.4707 | -0.2319 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
