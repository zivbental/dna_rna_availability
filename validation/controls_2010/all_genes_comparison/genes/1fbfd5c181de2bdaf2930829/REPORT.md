# YLR029C
Status: ok. Length: 709 nt. Measured usable bases: 389. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 389 | 0.3572 | 0.3633 |
| rnafold | ok | 389 | 0.3201 | 0.3390 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 261 | -0.0226 | -0.3355 |
| seed_p | 261 | -0.2071 | -0.2151 |
| seed_p_vs_seed_pars | 225 | -0.0832 | -0.0036 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
