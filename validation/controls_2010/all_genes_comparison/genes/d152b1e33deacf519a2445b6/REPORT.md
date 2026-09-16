# YDR346C
Status: ok. Length: 1856 nt. Measured usable bases: 1255. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1255 | 0.3569 | 0.3506 |
| rnafold | ok | 1255 | 0.2966 | 0.3039 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 673 | -0.0367 | -0.2233 |
| seed_p | 673 | -0.1693 | -0.1773 |
| seed_p_vs_seed_pars | 524 | -0.2356 | -0.2469 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
