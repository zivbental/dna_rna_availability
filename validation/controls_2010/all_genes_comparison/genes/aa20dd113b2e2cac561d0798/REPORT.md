# YNR055C
Status: ok. Length: 2081 nt. Measured usable bases: 1332. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1332 | 0.2999 | 0.3041 |
| rnafold | ok | 1332 | 0.2083 | 0.2219 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 513 | -0.0822 | -0.3260 |
| seed_p | 513 | -0.2372 | -0.2505 |
| seed_p_vs_seed_pars | 409 | -0.2000 | -0.2359 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
