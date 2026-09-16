# YDR135C
Status: ok. Length: 4658 nt. Measured usable bases: 2489. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2489 | 0.2972 | 0.2851 |
| rnafold | ok | 2489 | 0.2476 | 0.2358 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 651 | 0.0347 | 0.2417 |
| seed_p | 651 | 0.1570 | 0.1943 |
| seed_p_vs_seed_pars | 403 | 0.0941 | 0.1337 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
