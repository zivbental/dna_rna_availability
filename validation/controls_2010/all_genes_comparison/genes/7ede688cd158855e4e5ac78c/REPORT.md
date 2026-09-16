# YLL022C
Status: ok. Length: 1288 nt. Measured usable bases: 540. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 540 | 0.2288 | 0.2359 |
| rnafold | ok | 540 | 0.1790 | 0.1875 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | 0.3139 | 0.3419 |
| seed_p | 46 | -0.2742 | -0.0847 |
| seed_p_vs_seed_pars | 29 | 0.1581 | -0.0154 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
