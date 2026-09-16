# YGL026C
Status: ok. Length: 2213 nt. Measured usable bases: 1819. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1819 | 0.3219 | 0.2930 |
| rnafold | ok | 1819 | 0.2519 | 0.2436 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1555 | -0.1231 | 0.0536 |
| seed_p | 1555 | -0.1388 | -0.0773 |
| seed_p_vs_seed_pars | 1288 | -0.1889 | -0.1373 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
