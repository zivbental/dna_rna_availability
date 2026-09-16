# YDR382W
Status: ok. Length: 546 nt. Measured usable bases: 443. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 443 | 0.2335 | 0.2244 |
| rnafold | ok | 443 | 0.2120 | 0.2098 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 385 | -0.0389 | -0.2710 |
| seed_p | 385 | 0.0763 | -0.0018 |
| seed_p_vs_seed_pars | 377 | -0.0100 | 0.0164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
