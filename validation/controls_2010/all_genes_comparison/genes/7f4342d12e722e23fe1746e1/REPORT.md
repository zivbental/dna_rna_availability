# YPL245W
Status: ok. Length: 1477 nt. Measured usable bases: 819. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 819 | 0.3354 | 0.3227 |
| rnafold | ok | 819 | 0.2798 | 0.2537 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 267 | -0.2111 | -0.1720 |
| seed_p | 267 | -0.4555 | -0.3619 |
| seed_p_vs_seed_pars | 191 | -0.6089 | -0.4862 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
