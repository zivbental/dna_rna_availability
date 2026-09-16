# YNR037C
Status: ok. Length: 383 nt. Measured usable bases: 227. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 227 | 0.4394 | 0.4202 |
| rnafold | ok | 227 | 0.4823 | 0.4856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.4611 | -0.5454 |
| seed_p | 101 | 0.1239 | 0.0960 |
| seed_p_vs_seed_pars | 81 | 0.4787 | 0.4382 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
