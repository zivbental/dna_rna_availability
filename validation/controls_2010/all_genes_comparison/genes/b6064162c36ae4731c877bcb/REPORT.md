# YHR167W
Status: ok. Length: 900 nt. Measured usable bases: 325. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 325 | 0.3597 | 0.3346 |
| rnafold | ok | 325 | 0.2347 | 0.2230 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.4096 | -0.2999 |
| seed_p | 43 | -0.4121 | -0.2412 |
| seed_p_vs_seed_pars | 22 | -0.7090 | -0.8815 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
