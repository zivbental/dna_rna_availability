# YDL121C
Status: ok. Length: 641 nt. Measured usable bases: 397. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 397 | 0.3089 | 0.3059 |
| rnafold | ok | 397 | 0.2214 | 0.2487 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.0216 | -0.4062 |
| seed_p | 153 | -0.0890 | -0.2603 |
| seed_p_vs_seed_pars | 96 | -0.6242 | -0.6235 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
